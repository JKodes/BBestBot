import searching.constants
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

class Searching(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=False):   
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Searching, self).__init__()
        self.implicitly_wait(20)
        

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()


    def main_page(self):
        self.get(searching.constants.BASE_URL)

    def get_rid_of_survey(self):
        try:
            no_thanks = self.find_element_by_id('survey_invite_no')
            no_thanks.click()
        except:
            print('Continuing to the process... No Survey was found continue buying product')


    def type_item_of_choice(self, item):
        search_nav = self.find_element(By.XPATH, '//*[@id="gh-search-input"]')
        search_nav.send_keys(item)

    def click_button(self):
        search = self.find_element(By.CSS_SELECTOR,  'button[type="submit"]')
        search.click()

    def add_to_cart(self):
        add_item = self.find_element(By.CSS_SELECTOR, 'button[data-button-state="ADD_TO_CART"]' )
        add_item.click()

    def go_to_cart(self):
        go = self.find_element(By.CLASS_NAME, 'go-to-cart-button')
        go.click()
       

    def checkout(self):
        check_out = self.find_element(By.CSS_SELECTOR, 'button[data-track="Checkout - Top"]')
        check_out.click()

    def returning_customer_email(self, email):
        email_address = self.find_element(By.ID, 'fld-e')
        email_address.send_keys(email)

    def returning_customer_password(self, password):
        pswd = self.find_element(By.ID, 'fld-p1')
        pswd.send_keys(password)
        sign_in = self.find_element(By.CSS_SELECTOR, 'button[data-track="Sign In"]')
        sign_in.click()
        place_order = self.find_element(By.CSS_SELECTOR, 'button[data-track="Place your Order - Contact Card"]')
        place_order.click()

        


    



     
    



    