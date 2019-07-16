import pytest
from test.test_ui.pages import FilesPage
from test.test_ui.pages import HomePage
from test.test_ui.pages import LoginPage
import pdb

class TestFileUpload(object):

    _file_upload_path = "/upload/upload_testing.md"

    def test_upload(self):
        files_page = FilesPage(driver=self.driver)
        login_page = LoginPage(driver=self.driver)
        home_page = HomePage(driver=self.driver)
        self.driver.get(files_page.url)
        login_page.login()
        home_page.visit_files()
        assert files_page.upload_file(self._file_upload_path) == True
