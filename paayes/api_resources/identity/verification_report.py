from __future__ import absolute_import, division, print_function

from paayes.api_resources.abstract import ListableAPIResource


class VerificationReport(ListableAPIResource):
    OBJECT_NAME = "identity.verification_report"
