from __future__ import absolute_import, division, print_function

import paayes
import pytest


TEST_RESOURCE_ID = "qt_123"


class TestQuote(object):
    @pytest.fixture(scope="function")
    def setup_upload_api_base(self):
        paayes.upload_api_base = paayes.api_base
        yield
        paayes.api_base = paayes.upload_api_base
        paayes.upload_api_base = "https://files.paayes.com"

    def test_is_listable(self, request_mock):
        resources = paayes.Quote.list()
        request_mock.assert_requested("get", "/api/v1/quotes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.Quote)

    def test_is_retrievable(self, request_mock):
        resource = paayes.Quote.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/quotes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Quote)

    def test_is_creatable(self, request_mock):
        resource = paayes.Quote.create(customer="cus_123")
        request_mock.assert_requested("post", "/api/v1/quotes")
        assert isinstance(resource, paayes.Quote)

    def test_is_saveable(self, request_mock):
        resource = paayes.Quote.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/api/v1/quotes/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = paayes.Quote.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/api/v1/quotes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Quote)

    def test_can_finalize_quote(self, request_mock):
        resource = paayes.Quote.retrieve(TEST_RESOURCE_ID)
        resource = resource.finalize_quote()
        request_mock.assert_requested(
            "post", "/api/v1/quotes/%s/finalize" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Quote)

    def test_can_finalize_quote_classmethod(self, request_mock):
        resource = paayes.Quote.finalize_quote(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/api/v1/quotes/%s/finalize" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Quote)

    def test_can_cancel(self, request_mock):
        resource = paayes.Quote.retrieve(TEST_RESOURCE_ID)
        resource = resource.cancel()
        request_mock.assert_requested(
            "post", "/api/v1/quotes/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Quote)

    def test_can_cancel_classmethod(self, request_mock):
        resource = paayes.Quote.cancel(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/api/v1/quotes/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Quote)

    def test_can_accept(self, request_mock):
        resource = paayes.Quote.retrieve(TEST_RESOURCE_ID)
        resource = resource.accept()
        request_mock.assert_requested(
            "post", "/api/v1/quotes/%s/accept" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Quote)

    def test_can_accept_classmethod(self, request_mock):
        resource = paayes.Quote.accept(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/api/v1/quotes/%s/accept" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.Quote)

    def test_can_list_line_items(self, request_mock):
        resources = paayes.Quote.list_line_items(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/quotes/%s/line_items" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.LineItem)

    def test_can_list_line_items_classmethod(self, request_mock):
        resources = paayes.Quote.list_line_items(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/quotes/%s/line_items" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.LineItem)

    def test_can_list_computed_upfront_line_items(self, request_mock):
        resources = paayes.Quote.list_computed_upfront_line_items(
            TEST_RESOURCE_ID
        )
        request_mock.assert_requested(
            "get",
            "/api/v1/quotes/%s/computed_upfront_line_items" % TEST_RESOURCE_ID,
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.LineItem)

    def test_can_list_computed_upfront_line_items_classmethod(
        self, request_mock
    ):
        resources = paayes.Quote.list_computed_upfront_line_items(
            TEST_RESOURCE_ID
        )
        request_mock.assert_requested(
            "get",
            "/api/v1/quotes/%s/computed_upfront_line_items" % TEST_RESOURCE_ID,
        )
        assert isinstance(resources.data[0], paayes.LineItem)

    def test_can_pdf(self, setup_upload_api_base, request_mock):
        resource = paayes.Quote.retrieve(TEST_RESOURCE_ID)
        stream, _ = resource.pdf()
        request_mock.assert_api_base(paayes.upload_api_base)
        request_mock.assert_requested_stream(
            "get", "/api/v1/quotes/%s/pdf" % TEST_RESOURCE_ID
        )
        content = stream.io.read()
        assert content == b"Paayes binary response"

    def test_can_pdf_classmethod(self, setup_upload_api_base, request_mock):
        stream = paayes.Quote.pdf(TEST_RESOURCE_ID)
        request_mock.assert_api_base(paayes.upload_api_base)
        request_mock.assert_requested_stream(
            "get", "/api/v1/quotes/%s/pdf" % TEST_RESOURCE_ID
        )
        content = stream.io.read()
        assert content == b"Paayes binary response"
