from __future__ import absolute_import, division, print_function

import paayes


class TestCreateableAPIResource(object):
    class MyCreatable(paayes.api_resources.abstract.CreateableAPIResource):
        OBJECT_NAME = "mycreatable"

    def test_create(self, request_mock):
        request_mock.stub_request(
            "post",
            "/api/v1/mycreatables",
            {"object": "charge", "foo": "bar"},
            rheaders={"request-id": "req_id"},
        )

        res = self.MyCreatable.create()

        request_mock.assert_requested("post", "/api/v1/mycreatables", {})
        assert isinstance(res, paayes.Charge)
        assert res.foo == "bar"

        assert res.last_response is not None
        assert res.last_response.request_id == "req_id"

    def test_idempotent_create(self, request_mock):
        request_mock.stub_request(
            "post",
            "/api/v1/mycreatables",
            {"object": "charge", "foo": "bar"},
            rheaders={"idempotency-key": "foo"},
        )

        res = self.MyCreatable.create(idempotency_key="foo")

        request_mock.assert_requested(
            "post", "/api/v1/mycreatables", {}, {"Idempotency-Key": "foo"}
        )
        assert isinstance(res, paayes.Charge)
        assert res.foo == "bar"
