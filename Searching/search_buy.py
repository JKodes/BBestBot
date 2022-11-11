import searching.constants
import os
from selenium import webdriver

class Searching(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Searching, self).__init__()
        self.implicitly_wait(9)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()


    def main_page(self):
        self.get(searching.constants.BASE_URL)
