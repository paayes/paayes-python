from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "cus_123"
TEST_SUB_ID = "sub_123"
TEST_SOURCE_ID = "ba_123"
TEST_TAX_ID_ID = "txi_123"
TEST_TRANSACTION_ID = "cbtxn_123"


class TestCustomer(object):
    def test_is_listable(self, request_mock):
        resources = paayes.Customer.list()
        request_mock.assert_requested("get", "/api/v1/customers")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.Customer)

    def test_is_retrievable(self, request_mock):
        resource = paayes.Customer.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/customers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Customer)

    def test_is_creatable(self, request_mock):
        resource = paayes.Customer.create()
        request_mock.assert_requested("post", "/api/v1/customers")
        assert isinstance(resource, paayes.Customer)

    def test_is_saveable(self, request_mock):
        resource = paayes.Customer.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/api/v1/customers/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = paayes.Customer.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/api/v1/customers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Customer)

    def test_is_deletable(self, request_mock):
        resource = paayes.Customer.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/api/v1/customers/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, request_mock):
        resource = paayes.Customer.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/api/v1/customers/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete_discount(self, request_mock):
        resource = paayes.Customer.retrieve(TEST_RESOURCE_ID)
        resource.delete_discount()
        request_mock.assert_requested(
            "delete", "/api/v1/customers/%s/discount" % TEST_RESOURCE_ID
        )

    def test_can_delete_discount_class_method(self, request_mock):
        paayes.Customer.delete_discount(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/api/v1/customers/%s/discount" % TEST_RESOURCE_ID
        )


class TestCustomerSources(object):
    def test_is_creatable(self, request_mock):
        paayes.Customer.create_source(TEST_RESOURCE_ID, source="btok_123")
        request_mock.assert_requested(
            "post", "/api/v1/customers/%s/sources" % TEST_RESOURCE_ID
        )

    def test_is_retrievable(self, request_mock):
        paayes.Customer.retrieve_source(TEST_RESOURCE_ID, TEST_SOURCE_ID)
        request_mock.assert_requested(
            "get",
            "/api/v1/customers/%s/sources/%s" % (TEST_RESOURCE_ID, TEST_SOURCE_ID),
        )

    def test_is_modifiable(self, request_mock):
        paayes.Customer.modify_source(
            TEST_RESOURCE_ID, TEST_SOURCE_ID, metadata={"foo": "bar"}
        )
        request_mock.assert_requested(
            "post",
            "/api/v1/customers/%s/sources/%s" % (TEST_RESOURCE_ID, TEST_SOURCE_ID),
        )

    def test_is_deletable(self, request_mock):
        paayes.Customer.delete_source(TEST_RESOURCE_ID, TEST_SOURCE_ID)
        request_mock.assert_requested(
            "delete",
            "/api/v1/customers/%s/sources/%s" % (TEST_RESOURCE_ID, TEST_SOURCE_ID),
        )

    def test_is_listable(self, request_mock):
        resources = paayes.Customer.list_sources(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/customers/%s/sources" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)


class TestCustomerTaxIds(object):
    def test_is_creatable(self, request_mock):
        resource = paayes.Customer.create_tax_id(
            TEST_RESOURCE_ID, type="eu_vat", value="11111"
        )
        request_mock.assert_requested(
            "post", "/api/v1/customers/%s/tax_ids" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.TaxId)

    def test_is_retrievable(self, request_mock):
        paayes.Customer.retrieve_tax_id(TEST_RESOURCE_ID, TEST_TAX_ID_ID)
        request_mock.assert_requested(
            "get",
            "/api/v1/customers/%s/tax_ids/%s" % (TEST_RESOURCE_ID, TEST_TAX_ID_ID),
        )

    def test_is_deletable(self, request_mock):
        paayes.Customer.delete_tax_id(TEST_RESOURCE_ID, TEST_TAX_ID_ID)
        request_mock.assert_requested(
            "delete",
            "/api/v1/customers/%s/tax_ids/%s" % (TEST_RESOURCE_ID, TEST_TAX_ID_ID),
        )

    def test_is_listable(self, request_mock):
        resources = paayes.Customer.list_tax_ids(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/customers/%s/tax_ids" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)


class TestCustomerTransactions(object):
    def test_is_creatable(self, request_mock):
        resource = paayes.Customer.create_balance_transaction(
            TEST_RESOURCE_ID, amount=1234, currency="usd"
        )
        request_mock.assert_requested(
            "post", "/api/v1/customers/%s/balance_transactions" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.CustomerBalanceTransaction)

    def test_is_retrievable(self, request_mock):
        paayes.Customer.retrieve_balance_transaction(
            TEST_RESOURCE_ID, TEST_TRANSACTION_ID
        )
        request_mock.assert_requested(
            "get",
            "/api/v1/customers/%s/balance_transactions/%s"
            % (TEST_RESOURCE_ID, TEST_TRANSACTION_ID),
        )

    def test_is_listable(self, request_mock):
        resources = paayes.Customer.list_balance_transactions(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/customers/%s/balance_transactions" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
