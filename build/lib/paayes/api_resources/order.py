from __future__ import absolute_import, division, print_function

from paayes import util
from paayes.api_resources.abstract import CreateableAPIResource
from paayes.api_resources.abstract import ListableAPIResource
from paayes.api_resources.abstract import UpdateableAPIResource
from paayes.api_resources.abstract import custom_method


@custom_method("return_order", http_verb="post", http_path="returns")
@custom_method("pay", http_verb="post")
class Order(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "order"

    def pay(self, idempotency_key=None, **params):
        url = self.instance_url() + "/pay"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def return_order(self, idempotency_key=None, **params):
        headers = util.populate_headers(idempotency_key)
        return self.request(
            "post", self.instance_url() + "/returns", params, headers
        )
