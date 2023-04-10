from __future__ import absolute_import, division, print_function

import paayes


class TestSetupAttempt(object):
    def test_is_listable(self, request_mock):
        resources = paayes.SetupAttempt.list(setup_intent="seti_123")
        request_mock.assert_requested("get", "/api/v1/setup_attempts")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.SetupAttempt)
