import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action='store', default='chrome'

    )

@pytest.fixture(scope='class')
def setup_yatra(request):

    option1 = Options()
    option1.add_argument("--disable-notifications")
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=option1)

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=option1)

    elif browser_name == "IE":
        driver = webdriver.Ie(IEDriverManager().install(),options=option1)

    driver.implicitly_wait(10)
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver = driver









