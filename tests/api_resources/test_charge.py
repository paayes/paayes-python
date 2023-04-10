from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "ch_123"


class TestCharge(object):
    def test_is_listable(self, request_mock):
        resources = paayes.Charge.list()
        request_mock.assert_requested("get", "/api/v1/charges")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.Charge)

    def test_is_retrievable(self, request_mock):
        resource = paayes.Charge.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/charges/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Charge)

    def test_is_creatable(self, request_mock):
        resource = paayes.Charge.create(
            amount=100, currency="usd", source="tok_123"
        )
        request_mock.assert_requested("post", "/api/v1/charges")
        assert isinstance(resource, paayes.Charge)

    def test_is_saveable(self, request_mock):
        resource = paayes.Charge.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/api/v1/charges/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = paayes.Charge.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/api/v1/charges/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Charge)

    def test_is_refundable(self, request_mock):
        charge = paayes.Charge.retrieve(TEST_RESOURCE_ID)
        resource = charge.refund()
        request_mock.assert_requested(
            "post", "/api/v1/charges/%s/refund" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Charge)

    def test_can_capture(self, request_mock):
        charge = paayes.Charge.retrieve(TEST_RESOURCE_ID)
        resource = charge.capture()
        request_mock.assert_requested(
            "post", "/api/v1/charges/%s/capture" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Charge)

    def test_can_capture_classmethod(self, request_mock):
        resource = paayes.Charge.capture(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/api/v1/charges/%s/capture" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Charge)

    def test_can_update_dispute(self, request_mock):
        charge = paayes.Charge.retrieve(TEST_RESOURCE_ID)
        resource = charge.update_dispute()
        request_mock.assert_requested(
            "post", "/api/v1/charges/%s/dispute" % charge.id
        )
        assert isinstance(resource, paayes.Dispute)

    def test_can_close_dispute(self, request_mock):
        charge = paayes.Charge.retrieve(TEST_RESOURCE_ID)
        resource = charge.close_dispute()
        request_mock.assert_requested(
            "post", "/api/v1/charges/%s/dispute/close" % charge.id
        )
        assert isinstance(resource, paayes.Dispute)

    def test_can_mark_as_fraudulent(self, request_mock):
        charge = paayes.Charge.retrieve(TEST_RESOURCE_ID)
        resource = charge.mark_as_fraudulent()
        request_mock.assert_requested(
            "post",
            "/api/v1/charges/%s" % charge.id,
            {"fraud_details": {"user_report": "fraudulent"}},
        )
        assert isinstance(resource, paayes.Charge)

    def test_can_mark_as_safe(self, request_mock):
        charge = paayes.Charge.retrieve(TEST_RESOURCE_ID)
        resource = charge.mark_as_safe()
        request_mock.assert_requested(
            "post",
            "/api/v1/charges/%s" % charge.id,
            {"fraud_details": {"user_report": "safe"}},
        )
        assert isinstance(resource, paayes.Charge)
