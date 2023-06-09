from __future__ import absolute_import, division, print_function

from paayes import util
from paayes.api_resources.abstract import ListableAPIResource
from paayes.api_resources.customer import Customer
from paayes.six.moves.urllib.parse import quote_plus


class BitcoinReceiver(ListableAPIResource):
    OBJECT_NAME = "bitcoin_receiver"

    def instance_url(self):
        token = util.utf8(self.id)
        extn = quote_plus(token)

        if hasattr(self, "customer"):
            customer = util.utf8(self.customer)
            base = Customer.class_url()
            cust_extn = quote_plus(customer)
            return "%s/%s/sources/%s" % (base, cust_extn, extn)
        else:
            base = BitcoinReceiver.class_url()
            return "%s/%s" % (base, extn)

    @classmethod
    def class_url(cls):
        return "/api/v1/bitcoin/receivers"
