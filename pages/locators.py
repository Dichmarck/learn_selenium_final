from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6 h1")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    BASKET_PRICE = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs")
    SUCCESS_ADD_ALERT = (By.XPATH, "//div[contains(@class, 'alertinner')]")
