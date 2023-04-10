from __future__ import absolute_import, division, print_function

from paayes import api_requestor
from paayes import util
from paayes.api_resources.abstract import DeletableAPIResource


class EphemeralKey(DeletableAPIResource):
    OBJECT_NAME = "ephemeral_key"

    @classmethod
    def create(
        cls,
        api_key=None,
        idempotency_key=None,
        paayes_version=None,
        paayes_account=None,
        **params
    ):
        if paayes_version is None:
            raise ValueError(
                "paayes_version must be specified to create an ephemeral "
                "key"
            )

        requestor = api_requestor.APIRequestor(
            api_key, api_version=paayes_version, account=paayes_account
        )

        url = cls.class_url()
        headers = util.populate_headers(idempotency_key)
        response, api_key = requestor.request("post", url, params, headers)
        return util.convert_to_paayes_object(
            response, api_key, paayes_version, paayes_account
        )
