import pytest
from base.webdriverfactory import WebDriverFactory


@pytest.fixture()
def setUp(request):
    print("Running method level setUp")
    wdf = WebDriverFactory()
    driver = wdf.getWebDriverInstance()
    if request.cls is not None:
       request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running method level tearDown")

@pytest.fixture(scope="class")
def oneTimeSetUp(request):
    print("Running class setUp")
    # wdf = WebDriverFactory()
    # driver = wdf.getWebDriverInstance()
    #
    # if request.cls is not None:
    #     request.cls.driver = driver

    yield

    # driver.quit()
    print("Running class tearDown")

