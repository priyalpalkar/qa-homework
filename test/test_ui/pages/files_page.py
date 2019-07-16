import os
from test.test_ui.pages import HomePage
import pdb
import time

class FilesPage(HomePage):

    _upload_file_input = "#filesPageDropZone input"
    _filtered_file_count = "strong[ng-bind=filteredListLength]"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = os.path.join(self.url, "files")

    def upload_file(self, file_path, *args, **kwargs):
        current_file_count = int(self.find_element(self._filtered_file_count).text)
        element = self.find_element(self._upload_file_input)
        self.send_keys(element, file_path, ajax_timeout=20)
        if not self.verify_uploaded_file(file_path, *args, **kwargs):
            return False
        return True

    def verify_uploaded_file(self, original_file_count, *args, **kwargs):
        current_file_count = int(self.find_element(self._filtered_file_count).text)
        if current_file_count == original_file_count:
            return False
        return True
