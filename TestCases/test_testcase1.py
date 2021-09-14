# Launch Website
# Select from city
# Select To city
# Select date
# Click on search
# Select the filter 1 stop
# Verify that filtered results show results having 1 stop

from selenium.webdriver.common.keys import Keys

from PageObjects.FlightsPage import FlightsPage
from Utilities.BaseClass import BaseClass
import time


class TestYatraSite(BaseClass):

    def test_yatra_dot_com(self):


        print(self.driver.current_url)
        flightsPageObj = FlightsPage(self.driver)
        self.origin_to_wait("BE_flight_origin_city")
        fromcityvar = flightsPageObj.fromCity_func()
        fromcityvar.click()
        time.sleep(3)
        fromcityvar.send_keys("kolkata")
        time.sleep(2)
        fromcityvar.send_keys(Keys.ENTER)
        self.origin_to_wait("BE_flight_arrival_city")
        tocityvar = flightsPageObj.toCity_func()
        tocityvar.click()
        time.sleep(3)
        tocityvar.send_keys("Mumbai")
        time.sleep(3)
        tocityvar.send_keys(Keys.ENTER)
        flightsPageObj.departDatefield_func().click()
        flightsPageObj.actualDate_func().click()
        flightsListVar = flightsPageObj.searchflightButton_func()
        flightsListVar.stopsNumber_func().click()
        allstops1 = flightsListVar.stopNumber1_func()
        print(len(allstops1))
        print("hello")
        for i in allstops1:
            print("stop is:" +i.text)
            assert i.text == "1 Stop"
            print("assert passed")



















