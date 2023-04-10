from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "cs_123"


class TestSession(object):
    def test_is_creatable(self, request_mock):
        resource = paayes.checkout.Session.create(
            cancel_url="https://paayes.com/cancel",
            client_reference_id="1234",
            line_items=[
                {
                    "amount": 123,
                    "currency": "usd",
                    "description": "item 1",
                    "images": ["https://paayes.com/img1"],
                    "name": "name",
                    "quantity": 2,
                }
            ],
            payment_intent_data={"receipt_email": "test@paayes.com"},
            payment_method_types=["card"],
            success_url="https://paayes.com/success",
        )
        request_mock.assert_requested("post", "/api/v1/checkout/sessions")
        assert isinstance(resource, paayes.checkout.Session)

    def test_is_retrievable(self, request_mock):
        resource = paayes.checkout.Session.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/checkout/sessions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.checkout.Session)


class TestSessionLineItems(object):
    def test_is_listable(self, request_mock):
        resources = paayes.checkout.Session.list_line_items(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/checkout/sessions/%s/line_items" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.LineItem)
