import time, re
from learn_selenium_final.pages.base_page import BasePage
from learn_selenium_final.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        self.click_on_add_to_basket_button()
        self.solve_quiz_and_get_code()
        self.should_be_success_add_alert()
        self.should_be_basket_price_equal_to_product_price()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON)

    def click_on_add_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_success_add_alert(self):
        success_alert = self.browser.find_element(*ProductPageLocators.SUCCESS_ADD_ALERT).text.strip()
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text.strip()
        assert product_name in success_alert, \
            "Product name in basket not equals to actual product name:"

    def should_be_basket_price_equal_to_product_price(self):
        basket_price_text = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text.split('\n')[0]
        product_price_text = self.browser.find_element(*ProductPageLocators.PRICE).text
        basket_price = re.search(r"\d+[.,]\d+", basket_price_text)[0]
        product_price = re.search(r"\d+[.,]\d+", product_price_text)[0]
        assert product_price == basket_price, \
            f"Basket total price not equals to product price: product: {product_price}, basket: {basket_price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADD_ALERT), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ADD_ALERT), \
            "Success message didn't disappeared, but it should to"

# cd learn_selenium_final
# pytest -s -v --tb=line --language=ru test_product_page.py
