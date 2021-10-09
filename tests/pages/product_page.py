from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
import time

class ProductPage(BasePage):
    def add_to_basket(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_btn.click()
        self.solve_quiz_and_get_code()
        time.sleep(2)
        a = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        b = self.browser.find_element(*ProductPageLocators.ASSERT_BOOK).text
        assert a == b, "Book name is not equal!"
        c = self.browser.find_element(*ProductPageLocators.PRICE).text
        d = self.browser.find_element(*ProductPageLocators.ASSERT_PRICE).text
        assert c == d, "Price is not equal!"
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ASSERT_BOOK), \
           "Success message is presented, but should not be"
    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ASSERT_BOOK), \
            "Success message is appear, but should not be"

           

       
        

        

        
        
        
        

        


        
    




