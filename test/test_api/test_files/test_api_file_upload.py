import os
import time
from shutil import copyfile
import requests
from test.test_api.api import APIFile
import pytest

class TestAPIFileUpload(object):

    _file_upload_path = "/upload/upload_testing.md"

    @pytest.fixture
    def test_file_upload(self, request):
        file_name, extension = self._file_upload_path.split(".")
        new_path = "{}_{}.{}".format(file_name, int(time.time()), extension)
        yield new_path
        if os.path.exists(new_path):
            os.remove(new_path)

    def test_api_file_upload(self, test_file_upload):
        file = APIFile(session=self.session)
        new_path = test_file_upload
        copyfile(self._file_upload_path, new_path)
        response = file.upload_file(new_path)
        assert file.response_content(response)["name"] == os.path.basename(new_path)
        assert file.response_content(response)["isUploaded"] == True
