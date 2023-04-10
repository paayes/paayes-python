from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "txcd_123"


class TestTaxCode(object):
    def test_is_listable(self, request_mock):
        resources = paayes.TaxCode.list()
        request_mock.assert_requested("get", "/api/v1/tax_codes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.TaxCode)

    def test_is_retrievable(self, request_mock):
        resource = paayes.TaxCode.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/tax_codes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.TaxCode)
