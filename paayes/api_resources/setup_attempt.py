from __future__ import absolute_import, division, print_function

from paayes.api_resources.abstract import ListableAPIResource


class SetupAttempt(ListableAPIResource):
    OBJECT_NAME = "setup_attempt"
