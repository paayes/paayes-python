from __future__ import absolute_import, division, print_function

from paayes.api_resources.abstract import CreateableAPIResource


class Session(CreateableAPIResource):
    OBJECT_NAME = "billing_portal.session"
