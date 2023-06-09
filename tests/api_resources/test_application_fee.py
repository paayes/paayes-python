from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "fee_123"
TEST_FEEREFUND_ID = "fr_123"


class TestApplicationFee(object):
    def test_is_listable(self, request_mock):
        resources = paayes.ApplicationFee.list()
        request_mock.assert_requested("get", "/api/v1/application_fees")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.ApplicationFee)

    def test_is_refundable(self, request_mock):
        appfee = paayes.ApplicationFee.retrieve(TEST_RESOURCE_ID)
        resource = appfee.refund()
        request_mock.assert_requested(
            "post", "/api/v1/application_fees/%s/refund" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.ApplicationFee)
        assert resource is appfee


class TestApplicationFeeRefunds(object):
    def test_is_listable(self, request_mock):
        resources = paayes.ApplicationFee.list_refunds(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/application_fees/%s/refunds" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.ApplicationFeeRefund)

    def test_is_retrievable(self, request_mock):
        resource = paayes.ApplicationFee.retrieve_refund(
            TEST_RESOURCE_ID, TEST_FEEREFUND_ID
        )
        request_mock.assert_requested(
            "get",
            "/api/v1/application_fees/%s/refunds/%s"
            % (TEST_RESOURCE_ID, TEST_FEEREFUND_ID),
        )
        assert isinstance(resource, paayes.ApplicationFeeRefund)

    def test_is_creatable(self, request_mock):
        resource = paayes.ApplicationFee.create_refund(
            TEST_RESOURCE_ID, amount=100
        )
        request_mock.assert_requested(
            "post", "/api/v1/application_fees/%s/refunds" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.ApplicationFeeRefund)

    def test_is_modifiable(self, request_mock):
        resource = paayes.ApplicationFee.modify_refund(
            TEST_RESOURCE_ID, TEST_FEEREFUND_ID, metadata={"foo": "bar"}
        )
        request_mock.assert_requested(
            "post",
            "/api/v1/application_fees/%s/refunds/%s"
            % (TEST_RESOURCE_ID, TEST_FEEREFUND_ID),
        )
        assert isinstance(resource, paayes.ApplicationFeeRefund)
