from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "apwc_123"


class TestApplePayDomain(object):
    def test_is_listable(self, request_mock):
        resources = paayes.ApplePayDomain.list()
        request_mock.assert_requested("get", "/api/v1/apple_pay/domains")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.ApplePayDomain)

    def test_is_retrievable(self, request_mock):
        resource = paayes.ApplePayDomain.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/apple_pay/domains/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.ApplePayDomain)

    def test_is_creatable(self, request_mock):
        resource = paayes.ApplePayDomain.create(domain_name="test.com")
        request_mock.assert_requested("post", "/api/v1/apple_pay/domains")
        assert isinstance(resource, paayes.ApplePayDomain)

    def test_is_deletable(self, request_mock):
        resource = paayes.ApplePayDomain.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/api/v1/apple_pay/domains/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, request_mock):
        resource = paayes.ApplePayDomain.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/api/v1/apple_pay/domains/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
