import os
from test.test_ui.pages import BasePage
import pdb

class LoginPage(BasePage):

    _username = ".box.email-box input"
    _password = ".input-container input[type=password]"
    _next_step = ".next-step.ready"
    _submit = ".input-container button[type=submit]"

    def login(self, *args, **kwargs):
        self.send_keys(self.find_element(self._username), "priyal.palkar@gmail.com")
        self.click(self._next_step)
        self.send_keys(self.find_element(self._password), "Welcome!")
        self.click(self._submit)
