from tests.pages.base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def order_button_inactive(self):
        assert self.is_not_element_present(*BasketPageLocators.ORDER_BTN), "Order button is presented, but shouldnt be!"
    def basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_ASSERT), "Basket should be empty!"
    
