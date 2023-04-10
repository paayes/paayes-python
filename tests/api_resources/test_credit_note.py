from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "cn_123"


class TestCreditNote(object):
    def test_is_listable(self, request_mock):
        resources = paayes.CreditNote.list()
        request_mock.assert_requested("get", "/api/v1/credit_notes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.CreditNote)

    def test_is_retrievable(self, request_mock):
        resource = paayes.CreditNote.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/credit_notes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.CreditNote)

    def test_is_creatable(self, request_mock):
        resource = paayes.CreditNote.create(
            amount=100, invoice="in_123", reason="duplicate"
        )
        request_mock.assert_requested("post", "/api/v1/credit_notes")
        assert isinstance(resource, paayes.CreditNote)

    def test_is_saveable(self, request_mock):
        resource = paayes.CreditNote.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/api/v1/credit_notes/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = paayes.CreditNote.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/api/v1/credit_notes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.CreditNote)

    def test_can_preview(self, request_mock):
        resource = paayes.CreditNote.preview(invoice="in_123", amount=500)
        request_mock.assert_requested("get", "/api/v1/credit_notes/preview")
        assert isinstance(resource, paayes.CreditNote)

    def test_can_void_credit_note(self, request_mock):
        resource = paayes.CreditNote.retrieve(TEST_RESOURCE_ID)
        resource = resource.void_credit_note()
        request_mock.assert_requested(
            "post", "/api/v1/credit_notes/%s/void" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.CreditNote)

    def test_can_void_credit_note_classmethod(self, request_mock):
        resource = paayes.CreditNote.void_credit_note(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/api/v1/credit_notes/%s/void" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.CreditNote)
