from argparse import ArgumentTypeError

import pytest as pytest
from selenium import webdriver
from webium import BasePage





def pytest_addoption(parser):
    parser.addoption(
        '--hub_url',
        action='store',
        required=False,
        dest='hub_url',
        help='Hub'
    )

    parser.addoption(
        '--browser',
        action='append',
        required=False,
        default=[],
        dest='browser',
        help='Browser name for grid capabilities'
    )

@pytest.fixture
def driver_manager(request,browserName):
    BasePage._driver = webdriver.Remote(command_executor=request.config.option.hub_url,
                                        desired_capabilities={'browserName': browserName})
    BasePage._driver.implicitly_wait(10)
    yield BasePage._driver

    def exit_driver():
        BasePage._driver.quit()
    request.addfinalizer(exit_driver)



def pytest_generate_tests(metafunc):
    if 'browserName' in metafunc.fixturenames:
        metafunc.parametrize('browserName',
                             metafunc.config.getoption('browser'))