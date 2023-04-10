from __future__ import absolute_import, division, print_function

import paayes


class TestSourceTransaction(object):
    def test_is_listable(self, request_mock):
        source = paayes.Source.construct_from(
            {"id": "src_123", "object": "source"}, paayes.api_key
        )
        source_transactions = source.source_transactions()
        request_mock.assert_requested(
            "get", "/api/v1/sources/src_123/source_transactions"
        )
        assert isinstance(source_transactions.data, list)
        assert isinstance(
            source_transactions.data[0], paayes.SourceTransaction
        )
