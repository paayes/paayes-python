from __future__ import absolute_import, division, print_function

from paayes.api_resources.abstract import ListableAPIResource


class Event(ListableAPIResource):
    OBJECT_NAME = "event"
