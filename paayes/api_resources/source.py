from __future__ import absolute_import, division, print_function

from paayes import error
from paayes import util
from paayes.api_resources import Customer
from paayes.api_resources.abstract import CreateableAPIResource
from paayes.api_resources.abstract import UpdateableAPIResource
from paayes.api_resources.abstract import VerifyMixin
from paayes.api_resources.abstract import nested_resource_class_methods
from paayes.six.moves.urllib.parse import quote_plus


@nested_resource_class_methods("source_transaction", operations=["list"])
class Source(CreateableAPIResource, UpdateableAPIResource, VerifyMixin):
    OBJECT_NAME = "source"

    def detach(self, idempotency_key=None, **params):
        token = util.utf8(self.id)

        if hasattr(self, "customer") and self.customer:
            extn = quote_plus(token)
            customer = util.utf8(self.customer)
            base = Customer.class_url()
            owner_extn = quote_plus(customer)
            url = "%s/%s/sources/%s" % (base, owner_extn, extn)
            headers = util.populate_headers(idempotency_key)

            self.refresh_from(self.request("delete", url, params, headers))
            return self

        else:
            raise error.InvalidRequestError(
                "Source %s does not appear to be currently attached "
                "to a customer object." % token,
                "id",
            )

    def source_transactions(self, **params):
        """source_transactions is deprecated, use Source.list_source_transactions instead."""
        return self.request(
            "get", self.instance_url() + "/source_transactions", params
        )
