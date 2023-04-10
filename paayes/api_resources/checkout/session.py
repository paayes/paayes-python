from __future__ import absolute_import, division, print_function

from paayes.api_resources.abstract import CreateableAPIResource
from paayes.api_resources.abstract import ListableAPIResource
from paayes.api_resources.abstract import nested_resource_class_methods


@nested_resource_class_methods("line_item", operations=["list"])
class Session(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "checkout.session"
