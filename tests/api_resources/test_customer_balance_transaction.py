from __future__ import absolute_import, division, print_function

import pytest

import paayes


TEST_RESOURCE_ID = "cbtxn_123"


class TestCustomerBalanceTransaction(object):
    def construct_resource(self):
        tax_id_dict = {
            "id": TEST_RESOURCE_ID,
            "object": "customer_balance_transaction",
            "customer": "cus_123",
        }
        return paayes.CustomerBalanceTransaction.construct_from(
            tax_id_dict, paayes.api_key
        )

    def test_has_instance_url(self, request_mock):
        resource = self.construct_resource()
        assert (
            resource.instance_url()
            == "/api/v1/customers/cus_123/balance_transactions/%s"
            % TEST_RESOURCE_ID
        )

    def test_is_not_retrievable(self, request_mock):
        with pytest.raises(NotImplementedError):
            paayes.CustomerBalanceTransaction.retrieve(TEST_RESOURCE_ID)
