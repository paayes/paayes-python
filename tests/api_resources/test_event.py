from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "evt_123"


class TestEvent(object):
    def test_is_listable(self, request_mock):
        resources = paayes.Event.list()
        request_mock.assert_requested("get", "/api/v1/events")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.Event)

    def test_is_retrievable(self, request_mock):
        resource = paayes.Event.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/events/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Event)
