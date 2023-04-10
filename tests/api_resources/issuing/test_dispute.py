from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "idp_123"


class TestDispute(object):
    def test_is_creatable(self, request_mock):
        resource = paayes.issuing.Dispute.create(transaction="ipi_123")
        request_mock.assert_requested("post", "/api/v1/issuing/disputes")
        assert isinstance(resource, paayes.issuing.Dispute)

    def test_is_listable(self, request_mock):
        resources = paayes.issuing.Dispute.list()
        request_mock.assert_requested("get", "/api/v1/issuing/disputes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.issuing.Dispute)

    def test_is_modifiable(self, request_mock):
        resource = paayes.issuing.Dispute.modify(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/api/v1/issuing/disputes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.issuing.Dispute)

    def test_is_retrievable(self, request_mock):
        resource = paayes.issuing.Dispute.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/issuing/disputes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.issuing.Dispute)

    def test_is_submittable(self, request_mock):
        resource = paayes.issuing.Dispute.submit(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/api/v1/issuing/disputes/%s/submit" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.issuing.Dispute)
