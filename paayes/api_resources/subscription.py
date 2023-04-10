from __future__ import absolute_import, division, print_function

from paayes import api_requestor
from paayes.api_resources.abstract import CreateableAPIResource
from paayes.api_resources.abstract import DeletableAPIResource
from paayes.api_resources.abstract import ListableAPIResource
from paayes.api_resources.abstract import UpdateableAPIResource
from paayes.api_resources.abstract import custom_method


@custom_method("delete_discount", http_verb="delete", http_path="discount")
class Subscription(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "subscription"

    def delete_discount(self, **params):
        requestor = api_requestor.APIRequestor(
            self.api_key,
            api_version=self.paayes_version,
            account=self.paayes_account,
        )
        url = self.instance_url() + "/discount"
        _, api_key = requestor.request("delete", url, params)
        self.refresh_from({"discount": None}, api_key, True)
