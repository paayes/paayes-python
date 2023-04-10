from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "sku_123"


class TestSKU(object):
    def test_is_listable(self, request_mock):
        resources = paayes.SKU.list()
        request_mock.assert_requested("get", "/api/v1/skus")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.SKU)

    def test_is_retrievable(self, request_mock):
        resource = paayes.SKU.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/api/v1/skus/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, paayes.SKU)

    def test_is_creatable(self, request_mock):
        resource = paayes.SKU.create(
            currency="usd",
            inventory=dict(type="finite", quantity=500),
            price=100,
            product="prod_123",
        )
        request_mock.assert_requested("post", "/api/v1/skus")
        assert isinstance(resource, paayes.SKU)

    def test_is_saveable(self, request_mock):
        resource = paayes.SKU.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested("post", "/api/v1/skus/%s" % TEST_RESOURCE_ID)

    def test_is_modifiable(self, request_mock):
        resource = paayes.SKU.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested("post", "/api/v1/skus/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, paayes.SKU)

    def test_is_deletable(self, request_mock):
        resource = paayes.SKU.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/api/v1/skus/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, request_mock):
        resource = paayes.SKU.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/api/v1/skus/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
