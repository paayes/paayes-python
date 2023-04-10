from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "pts_123"


class TestSession(object):
    def test_is_creatable(self, request_mock):
        resource = paayes.billing_portal.Session.create(
            customer="cus_123", return_url="https://paayes.com/return"
        )
        request_mock.assert_requested("post", "/api/v1/billing_portal/sessions")
        assert isinstance(resource, paayes.billing_portal.Session)
