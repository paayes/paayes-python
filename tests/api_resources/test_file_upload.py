from __future__ import absolute_import, division, print_function

import tempfile

import pytest

import paayes


TEST_RESOURCE_ID = "file_123"


class TestFileUpload(object):
    @pytest.fixture(scope="function")
    def setup_upload_api_base(self):
        paayes.upload_api_base = paayes.api_base
        paayes.api_base = None
        yield
        paayes.api_base = paayes.upload_api_base
        paayes.upload_api_base = "https://files.paayes.com"

    def test_is_listable(self, request_mock):
        resources = paayes.FileUpload.list()
        request_mock.assert_requested("get", "/api/v1/files")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], paayes.FileUpload)

    def test_is_retrievable(self, request_mock):
        resource = paayes.FileUpload.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/api/v1/files/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, paayes.FileUpload)

    def test_is_creatable(self, setup_upload_api_base, request_mock):
        paayes.multipart_data_generator.MultipartDataGenerator._initialize_boundary = (
            lambda self: 1234567890
        )
        test_file = tempfile.TemporaryFile()
        resource = paayes.FileUpload.create(
            purpose="dispute_evidence",
            file=test_file,
            file_link_data={"create": True},
        )
        request_mock.assert_api_base(paayes.upload_api_base)
        request_mock.assert_requested(
            "post",
            "/api/v1/files",
            headers={
                "Content-Type": "multipart/form-data; boundary=1234567890"
            },
        )
        assert isinstance(resource, paayes.FileUpload)

    def test_deserializes_from_file(self):
        obj = paayes.util.convert_to_paayes_object({"object": "file"})
        assert isinstance(obj, paayes.FileUpload)

    def test_deserializes_from_file_upload(self):
        obj = paayes.util.convert_to_paayes_object({"object": "file_upload"})
        assert isinstance(obj, paayes.FileUpload)
