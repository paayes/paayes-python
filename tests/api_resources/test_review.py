from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "prv_123"


class TestReview(object):
    def test_is_listable(self, request_mock):
        resources = paayes.Review.list()
        request_mock.assert_requested("get", "/api/v1/reviews")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.Review)

    def test_is_retrievable(self, request_mock):
        resource = paayes.Review.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/reviews/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Review)

    def test_can_approve(self, request_mock):
        resource = paayes.Review.retrieve(TEST_RESOURCE_ID)
        resource.approve()
        request_mock.assert_requested(
            "post", "/api/v1/reviews/%s/approve" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Review)

    def test_can_approve_classmethod(self, request_mock):
        resource = paayes.Review.approve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/api/v1/reviews/%s/approve" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Review)
