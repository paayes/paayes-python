from __future__ import absolute_import, division, print_function

from paayes.paayes_object import PaayesObject


# This resource can only be instantiated when expanded on a BalanceTransaction
class RecipientTransfer(PaayesObject):
    OBJECT_NAME = "recipient_transfer"
