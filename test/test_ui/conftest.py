import pytest
from test.test_ui.base import DriverFactory
from selenium.common.exceptions import WebDriverException

# @pytest.fixture(scope="session", autouse=True)
# def driver_setup(request):
#     print("Running one time setUp")
#     try:
#         df = DriverFactory()
#         driver = df.driver_factory()
#     except WebDriverException as e:
#         print("Error: {}".format(e))
#     finally:
#         driver.quit()
#     yield driver
#     #driver.quit()
#     print("Running one time tearDown")

@pytest.fixture(scope="class", autouse=True)
def test_setup(request):
    print("Running one time setUp")
    df = DriverFactory()
    driver = df.driver_factory()
    # driver = driver_setup
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time tearDown")

