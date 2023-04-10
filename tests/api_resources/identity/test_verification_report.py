from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "vs_123"


class TestVerificationReport(object):
    def test_is_listable(self, request_mock):
        resources = paayes.identity.VerificationReport.list()
        request_mock.assert_requested(
            "get", "/api/v1/identity/verification_reports"
        )
        assert isinstance(resources.data, list)
        assert isinstance(
            resources.data[0], paayes.identity.VerificationReport
        )

    def test_is_retrievable(self, request_mock):
        resource = paayes.identity.VerificationReport.retrieve(
            TEST_RESOURCE_ID
        )
        request_mock.assert_requested(
            "get", "/api/v1/identity/verification_reports/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.identity.VerificationReport)
