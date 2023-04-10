from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "US"


class TestCountrySpec(object):
    def test_is_listable(self, request_mock):
        resources = paayes.CountrySpec.list()
        request_mock.assert_requested("get", "/api/v1/country_specs")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.CountrySpec)

    def test_is_retrievable(self, request_mock):
        resource = paayes.CountrySpec.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/country_specs/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.CountrySpec)
