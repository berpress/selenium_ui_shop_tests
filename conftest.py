 
import pytest
from fixture.application import Application
import logging

logger = logging.getLogger()


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base-url")
    fixture = Application(base_url)
    fixture.wd.maximize_window()
    fixture.wd.implicitly_wait(10)
    yield fixture
    fixture.destroy()


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="http://automationpractice.com/",
        help="enter base_url",
    )
