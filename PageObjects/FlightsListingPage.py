from selenium.webdriver.common.by import By


class FlightsListingPage:

    def __init__(self,driver):
        self.driver = driver

    stopsNumber_locate = (By.XPATH,"//div[@class='i-b pl-18 pt-12 pr filter-stops heading ']/label[2]/p")

    stopNumber1_loacate = (By.XPATH,"//div[@class = ' font-lightgrey fs-10 tipsy i-b fs-10']/span")

    def stopsNumber_func(self):
        return self.driver.find_element(*FlightsListingPage.stopsNumber_locate)

    def stopNumber1_func(self):
        return self.driver.find_elements(*FlightsListingPage.stopNumber1_loacate)


