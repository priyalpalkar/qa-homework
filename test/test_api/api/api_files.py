import os
from test.test_api.api import APIBase

class APIFile(APIBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = os.path.join(self.url, "files/")

    def list_files(self, *args, **kwargs):
        url = self.url
        count_till_now = 0
        while True:
            response = self.get(url)
            response_content = response.json()
            yield response_content["results"]
            total_count = response_content["count"]
            current_count = len(response_content["results"])
            count_till_now += current_count
            if total_count == count_till_now:
                raise StopIteration
            url = response_content["next"]

    def find_file_by_name(self, file_name):
        for files in self.list_files():
            for file in files:
                if file["name"] == file_name:
                    return file
        return file

    def upload_file(self, file_path):
        upload_url = os.path.join(self.url, "contents/")
        response = None
        with open(file_path, 'rb') as f:
            files = {
                'file': (os.path.basename(file_path), f,
                    {
                        'type_id': 1
                    }
                )
            }
            response = self.post(upload_url, files=files)
        return response
