from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "or_123"


class TestOrder(object):
    def test_is_listable(self, request_mock):
        resources = paayes.Order.list()
        request_mock.assert_requested("get", "/api/v1/orders")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.Order)

    def test_is_retrievable(self, request_mock):
        resource = paayes.Order.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/orders/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Order)

    def test_is_creatable(self, request_mock):
        resource = paayes.Order.create(currency="usd")
        request_mock.assert_requested("post", "/api/v1/orders")
        assert isinstance(resource, paayes.Order)

    def test_is_saveable(self, request_mock):
        resource = paayes.Order.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/api/v1/orders/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = paayes.Order.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/api/v1/orders/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Order)

    def test_can_pay(self, request_mock):
        order = paayes.Order.retrieve(TEST_RESOURCE_ID)
        resource = order.pay(source="src_123")
        request_mock.assert_requested(
            "post",
            "/api/v1/orders/%s/pay" % TEST_RESOURCE_ID,
            {"source": "src_123"},
        )
        assert isinstance(resource, paayes.Order)
        assert resource is order

    def test_can_pay_classmethod(self, request_mock):
        resource = paayes.Order.pay(TEST_RESOURCE_ID, source="src_123")
        request_mock.assert_requested(
            "post",
            "/api/v1/orders/%s/pay" % TEST_RESOURCE_ID,
            {"source": "src_123"},
        )
        assert isinstance(resource, paayes.Order)

    def test_can_return(self, request_mock):
        order = paayes.Order.retrieve(TEST_RESOURCE_ID)
        resource = order.return_order()
        request_mock.assert_requested(
            "post", "/api/v1/orders/%s/returns" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.OrderReturn)

    def test_can_return_classmethod(self, request_mock):
        resource = paayes.Order.return_order(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/api/v1/orders/%s/returns" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.OrderReturn)
