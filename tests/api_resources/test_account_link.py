from __future__ import absolute_import, division, print_function

import paayes


class TestAccountLink(object):
    def test_is_creatable(self, request_mock):
        resource = paayes.AccountLink.create(
            account="acct_123",
            refresh_url="https://paayes.com/failure",
            return_url="https://paayes.com/success",
            type="account_onboarding",
        )
        request_mock.assert_requested("post", "/api/v1/account_links")
        assert isinstance(resource, paayes.AccountLink)
