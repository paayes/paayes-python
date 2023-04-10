from __future__ import absolute_import, division, print_function

import pytest

import paayes


TEST_RESOURCE_ID = "trr_123"


class TestReversal(object):
    def construct_resource(self):
        reversal_dict = {
            "id": TEST_RESOURCE_ID,
            "object": "reversal",
            "metadata": {},
            "transfer": "tr_123",
        }
        return paayes.Reversal.construct_from(reversal_dict, paayes.api_key)

    def test_has_instance_url(self, request_mock):
        resource = self.construct_resource()
        assert (
            resource.instance_url()
            == "/api/v1/transfers/tr_123/reversals/%s" % TEST_RESOURCE_ID
        )

    def test_is_not_modifiable(self, request_mock):
        with pytest.raises(NotImplementedError):
            paayes.Reversal.modify(TEST_RESOURCE_ID, metadata={"key": "value"})

    def test_is_not_retrievable(self, request_mock):
        with pytest.raises(NotImplementedError):
            paayes.Reversal.retrieve(TEST_RESOURCE_ID)

    def test_is_saveable(self, request_mock):
        resource = self.construct_resource()
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/api/v1/transfers/tr_123/reversals/%s" % TEST_RESOURCE_ID
        )
