from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "ich_123"


class TestCardholder(object):
    def test_is_creatable(self, request_mock):
        resource = paayes.issuing.Cardholder.create(
            billing={
                "address": {
                    "city": "city",
                    "country": "US",
                    "line1": "line1",
                    "postal_code": "postal_code",
                }
            },
            name="Jenny Rosen",
            type="individual",
        )
        request_mock.assert_requested("post", "/api/v1/issuing/cardholders")
        assert isinstance(resource, paayes.issuing.Cardholder)

    def test_is_listable(self, request_mock):
        resources = paayes.issuing.Cardholder.list()
        request_mock.assert_requested("get", "/api/v1/issuing/cardholders")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.issuing.Cardholder)

    def test_is_modifiable(self, request_mock):
        resource = paayes.issuing.Cardholder.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/api/v1/issuing/cardholders/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.issuing.Cardholder)

    def test_is_retrievable(self, request_mock):
        resource = paayes.issuing.Cardholder.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/issuing/cardholders/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.issuing.Cardholder)

    def test_is_saveable(self, request_mock):
        resource = paayes.issuing.Cardholder.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        cardholder = resource.save()
        request_mock.assert_requested(
            "post", "/api/v1/issuing/cardholders/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.issuing.Cardholder)
        assert resource is cardholder
