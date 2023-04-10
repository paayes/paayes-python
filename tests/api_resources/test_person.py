from __future__ import absolute_import, division, print_function

import pytest

import paayes


TEST_RESOURCE_ID = "trr_123"


class TestPerson(object):
    def construct_resource(self):
        person_dict = {
            "id": TEST_RESOURCE_ID,
            "object": "person",
            "account": "acct_123",
        }
        return paayes.Person.construct_from(person_dict, paayes.api_key)

    def test_has_instance_url(self, request_mock):
        resource = self.construct_resource()
        assert (
            resource.instance_url()
            == "/api/v1/accounts/acct_123/persons/%s" % TEST_RESOURCE_ID
        )

    def test_is_not_modifiable(self, request_mock):
        with pytest.raises(NotImplementedError):
            paayes.Person.modify(TEST_RESOURCE_ID, first_name="John")

    def test_is_not_retrievable(self, request_mock):
        with pytest.raises(NotImplementedError):
            paayes.Person.retrieve(TEST_RESOURCE_ID)

    def test_is_saveable(self, request_mock):
        resource = self.construct_resource()
        resource.first_name = "John"
        resource.save()
        request_mock.assert_requested(
            "post", "/api/v1/accounts/acct_123/persons/%s" % TEST_RESOURCE_ID
        )
