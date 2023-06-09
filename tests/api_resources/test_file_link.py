from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "link_123"


class TestFileLink(object):
    def test_is_listable(self, request_mock):
        resources = paayes.FileLink.list()
        request_mock.assert_requested("get", "/api/v1/file_links")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.FileLink)

    def test_is_retrievable(self, request_mock):
        resource = paayes.FileLink.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/file_links/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.FileLink)

    def test_is_creatable(self, request_mock):
        resource = paayes.FileLink.create(file="file_123")
        request_mock.assert_requested("post", "/api/v1/file_links")
        assert isinstance(resource, paayes.FileLink)

    def test_is_saveable(self, request_mock):
        resource = paayes.FileLink.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/api/v1/file_links/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = paayes.FileLink.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/api/v1/file_links/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.FileLink)
