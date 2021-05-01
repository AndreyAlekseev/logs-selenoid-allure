import pytest
from selenium import webdriver
import logging

logging.basicConfig(level=logging.INFO, filename="logs/logtests.log")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "ie"], help="Select one browser")
    parser.addoption("--bversion", action="store", default="90.0", help="Enter browser version")
    parser.addoption("--executor", action="store", default="localhost", help="Enter executor")
    parser.addoption("--url", action="store", default="https://demo.opencart.com/", help="Enter base url")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)
    parser.addoption("--mobile", action="store_true")


@pytest.fixture(scope='session')
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="function")
def browser(request, base_url):
    browser = request.config.getoption("--browser")
    version = request.config.getoption("--bversion")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")
    mobile = request.config.getoption("--mobile")

    driver = None

    executor_url = f"http://{executor}:4444/wd/hub"

    capabilities = {
        "browserName": browser,
        "browserVersion": version,
        "selenoid:options": {
            "enableVNC": vnc,
            "enableVideo": videos,
            "enableLog": logs
        },
        'acceptSslCerts': True,
        'acceptInsecureCerts': True,
        'goog:chromeOptions': {
            'args': []
        }
    }

    if browser == "chrome":
        if mobile:
            capabilities["goog:chromeOptions"]["mobileEmulation"] = {"deviceName": "iPhone 5/SE"}
        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=capabilities
        )

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
