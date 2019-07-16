from test.test_ui.base import DriverUtils

class BasePage(DriverUtils):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = "https://platform.rescale.com"
