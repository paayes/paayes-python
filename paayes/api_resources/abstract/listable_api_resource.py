from __future__ import absolute_import, division, print_function

from paayes import api_requestor, util
from paayes.api_resources.abstract.api_resource import APIResource


class ListableAPIResource(APIResource):
    @classmethod
    def auto_paging_iter(cls, *args, **params):
        return cls.list(*args, **params).auto_paging_iter()

    @classmethod
    def list(
        cls, api_key=None, paayes_version=None, paayes_account=None, **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key,
            api_base=cls.api_base(),
            api_version=paayes_version,
            account=paayes_account,
        )
        url = cls.class_url()
        response, api_key = requestor.request("get", url, params)
        paayes_object = util.convert_to_paayes_object(
            response, api_key, paayes_version, paayes_account
        )
        paayes_object._retrieve_params = params
        return paayes_object
