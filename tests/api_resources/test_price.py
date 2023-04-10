from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "price_123"


class TestPrice(object):
    def test_is_listable(self, request_mock):
        resources = paayes.Price.list()
        request_mock.assert_requested("get", "/api/v1/prices")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.Price)

    def test_is_retrievable(self, request_mock):
        resource = paayes.Price.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/prices/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Price)

    def test_is_creatable(self, request_mock):
        resource = paayes.Price.create(
            unit_amount=1000,
            currency="usd",
            recurring={"interval": "month"},
            product_data={"name": "price_nickname"},
        )
        request_mock.assert_requested("post", "/api/v1/prices")
        assert isinstance(resource, paayes.Price)

    def test_is_saveable(self, request_mock):
        resource = paayes.Price.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/api/v1/prices/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = paayes.Price.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/api/v1/prices/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Price)
