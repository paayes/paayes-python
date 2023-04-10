from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "issfr_123"


class TestEarlyFraudWarning(object):
    def test_is_listable(self, request_mock):
        resources = paayes.radar.EarlyFraudWarning.list()
        request_mock.assert_requested("get", "/api/v1/radar/early_fraud_warnings")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.radar.EarlyFraudWarning)

    def test_is_retrievable(self, request_mock):
        resource = paayes.radar.EarlyFraudWarning.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/radar/early_fraud_warnings/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.radar.EarlyFraudWarning)