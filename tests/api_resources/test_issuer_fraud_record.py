from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "issfr_123"


class TestIssuerFraudRecord(object):
    def test_is_listable(self, request_mock):
        resources = paayes.IssuerFraudRecord.list()
        request_mock.assert_requested("get", "/api/v1/issuer_fraud_records")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.IssuerFraudRecord)

    def test_is_retrievable(self, request_mock):
        resource = paayes.IssuerFraudRecord.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/issuer_fraud_records/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.IssuerFraudRecord)
