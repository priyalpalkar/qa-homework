import os
from test.test_ui.pages import HomePage
import pdb
import time

class FilesPage(HomePage):

    _upload_file_input = "#filesPageDropZone input"
    _filtered_file_count = "strong[ng-bind=filteredListLength]"
    _opening_folder = "span[ng-if=openingFolder]"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = os.path.join(self.url, "files")

    def upload_file(self, file_path, *args, **kwargs):
        #Sometimes the uploaded file doesn't show up in the data table even after the
        #page is refreshed (files are not loaded from the server).
        #Not sure if that is indented, verifying that the file is uploaded
        #by validating that the count of the files has increased in the data table
        self._wait_for_files_to_be_loaded()
        current_file_count = self._current_file_count()
        element = self.find_element(self._upload_file_input)
        self.send_keys(element, file_path, ajax_timeout=20)
        self._wait_for_files_to_be_loaded()
        #Browser needs to be sometimes refreshed twice to make sure uploaded file shows up..
        for _ in range(2):    
            self.driver.refresh()
            self._wait_for_files_to_be_loaded()
            if self.verify_uploaded_file(current_file_count, *args, **kwargs):
                return True
        return False

    def verify_uploaded_file(self, original_file_count, *args, **kwargs):
        current_file_count = self._current_file_count()
        if current_file_count == original_file_count:
            return False
        return True

    def _current_file_count(self):
        current_file_count = 0
        file_count_element = self.find_element(self._filtered_file_count)
        if file_count_element.text != "":
            current_file_count = int(file_count_element.text)
        return current_file_count

    def _wait_for_files_to_be_loaded(self):
        loading_files = self.find_element(self._opening_folder, raise_exception=False, timeout=5)
        if loading_files:
            self.wait_for_element_invisibility(self._opening_folder, timeout=50)
