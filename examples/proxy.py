from __future__ import absolute_import, division, print_function

import os

import paayes


paayes.api_key = os.environ.get("PAAYES_SECRET_KEY")

print("Attempting charge...")

proxy = {
    "http": "http://<user>:<pass>@<proxy>:<port>",
    "https": "http://<user>:<pass>@<proxy>:<port>",
}

clients = (
    paayes.http_client.RequestsClient(
        verify_ssl_certs=paayes.verify_ssl_certs, proxy=proxy
    ),
    paayes.http_client.PycurlClient(
        verify_ssl_certs=paayes.verify_ssl_certs, proxy=proxy
    ),
    paayes.http_client.Urllib2Client(
        verify_ssl_certs=paayes.verify_ssl_certs, proxy=proxy
    ),
)

for c in clients:
    paayes.default_http_client = c
    resp = paayes.Charge.create(
        amount=200,
        currency="usd",
        card="tok_visa",
        description="customer@gmail.com",
    )
    print("Success: %s, %r" % (c.name, resp))
