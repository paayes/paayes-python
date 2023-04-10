from __future__ import absolute_import, division, print_function

from paayes import api_requestor, util
from paayes.api_resources.abstract import APIResource


class UsageRecord(APIResource):
    OBJECT_NAME = "usage_record"

    @classmethod
    def create(
        cls,
        api_key=None,
        idempotency_key=None,
        paayes_version=None,
        paayes_account=None,
        **params
    ):
        if "subscription_item" not in params:
            raise ValueError("Params must have a subscription_item key")

        subscription_item = params.pop("subscription_item")

        requestor = api_requestor.APIRequestor(
            api_key, api_version=paayes_version, account=paayes_account
        )
        url = "/api/v1/subscription_items/%s/usage_records" % subscription_item
        headers = util.populate_headers(idempotency_key)
        response, api_key = requestor.request("post", url, params, headers)

        return util.convert_to_paayes_object(
            response, api_key, paayes_version, paayes_account
        )
