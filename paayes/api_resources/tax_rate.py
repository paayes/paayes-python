from __future__ import absolute_import, division, print_function

from paayes.api_resources.abstract import CreateableAPIResource
from paayes.api_resources.abstract import ListableAPIResource
from paayes.api_resources.abstract import UpdateableAPIResource


class TaxRate(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "tax_rate"
