import pytest
import os
from test.test_api.base import APISession

@pytest.fixture(scope="class", autouse=True)
def test_api_setup(request):
    api_base = APISession(os.environ["API_TOKEN"])
    if request.cls is not None:
        request.cls.session = api_base.session
    yield api_base.session
    api_base.session.close()
