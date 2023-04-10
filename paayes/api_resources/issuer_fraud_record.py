from __future__ import absolute_import, division, print_function

from paayes.api_resources.abstract import ListableAPIResource


class IssuerFraudRecord(ListableAPIResource):
    OBJECT_NAME = "issuer_fraud_record"
