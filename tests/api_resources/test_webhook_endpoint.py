from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "we_123"


class TestWebhookEndpoint(object):
    def test_is_listable(self, request_mock):
        resources = paayes.WebhookEndpoint.list()
        request_mock.assert_requested("get", "/api/v1/webhook_endpoints")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.WebhookEndpoint)

    def test_is_retrievable(self, request_mock):
        resource = paayes.WebhookEndpoint.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/webhook_endpoints/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.WebhookEndpoint)

    def test_is_creatable(self, request_mock):
        resource = paayes.WebhookEndpoint.create(
            enabled_events=["charge.succeeded"], url="https://paayes.com"
        )
        request_mock.assert_requested("post", "/api/v1/webhook_endpoints")
        assert isinstance(resource, paayes.WebhookEndpoint)

    def test_is_saveable(self, request_mock):
        resource = paayes.WebhookEndpoint.retrieve(TEST_RESOURCE_ID)
        resource.enabled_events = ["charge.succeeded"]
        resource.save()
        request_mock.assert_requested(
            "post", "/api/v1/webhook_endpoints/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = paayes.WebhookEndpoint.modify(
            TEST_RESOURCE_ID,
            enabled_events=["charge.succeeded"],
            url="https://paayes.com",
        )
        request_mock.assert_requested(
            "post", "/api/v1/webhook_endpoints/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.WebhookEndpoint)

    def test_is_deletable(self, request_mock):
        resource = paayes.WebhookEndpoint.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/api/v1/webhook_endpoints/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, request_mock):
        resource = paayes.WebhookEndpoint.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/api/v1/webhook_endpoints/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
