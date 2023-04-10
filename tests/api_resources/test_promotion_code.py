from __future__ import absolute_import, division, print_function

import paayes


TEST_RESOURCE_ID = "promo_123"


class TestPromotionCode(object):
    def test_is_listable(self, request_mock):
        resources = paayes.PromotionCode.list()
        request_mock.assert_requested("get", "/api/v1/promotion_codes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.PromotionCode)

    def test_is_retrievable(self, request_mock):
        resource = paayes.PromotionCode.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/api/v1/promotion_codes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.PromotionCode)

    def test_is_creatable(self, request_mock):
        resource = paayes.PromotionCode.create(coupon="co_123", code="MYCODE")
        request_mock.assert_requested("post", "/api/v1/promotion_codes")
        assert isinstance(resource, paayes.PromotionCode)

    def test_is_saveable(self, request_mock):
        resource = paayes.PromotionCode.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/api/v1/promotion_codes/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = paayes.PromotionCode.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/api/v1/promotion_codes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, paayes.PromotionCode)
