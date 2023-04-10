from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "mandate_123"


class TestMandateSchedule(object):
    def test_is_retrievable(self, request_mock):
        resource = paayes.Mandate.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/mandates/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Mandate)
