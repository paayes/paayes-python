from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "ii_123"


class TestInvoiceItem(object):
    def test_is_listable(self, request_mock):
        resources = paayes.InvoiceItem.list()
        request_mock.assert_requested("get", "/api/v1/invoiceitems")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.InvoiceItem)

    def test_is_retrievable(self, request_mock):
        resource = paayes.InvoiceItem.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/invoiceitems/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.InvoiceItem)

    def test_is_creatable(self, request_mock):
        resource = paayes.InvoiceItem.create(
            customer="cus_123", amount=123, currency="usd"
        )
        request_mock.assert_requested("post", "/api/v1/invoiceitems")
        assert isinstance(resource, paayes.InvoiceItem)

    def test_is_saveable(self, request_mock):
        resource = paayes.InvoiceItem.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/api/v1/invoiceitems/%s" % TEST_RESOURCE_ID
        )

    def test_can_delete(self, request_mock):
        resource = paayes.InvoiceItem.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/api/v1/invoiceitems/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_is_modifiable(self, request_mock):
        resource = paayes.InvoiceItem.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/api/v1/invoiceitems/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.InvoiceItem)

    def test_is_deletable(self, request_mock):
        resource = paayes.InvoiceItem.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/api/v1/invoiceitems/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
