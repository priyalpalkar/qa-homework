from test.test_ui.pages import BasePage

class HomePage(BasePage):

    _files = "#menuFiles"

    def visit_files(self):
        self.click(self._files)
