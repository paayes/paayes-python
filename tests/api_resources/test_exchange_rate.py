from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "usd"


class TestExchangeRate(object):
    def test_is_listable(self, request_mock):
        resources = paayes.ExchangeRate.list()
        request_mock.assert_requested("get", "/api/v1/exchange_rates")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.ExchangeRate)

    def test_is_retrievable(self, request_mock):
        resource = paayes.ExchangeRate.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/exchange_rates/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.ExchangeRate)
