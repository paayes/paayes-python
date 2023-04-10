from __future__ import absolute_import, division, print_function

import atexit
import os
import sys
from distutils.version import StrictVersion

import pytest

import paayes
from paayes.six.moves.urllib.request import urlopen
from paayes.six.moves.urllib.error import HTTPError

from tests.request_mock import RequestMock
from tests.paayes_mock import PaayesMock

MOCK_MINIMUM_VERSION = "0.109.0"

# Starts paayes-mock if an OpenAPI spec override is found in `openapi/`, and
# otherwise fall back to `PAAYES_MOCK_PORT` or 12111.
if PaayesMock.start():
    MOCK_PORT = PaayesMock.port()
else:
    MOCK_PORT = os.environ.get("PAAYES_MOCK_PORT", 12111)


@atexit.register
def stop_paayes_mock():
    PaayesMock.stop()


def pytest_configure(config):
    if not config.getoption("--nomock"):
        try:
            resp = urlopen("http://localhost:%s/" % MOCK_PORT)
            info = resp.info()
            version = info.get("Paayes-Mock-Version")
            if version != "master" and StrictVersion(version) < StrictVersion(
                MOCK_MINIMUM_VERSION
            ):
                sys.exit(
                    "Your version of paayes-mock (%s) is too old. The minimum "
                    "version to run this test suite is %s. Please "
                    "see its repository for upgrade instructions."
                    % (version, MOCK_MINIMUM_VERSION)
                )

        except HTTPError as e:
            info = e.info()
        except Exception:
            sys.exit(
                "Couldn't reach paayes-mock at `localhost:%s`. Is "
                "it running? Please see README for setup instructions."
                % MOCK_PORT
            )


def pytest_addoption(parser):
    parser.addoption(
        "--nomock",
        action="store_true",
        help="only run tests that don't need paayes-mock",
    )


def pytest_runtest_setup(item):
    if "request_mock" in item.fixturenames and item.config.getoption(
        "--nomock"
    ):
        pytest.skip(
            "run paayes-mock locally and remove --nomock flag to run skipped tests"
        )


@pytest.fixture(autouse=True)
def setup_paayes():
    orig_attrs = {
        "api_base": paayes.api_base,
        "api_key": paayes.api_key,
        "client_id": paayes.client_id,
        "default_http_client": paayes.default_http_client,
    }
    http_client = paayes.http_client.new_default_http_client()
    paayes.api_base = "http://localhost:%s" % MOCK_PORT
    paayes.api_key = "sk_test_123"
    paayes.client_id = "ca_123"
    paayes.default_http_client = http_client
    yield
    http_client.close()
    paayes.api_base = orig_attrs["api_base"]
    paayes.api_key = orig_attrs["api_key"]
    paayes.client_id = orig_attrs["client_id"]
    paayes.default_http_client = orig_attrs["default_http_client"]


@pytest.fixture
def request_mock(mocker):
    return RequestMock(mocker)
