import searching.constants
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

class Searching(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers", ):   #,teardown=False
        self.driver_path = driver_path
        #self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Searching, self).__init__()
        self.implicitly_wait(9)
        

    #def __exit__(self, exc_type, exc_val, exc_tb):
    #    if self.teardown:
    #        self.quit()


    def main_page(self):
        self.get(searching.constants.BASE_URL)

    def type_item_of_choice(self, item):
        search_nav = self.find_element(By.XPATH, '//*[@id="gh-search-input"]')
        search_nav.send_keys(item)

