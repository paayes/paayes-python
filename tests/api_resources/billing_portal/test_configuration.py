from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "bpc_123"


class TestConfiguration(object):
    def test_is_creatable(self, request_mock):
        resource = paayes.billing_portal.Configuration.create(
            business_profile={
                "privacy_policy_url": "https://example.com/privacy",
                "terms_of_service_url": "https://example.com/tos",
            },
            features={
                "customer_update": {
                    "allowed_updates": ["address"],
                    "enabled": True,
                }
            },
        )
        request_mock.assert_requested(
            "post", "/api/v1/billing_portal/configurations"
        )
        assert isinstance(resource, paayes.billing_portal.Configuration)

    def test_is_retrievable(self, request_mock):
        resource = paayes.billing_portal.Configuration.retrieve(
            TEST_RESOURCE_ID
        )
        request_mock.assert_requested(
            "get", "/api/v1/billing_portal/configurations/%s" % (TEST_RESOURCE_ID)
        )
        assert isinstance(resource, paayes.billing_portal.Configuration)

    def test_is_modifiable(self, request_mock):
        resource = paayes.billing_portal.Configuration.modify(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/api/v1/billing_portal/configurations/%s" % (TEST_RESOURCE_ID)
        )
        assert isinstance(resource, paayes.billing_portal.Configuration)

    def test_is_listable(self, request_mock):
        resource = paayes.billing_portal.Configuration.list()
        request_mock.assert_requested(
            "get", "/api/v1/billing_portal/configurations"
        )
        assert isinstance(
            resource.data[0], paayes.billing_portal.Configuration
        )
