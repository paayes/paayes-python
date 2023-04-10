from __future__ import absolute_import, division, print_function

import paayes
from paayes import api_requestor
from paayes import util
from paayes.api_resources.abstract import ListableAPIResource


class File(ListableAPIResource):
    OBJECT_NAME = "file"

    # This resource can have two different object names. In latter API
    # versions, only `file` is used, but since paayes-python may be used with
    # any API version, we need to support deserializing the older
    # `file_upload` object into the same class.
    OBJECT_NAME_ALT = "file_upload"

    @classmethod
    def class_url(cls):
        return "/api/v1/files"

    @classmethod
    def create(
        # 'api_version' is deprecated, please use 'paayes_version'
        cls,
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
        url = cls.class_url()
        supplied_headers = {"Content-Type": "multipart/form-data"}
        response, api_key = requestor.request(
            "post", url, params=params, headers=supplied_headers
        )
        return util.convert_to_paayes_object(
            response, api_key, version, paayes_account
        )


# For backwards compatibility, the `File` class is aliased to `FileUpload`.
FileUpload = File
