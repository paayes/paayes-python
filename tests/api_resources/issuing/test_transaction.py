from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "ipi_123"


class TestTransaction(object):
    def test_is_listable(self, request_mock):
        resources = paayes.issuing.Transaction.list()
        request_mock.assert_requested("get", "/api/v1/issuing/transactions")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.issuing.Transaction)

    def test_is_modifiable(self, request_mock):
        resource = paayes.issuing.Transaction.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/api/v1/issuing/transactions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.issuing.Transaction)

    def test_is_retrievable(self, request_mock):
        resource = paayes.issuing.Transaction.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/issuing/transactions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.issuing.Transaction)

    def test_is_saveable(self, request_mock):
        resource = paayes.issuing.Transaction.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        transaction = resource.save()
        request_mock.assert_requested(
            "post", "/api/v1/issuing/transactions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.issuing.Transaction)
        assert resource is transaction
