import pytest
from test.test_ui.base import DriverFactory
from selenium.common.exceptions import WebDriverException

@pytest.fixture(scope="class", autouse=True)
def test_setup(request):
    df = DriverFactory()
    driver = df.driver_factory()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
