from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "dp_123"


class TestDispute(object):
    def test_is_listable(self, request_mock):
        resources = paayes.Dispute.list()
        request_mock.assert_requested("get", "/api/v1/disputes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.Dispute)

    def test_is_retrievable(self, request_mock):
        resource = paayes.Dispute.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/disputes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Dispute)

    def test_is_saveable(self, request_mock):
        resource = paayes.Dispute.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/api/v1/disputes/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = paayes.Dispute.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/api/v1/disputes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Dispute)

    def test_can_close(self, request_mock):
        resource = paayes.Dispute.retrieve(TEST_RESOURCE_ID)
        resource.close()
        request_mock.assert_requested(
            "post", "/api/v1/disputes/%s/close" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Dispute)

    def test_can_close_classmethod(self, request_mock):
        resource = paayes.Dispute.close(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/api/v1/disputes/%s/close" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Dispute)
