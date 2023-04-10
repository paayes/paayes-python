from __future__ import absolute_import, division, print_function

import os

# Paayes Python bindings
# API docs at http://docs.paayes.com/api/
# Authors:
# Patrick Collison <patrick@paayes.com>
# Greg Brockman <gdb@paayes.com>
# Andrew Metcalf <andrew@paayes.com>

# Configuration variables

api_key = None
client_id = None
api_base = "https://api.paayes.com"
connect_api_base = ""
upload_api_base = ""
api_version = None
verify_ssl_certs = True
proxy = None
default_http_client = None
app_info = None
enable_telemetry = True
max_network_retries = 0
ca_bundle_path = os.path.join(
    os.path.dirname(__file__), "data", "ca-certificates.crt"
)

# Set to either 'debug' or 'info', controls console logging
log = None

# API resources
from paayes.api_resources import *  # noqa

# OAuth
from paayes.oauth import OAuth  # noqa

# Webhooks
from paayes.webhook import Webhook, WebhookSignature  # noqa


# Sets some basic information about the running application that's sent along
# with API requests. Useful for plugin authors to identify their plugin when
# communicating with Paayes.
#
# Takes a name and optional version and plugin URL.
def set_app_info(name, partner_id=None, url=None, version=None):
    global app_info
    app_info = {
        "name": name,
        "partner_id": partner_id,
        "url": url,
        "version": version,
    }
