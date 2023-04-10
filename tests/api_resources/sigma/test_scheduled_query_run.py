from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "sqr_123"


class TestTransaction(object):
    def test_is_listable(self, request_mock):
        resources = paayes.sigma.ScheduledQueryRun.list()
        request_mock.assert_requested("get", "/api/v1/sigma/scheduled_query_runs")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.sigma.ScheduledQueryRun)

    def test_is_retrievable(self, request_mock):
        resource = paayes.sigma.ScheduledQueryRun.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/sigma/scheduled_query_runs/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.sigma.ScheduledQueryRun)
