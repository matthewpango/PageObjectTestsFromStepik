from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators():
    ADD_TO_BASKET = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    ASSERT_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    BOOK_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1') 
    ASSERT_BOOK =  (By.XPATH, '//*[@id="messages"]/div[1]/div/strong') 


