from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "ic_123"


class TestCard(object):
    def test_is_creatable(self, request_mock):
        resource = paayes.issuing.Card.create(currency="usd", type="physical")
        request_mock.assert_requested("post", "/api/v1/issuing/cards")
        assert isinstance(resource, paayes.issuing.Card)

    def test_is_listable(self, request_mock):
        resources = paayes.issuing.Card.list()
        request_mock.assert_requested("get", "/api/v1/issuing/cards")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.issuing.Card)

    def test_is_modifiable(self, request_mock):
        resource = paayes.issuing.Card.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/api/v1/issuing/cards/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.issuing.Card)

    def test_is_retrievable(self, request_mock):
        resource = paayes.issuing.Card.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/issuing/cards/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.issuing.Card)

    def test_is_saveable(self, request_mock):
        resource = paayes.issuing.Card.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        card = resource.save()
        request_mock.assert_requested(
            "post", "/api/v1/issuing/cards/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.issuing.Card)
        assert resource is card

    def test_can_retrieve_details(self, request_mock):
        # paayes-mock does not handle this anymore so we stub instead.
        request_mock.stub_request(
            "get",
            "/api/v1/issuing/cards/%s/details" % TEST_RESOURCE_ID,
            {"object": "issuing.card_details"},
        )
        card = paayes.issuing.Card.construct_from(
            {"id": "%s" % TEST_RESOURCE_ID, "object": "issuing.card"},
            paayes.api_key,
        )
        card_details = card.details()
        request_mock.assert_requested(
            "get", "/api/v1/issuing/cards/%s/details" % TEST_RESOURCE_ID
        )
        assert isinstance(card_details, paayes.issuing.CardDetails)

    def test_can_retrieve_details_classmethod(self, request_mock):
        # paayes-mock does not handle this anymore so we stub instead.
        request_mock.stub_request(
            "get",
            "/api/v1/issuing/cards/%s/details" % TEST_RESOURCE_ID,
            {"object": "issuing.card_details"},
        )

        card_details = paayes.issuing.Card.details(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/issuing/cards/%s/details" % TEST_RESOURCE_ID
        )
        assert isinstance(card_details, paayes.issuing.CardDetails)
