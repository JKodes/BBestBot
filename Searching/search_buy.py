import Searching.constants
import os
from selenium import webdriver

class Searching(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Searching, self).__init__()


    def main_page(self):
        self.get(Searching.constants.BASE_URL)
