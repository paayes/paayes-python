from __future__ import absolute_import, division, print_function

from paayes.api_resources.abstract.api_resource import APIResource
from paayes import api_requestor, util


class CreateableAPIResource(APIResource):
    @classmethod
    def create(
        cls,
        api_key=None,
        idempotency_key=None,
        paayes_version=None,
        paayes_account=None,
        **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key, api_version=paayes_version, account=paayes_account
        )
        url = cls.class_url()
        headers = util.populate_headers(idempotency_key)
        response, api_key = requestor.request("post", url, params, headers)

        return util.convert_to_paayes_object(
            response, api_key, paayes_version, paayes_account
        )
