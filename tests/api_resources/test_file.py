from __future__ import absolute_import, division, print_function

import tempfile

import pytest

import paayes


TEST_RESOURCE_ID = "file_123"


class TestFile(object):
    @pytest.fixture(scope="function")
    def setup_upload_api_base(self):
        paayes.upload_api_base = paayes.api_base
        paayes.api_base = None
        yield
        paayes.api_base = paayes.upload_api_base
        paayes.upload_api_base = "https://files.paayes.com"

    def test_is_listable(self, request_mock):
        resources = paayes.File.list()
        request_mock.assert_requested("get", "/api/v1/files")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.File)

    def test_is_retrievable(self, request_mock):
        resource = paayes.File.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/api/v1/files/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, paayes.File)

    def test_is_creatable(self, setup_upload_api_base, request_mock):
        paayes.multipart_data_generator.MultipartDataGenerator._initialize_boundary = (
            lambda self: 1234567890
        )
        test_file = tempfile.TemporaryFile()
        resource = paayes.File.create(
            purpose="dispute_evidence",
            file=test_file,
            file_link_data={"create": True},
        )
        request_mock.assert_api_base(paayes.upload_api_base)
        request_mock.assert_requested(
            "post",
            "/api/v1/files",
            headers={
                "Content-Type": "multipart/form-data; boundary=1234567890"
            },
        )
        assert isinstance(resource, paayes.File)

    def test_create_respects_paayes_version(
        self, setup_upload_api_base, request_mock
    ):
        test_file = tempfile.TemporaryFile()
        paayes.File.create(
            purpose="dispute_evidence", file=test_file, paayes_version="foo"
        )
        request_mock.assert_api_version("foo")

    # You can use api_version instead of paayes_version
    # in File.create. We preserve it for backwards compatibility
    def test_create_respects_api_version(
        self, setup_upload_api_base, request_mock
    ):
        test_file = tempfile.TemporaryFile()
        paayes.File.create(
            purpose="dispute_evidence", file=test_file, api_version="foo"
        )
        request_mock.assert_api_version("foo")

    def test_deserializes_from_file(self):
        obj = paayes.util.convert_to_paayes_object({"object": "file"})
        assert isinstance(obj, paayes.File)

    def test_deserializes_from_file_upload(self):
        obj = paayes.util.convert_to_paayes_object({"object": "file_upload"})
        assert isinstance(obj, paayes.File)
