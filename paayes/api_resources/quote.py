from __future__ import absolute_import, division, print_function

import paayes
from paayes import api_requestor
from paayes import util
from paayes.api_resources.abstract import CreateableAPIResource
from paayes.api_resources.abstract import ListableAPIResource
from paayes.api_resources.abstract import UpdateableAPIResource
from paayes.api_resources.abstract import custom_method
from paayes.six.moves.urllib.parse import quote_plus


@custom_method("accept", http_verb="post")
@custom_method("cancel", http_verb="post")
@custom_method("finalize_quote", http_verb="post", http_path="finalize")
@custom_method(
    "list_computed_upfront_line_items",
    http_verb="get",
    http_path="computed_upfront_line_items",
)
@custom_method("list_line_items", http_verb="get", http_path="line_items")
class Quote(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "quote"

    def accept(self, idempotency_key=None, **params):
        url = self.instance_url() + "/accept"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def cancel(self, idempotency_key=None, **params):
        url = self.instance_url() + "/cancel"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def finalize_quote(self, idempotency_key=None, **params):
        url = self.instance_url() + "/finalize"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def list_computed_upfront_line_items(self, idempotency_key=None, **params):
        url = self.instance_url() + "/computed_upfront_line_items"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("get", url, params, headers))
        return self

    def list_line_items(self, idempotency_key=None, **params):
        url = self.instance_url() + "/line_items"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("get", url, params, headers))
        return self

    @classmethod
    def _cls_pdf(
        cls,
        sid,
        api_key=None,
        idempotency_key=None,
        paayes_version=None,
        paayes_account=None,
        **params
    ):
        url = "%s/%s/%s" % (
            cls.class_url(),
            quote_plus(util.utf8(sid)),
            "pdf",
        )
        requestor = api_requestor.APIRequestor(
            api_key,
            api_base=paayes.upload_api_base,
            api_version=paayes_version,
            account=paayes_account,
        )
        headers = util.populate_headers(idempotency_key)
        response, _ = requestor.request_stream("get", url, params, headers)
        return response

    @util.class_method_variant("_cls_pdf")
    def pdf(
        self,
        api_key=None,
        api_version=None,
        paayes_version=None,
        paayes_account=None,
        **params
    ):
        version = api_version or paayes_version
        requestor = api_requestor.APIRequestor(
            api_key,
            api_base=paayes.upload_api_base,
            api_version=version,
            account=paayes_account,
        )
        url = self.instance_url() + "/pdf"
        return requestor.request_stream("get", url, params=params)
