from __future__ import absolute_import, division, print_function

from paayes import api_requestor
from paayes import util
from paayes.api_resources.abstract import CreateableAPIResource
from paayes.api_resources.abstract import ListableAPIResource
from paayes.api_resources.abstract import UpdateableAPIResource
from paayes.api_resources.abstract import custom_method


@custom_method("void_credit_note", http_verb="post", http_path="void")
class CreditNote(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "credit_note"

    def void_credit_note(self, idempotency_key=None, **params):
        url = self.instance_url() + "/void"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    @classmethod
    def preview(
        cls, api_key=None, paayes_version=None, paayes_account=None, **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key, api_version=paayes_version, account=paayes_account
        )
        url = cls.class_url() + "/preview"
        response, api_key = requestor.request("get", url, params)
        return util.convert_to_paayes_object(
            response, api_key, paayes_version, paayes_account
        )
