from selenium.webdriver.common.by import By

from PageObjects.FlightsListingPage import FlightsListingPage


class FlightsPage:

    def __init__(self,driver):
        self.driver = driver


    fromCity_loacte = (By.ID,"BE_flight_origin_city")

    toCity_locate = (By.ID,"BE_flight_arrival_city")

    departDate_locate = (By.ID, "BE_flight_origin_date")

    actualDate_locate = (By.XPATH,"//td[@id= '29/08/2021']")

    searchflightButton_locate = (By.ID,"BE_flight_flsearch_btn")


    def fromCity_func(self):
        return self.driver.find_element(*FlightsPage.fromCity_loacte)

    def toCity_func(self):
        return self.driver.find_element(*FlightsPage.toCity_locate)

    def departDatefield_func(self):
        return self.driver.find_element(*FlightsPage.departDate_locate)

    def actualDate_func(self):
        return self.driver.find_element(*FlightsPage.actualDate_locate)

    def searchflightButton_func(self):
        self.driver.find_element(*FlightsPage.searchflightButton_locate).click()
        flightsListObj = FlightsListingPage(self.driver)
        return flightsListObj










