from __future__ import absolute_import, division, print_function

import paayes


class TestUsageRecordSummary(object):
    def test_is_listable(self, request_mock):
        resource = paayes.SubscriptionItem.retrieve("si_123")
        usage_record_summaries = resource.usage_record_summaries()
        request_mock.assert_requested(
            "get", "/api/v1/subscription_items/si_123/usage_record_summaries"
        )
        assert isinstance(usage_record_summaries.data, list)
        assert isinstance(
            usage_record_summaries.data[0], paayes.UsageRecordSummary
        )
