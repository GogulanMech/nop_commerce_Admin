from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    else:
        driver = webdriver.Edge()

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########### HTML REPORT ##########
# def pytest_configure(config):
#     config._metadata["Project Name"] = "nop commerce"
#     config._metadata["Module"] = "customer"
#     config._metadata["Tester"] = "Gogulan"


# @pytest.mark.optionalhook
# def meta_config(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
