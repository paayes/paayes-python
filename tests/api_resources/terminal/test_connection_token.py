from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "rdr_123"


class TestConnectionToken(object):
    def test_is_creatable(self, request_mock):
        resource = paayes.terminal.ConnectionToken.create()
        request_mock.assert_requested("post", "/api/v1/terminal/connection_tokens")
        assert isinstance(resource, paayes.terminal.ConnectionToken)
