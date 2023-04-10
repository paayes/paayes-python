from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "seti_123"


class TestSetupIntent(object):
    def test_is_listable(self, request_mock):
        resources = paayes.SetupIntent.list()
        request_mock.assert_requested("get", "/api/v1/setup_intents")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.SetupIntent)

    def test_is_retrievable(self, request_mock):
        resource = paayes.SetupIntent.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/setup_intents/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.SetupIntent)

    def test_is_creatable(self, request_mock):
        resource = paayes.SetupIntent.create(payment_method_types=["card"])
        request_mock.assert_requested("post", "/api/v1/setup_intents")
        assert isinstance(resource, paayes.SetupIntent)

    def test_is_modifiable(self, request_mock):
        resource = paayes.SetupIntent.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post",
            "/api/v1/setup_intents/%s" % TEST_RESOURCE_ID,
            {"metadata": {"key": "value"}},
        )
        assert isinstance(resource, paayes.SetupIntent)

    def test_is_saveable(self, request_mock):
        resource = paayes.SetupIntent.retrieve(TEST_RESOURCE_ID)

        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post",
            "/api/v1/setup_intents/%s" % TEST_RESOURCE_ID,
            {"metadata": {"key": "value"}},
        )
        assert isinstance(resource, paayes.SetupIntent)

    def test_can_cancel(self, request_mock):
        resource = paayes.SetupIntent.retrieve(TEST_RESOURCE_ID)
        resource.cancel()
        request_mock.assert_requested(
            "post", "/api/v1/setup_intents/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.SetupIntent)

    def test_can_cancel_classmethod(self, request_mock):
        resource = paayes.SetupIntent.cancel(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/api/v1/setup_intents/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.SetupIntent)

    def test_can_confirm(self, request_mock):
        resource = paayes.SetupIntent.retrieve(TEST_RESOURCE_ID)
        resource.confirm()
        request_mock.assert_requested(
            "post", "/api/v1/setup_intents/%s/confirm" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.SetupIntent)

    def test_can_confirm_classmethod(self, request_mock):
        resource = paayes.SetupIntent.confirm(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/api/v1/setup_intents/%s/confirm" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.SetupIntent)
