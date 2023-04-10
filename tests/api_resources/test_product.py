from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "prod_123"


class TestProduct(object):
    def test_is_listable(self, request_mock):
        resources = paayes.Product.list()
        request_mock.assert_requested("get", "/api/v1/products")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.Product)

    def test_is_retrievable(self, request_mock):
        resource = paayes.Product.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/products/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Product)

    def test_is_creatable(self, request_mock):
        resource = paayes.Product.create(name="NAME")
        request_mock.assert_requested("post", "/api/v1/products")
        assert isinstance(resource, paayes.Product)

    def test_is_saveable(self, request_mock):
        resource = paayes.Product.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/api/v1/products/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = paayes.Product.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/api/v1/products/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Product)

    def test_is_deletable(self, request_mock):
        resource = paayes.Product.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/api/v1/products/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, request_mock):
        resource = paayes.Product.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/api/v1/products/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
