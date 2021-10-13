from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.browser.current_url, "URL is not correct!"
               

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not available!"
           

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not available!"
    def register_new_user(self, email, password):
        e = self.browser.find_element(*LoginPageLocators.REGISTER_MAIL)
        e.send_keys(email)
        pas = self.browser.find_element(*LoginPageLocators.REGISTER_PASS1)
        pas.send_keys(password)
        pas2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS2)
        pas2.send_keys(password)
        reg_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        reg_btn.click()
        time.sleep(10)
