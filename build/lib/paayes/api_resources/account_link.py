from __future__ import absolute_import, division, print_function

from paayes.api_resources.abstract import CreateableAPIResource


class AccountLink(CreateableAPIResource):
    OBJECT_NAME = "account_link"
