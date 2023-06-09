from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "rdr_123"


class TestReader(object):
    def test_is_creatable(self, request_mock):
        resource = paayes.terminal.Reader.create(
            registration_code="a-b-c", label="name"
        )
        request_mock.assert_requested("post", "/api/v1/terminal/readers")
        assert isinstance(resource, paayes.terminal.Reader)

    def test_is_listable(self, request_mock):
        resources = paayes.terminal.Reader.list()
        request_mock.assert_requested("get", "/api/v1/terminal/readers")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.terminal.Reader)

    def test_is_modifiable(self, request_mock):
        resource = paayes.terminal.Reader.modify(
            TEST_RESOURCE_ID, label="new-name"
        )
        request_mock.assert_requested(
            "post", "/api/v1/terminal/readers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.terminal.Reader)

    def test_is_retrievable(self, request_mock):
        resource = paayes.terminal.Reader.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/terminal/readers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.terminal.Reader)

    def test_is_saveable(self, request_mock):
        resource = paayes.terminal.Reader.retrieve(TEST_RESOURCE_ID)
        resource.label = "new-name"
        reader = resource.save()
        request_mock.assert_requested(
            "post", "/api/v1/terminal/readers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.terminal.Reader)
        assert resource is reader

    def test_is_deletable(self, request_mock):
        resource = paayes.terminal.Reader.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/api/v1/terminal/readers/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, request_mock):
        resource = paayes.terminal.Reader.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/api/v1/terminal/readers/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
