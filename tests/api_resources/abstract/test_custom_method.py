from __future__ import absolute_import, division, print_function

import paayes
from paayes import util


class TestCustomMethod(object):
    @paayes.api_resources.abstract.custom_method(
        "do_stuff", http_verb="post", http_path="do_the_thing"
    )
    @paayes.api_resources.abstract.custom_method(
        "do_stream_stuff",
        http_verb="post",
        http_path="do_the_stream_thing",
        is_streaming=True,
    )
    class MyResource(paayes.api_resources.abstract.APIResource):
        OBJECT_NAME = "myresource"

        def do_stuff(self, idempotency_key=None, **params):
            url = self.instance_url() + "/do_the_thing"
            headers = util.populate_headers(idempotency_key)
            self.refresh_from(self.request("post", url, params, headers))
            return self

        def do_stream_stuff(self, idempotency_key=None, **params):
            url = self.instance_url() + "/do_the_stream_thing"
            headers = util.populate_headers(idempotency_key)
            return self.request_stream("post", url, params, headers)

    def test_call_custom_method_class(self, request_mock):
        request_mock.stub_request(
            "post",
            "/api/v1/myresources/mid/do_the_thing",
            {"id": "mid", "thing_done": True},
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyResource.do_stuff("mid", foo="bar")

        request_mock.assert_requested(
            "post", "/api/v1/myresources/mid/do_the_thing", {"foo": "bar"}
        )
        assert obj.thing_done is True

    def test_call_custom_stream_method_class(self, request_mock):
        request_mock.stub_request_stream(
            "post",
            "/api/v1/myresources/mid/do_the_stream_thing",
            "response body",
            rheaders={"request-id": "req_id"},
        )

        resp = self.MyResource.do_stream_stuff("mid", foo="bar")

        request_mock.assert_requested_stream(
            "post", "/api/v1/myresources/mid/do_the_stream_thing", {"foo": "bar"}
        )

        body_content = resp.io.read()
        if hasattr(body_content, "decode"):
            body_content = body_content.decode("utf-8")

        assert body_content == "response body"

    def test_call_custom_method_class_with_object(self, request_mock):
        request_mock.stub_request(
            "post",
            "/api/v1/myresources/mid/do_the_thing",
            {"id": "mid", "thing_done": True},
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyResource.construct_from({"id": "mid"}, "mykey")
        self.MyResource.do_stuff(obj, foo="bar")

        request_mock.assert_requested(
            "post", "/api/v1/myresources/mid/do_the_thing", {"foo": "bar"}
        )
        assert obj.thing_done is True

    def test_call_custom_stream_method_class_with_object(self, request_mock):
        request_mock.stub_request_stream(
            "post",
            "/api/v1/myresources/mid/do_the_stream_thing",
            "response body",
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyResource.construct_from({"id": "mid"}, "mykey")
        resp = self.MyResource.do_stream_stuff(obj, foo="bar")

        request_mock.assert_requested_stream(
            "post", "/api/v1/myresources/mid/do_the_stream_thing", {"foo": "bar"}
        )

        body_content = resp.io.read()
        if hasattr(body_content, "decode"):
            body_content = body_content.decode("utf-8")

        assert body_content == "response body"

    def test_call_custom_method_instance(self, request_mock):
        request_mock.stub_request(
            "post",
            "/api/v1/myresources/mid/do_the_thing",
            {"id": "mid", "thing_done": True},
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyResource.construct_from({"id": "mid"}, "mykey")
        obj.do_stuff(foo="bar")

        request_mock.assert_requested(
            "post", "/api/v1/myresources/mid/do_the_thing", {"foo": "bar"}
        )
        assert obj.thing_done is True

    def test_call_custom_stream_method_instance(self, request_mock):
        request_mock.stub_request_stream(
            "post",
            "/api/v1/myresources/mid/do_the_stream_thing",
            "response body",
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyResource.construct_from({"id": "mid"}, "mykey")
        resp = obj.do_stream_stuff(foo="bar")

        request_mock.assert_requested_stream(
            "post", "/api/v1/myresources/mid/do_the_stream_thing", {"foo": "bar"}
        )

        body_content = resp.io.read()
        if hasattr(body_content, "decode"):
            body_content = body_content.decode("utf-8")

        assert body_content == "response body"
