from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "vs_123"


class TestVerificationSession(object):
    def test_is_creatable(self, request_mock):
        resource = paayes.identity.VerificationSession.create(type="id_number")
        request_mock.assert_requested(
            "post", "/api/v1/identity/verification_sessions"
        )
        assert isinstance(resource, paayes.identity.VerificationSession)

    def test_is_listable(self, request_mock):
        resources = paayes.identity.VerificationSession.list()
        request_mock.assert_requested(
            "get", "/api/v1/identity/verification_sessions"
        )
        assert isinstance(resources.data, list)
        assert isinstance(
            resources.data[0], paayes.identity.VerificationSession
        )

    def test_is_modifiable(self, request_mock):
        resource = paayes.identity.VerificationSession.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/api/v1/identity/verification_sessions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.identity.VerificationSession)

    def test_is_retrievable(self, request_mock):
        resource = paayes.identity.VerificationSession.retrieve(
            TEST_RESOURCE_ID
        )
        request_mock.assert_requested(
            "get", "/api/v1/identity/verification_sessions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.identity.VerificationSession)

    def test_is_saveable(self, request_mock):
        resource = paayes.identity.VerificationSession.retrieve(
            TEST_RESOURCE_ID
        )
        resource.metadata["key"] = "value"
        verification_session = resource.save()
        request_mock.assert_requested(
            "post", "/api/v1/identity/verification_sessions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.identity.VerificationSession)
        assert resource is verification_session

    def test_can_cancel(self, request_mock):
        resource = paayes.identity.VerificationSession.retrieve(
            TEST_RESOURCE_ID
        )
        verification_session = resource.cancel()
        request_mock.assert_requested(
            "post",
            "/api/v1/identity/verification_sessions/%s/cancel" % TEST_RESOURCE_ID,
        )
        assert isinstance(resource, paayes.identity.VerificationSession)
        assert resource is verification_session

    def test_can_cancel_classmethod(self, request_mock):
        resource = paayes.identity.VerificationSession.cancel(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post",
            "/api/v1/identity/verification_sessions/%s/cancel" % TEST_RESOURCE_ID,
        )
        assert isinstance(resource, paayes.identity.VerificationSession)

    def test_can_redact(self, request_mock):
        resource = paayes.identity.VerificationSession.retrieve(
            TEST_RESOURCE_ID
        )
        verification_session = resource.redact()
        request_mock.assert_requested(
            "post",
            "/api/v1/identity/verification_sessions/%s/redact" % TEST_RESOURCE_ID,
        )
        assert isinstance(resource, paayes.identity.VerificationSession)
        assert resource is verification_session

    def test_can_redact_classmethod(self, request_mock):
        resource = paayes.identity.VerificationSession.redact(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post",
            "/api/v1/identity/verification_sessions/%s/redact" % TEST_RESOURCE_ID,
        )
        assert isinstance(resource, paayes.identity.VerificationSession)
