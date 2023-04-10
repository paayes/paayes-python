from __future__ import absolute_import, division, print_function

from paayes import util
from paayes.api_resources.abstract import ListableAPIResource
from paayes.api_resources.abstract import UpdateableAPIResource
from paayes.api_resources.abstract import custom_method


@custom_method("close", http_verb="post")
class Dispute(ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "dispute"

    def close(self, idempotency_key=None, **params):
        url = self.instance_url() + "/close"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self
