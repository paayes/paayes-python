from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "tdsrc_123"


class TestThreeDSecure(object):
    def test_is_retrievable(self, request_mock):
        resource = paayes.ThreeDSecure.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/3d_secure/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.ThreeDSecure)

    def test_is_creatable(self, request_mock):
        resource = paayes.ThreeDSecure.create(
            card="tok_123", amount=100, currency="usd", return_url="url"
        )
        request_mock.assert_requested("post", "/api/v1/3d_secure")
        assert isinstance(resource, paayes.ThreeDSecure)
