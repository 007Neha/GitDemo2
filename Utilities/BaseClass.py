import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup_yatra")
class BaseClass:

    def origin_to_wait(self,value):
        wait = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, value)))


