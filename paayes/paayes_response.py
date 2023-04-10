from __future__ import absolute_import, division, print_function

import json
from collections import OrderedDict


class PaayesResponseBase(object):
    def __init__(self, code, headers):
        self.code = code
        self.headers = headers

    @property
    def idempotency_key(self):
        try:
            return self.headers["idempotency-key"]
        except KeyError:
            return None

    @property
    def request_id(self):
        try:
            return self.headers["request-id"]
        except KeyError:
            return None


class PaayesResponse(PaayesResponseBase):
    def __init__(self, body, code, headers):
        PaayesResponseBase.__init__(self, code, headers)
        self.body = body
        self.data = json.loads(body, object_pairs_hook=OrderedDict)


class PaayesStreamResponse(PaayesResponseBase):
    def __init__(self, io, code, headers):
        PaayesResponseBase.__init__(self, code, headers)
        self.io = io
