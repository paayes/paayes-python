from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "orret_123"


class TestOrderReturn(object):
    def test_is_listable(self, request_mock):
        resources = paayes.OrderReturn.list()
        request_mock.assert_requested("get", "/api/v1/order_returns")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.OrderReturn)

    def test_is_retrievable(self, request_mock):
        resource = paayes.OrderReturn.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/order_returns/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.OrderReturn)
