from __future__ import absolute_import, division, print_function

import paayes


class TestBalance(object):
    def test_is_retrievable(self, request_mock):
        resource = paayes.Balance.retrieve()
        request_mock.assert_requested("get", "/api/v1/balance")
        assert isinstance(resource, paayes.Balance)
