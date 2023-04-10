from __future__ import absolute_import, division, print_function

from paayes import util
from paayes.api_resources.abstract import CreateableAPIResource
from paayes.api_resources.abstract import ListableAPIResource
from paayes.api_resources.abstract import UpdateableAPIResource
from paayes.api_resources.abstract import custom_method


@custom_method("attach", http_verb="post")
@custom_method("detach", http_verb="post")
class PaymentMethod(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "payment_method"

    def attach(self, idempotency_key=None, **params):
        url = self.instance_url() + "/attach"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def detach(self, idempotency_key=None, **params):
        url = self.instance_url() + "/detach"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self
