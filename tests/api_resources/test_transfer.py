from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "tr_123"
TEST_REVERSAL_ID = "trr_123"


class TestTransfer(object):
    def test_is_listable(self, request_mock):
        resources = paayes.Transfer.list()
        request_mock.assert_requested("get", "/api/v1/transfers")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.Transfer)

    def test_is_retrievable(self, request_mock):
        resource = paayes.Transfer.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/transfers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Transfer)

    def test_is_creatable(self, request_mock):
        resource = paayes.Transfer.create(
            amount=100, currency="usd", destination="acct_123"
        )
        request_mock.assert_requested("post", "/api/v1/transfers")
        assert isinstance(resource, paayes.Transfer)

    def test_is_saveable(self, request_mock):
        resource = paayes.Transfer.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/api/v1/transfers/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = paayes.Transfer.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/api/v1/transfers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Transfer)

    def test_can_cancel(self, request_mock):
        # paayes-mock does not handle this anymore as it was on an old
        # API version so we stub instead.
        request_mock.stub_request(
            "post",
            "/api/v1/transfers/%s/cancel" % TEST_RESOURCE_ID,
            {
                "id": "%s" % TEST_RESOURCE_ID,
                "object": "transfer",
                "status": "canceled",
            },
        )
        transfer = paayes.Transfer.construct_from(
            {"id": "%s" % TEST_RESOURCE_ID, "object": "transfer"},
            paayes.api_key,
        )
        transfer_canceled = transfer.cancel()
        request_mock.assert_requested(
            "post", "/api/v1/transfers/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(transfer_canceled, paayes.Transfer)

    def test_can_cancel_classmethod(self, request_mock):
        # paayes-mock does not handle this anymore as it was on an old
        # API version so we stub instead.
        request_mock.stub_request(
            "post",
            "/api/v1/transfers/%s/cancel" % TEST_RESOURCE_ID,
            {"id": "%s" % TEST_RESOURCE_ID, "object": "transfer"},
        )
        transfer = paayes.Transfer.cancel(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/api/v1/transfers/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(transfer, paayes.Transfer)


class TestTransferReversals:
    def test_is_listable(self, request_mock):
        resources = paayes.Transfer.list_reversals(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/transfers/%s/reversals" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.Reversal)

    def test_is_retrievable(self, request_mock):
        resource = paayes.Transfer.retrieve_reversal(
            TEST_RESOURCE_ID, TEST_REVERSAL_ID
        )
        request_mock.assert_requested(
            "get",
            "/api/v1/transfers/%s/reversals/%s"
            % (TEST_RESOURCE_ID, TEST_REVERSAL_ID),
        )
        assert isinstance(resource, paayes.Reversal)

    def test_is_creatable(self, request_mock):
        resource = paayes.Transfer.create_reversal(
            TEST_RESOURCE_ID, amount=100
        )
        request_mock.assert_requested(
            "post", "/api/v1/transfers/%s/reversals" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Reversal)

    def test_is_modifiable(self, request_mock):
        resource = paayes.Transfer.modify_reversal(
            TEST_RESOURCE_ID, TEST_REVERSAL_ID, metadata={"foo": "bar"}
        )
        request_mock.assert_requested(
            "post",
            "/api/v1/transfers/%s/reversals/%s"
            % (TEST_RESOURCE_ID, TEST_REVERSAL_ID),
        )
        assert isinstance(resource, paayes.Reversal)
