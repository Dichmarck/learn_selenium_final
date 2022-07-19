import time
from learn_selenium_final.pages.base_page import BasePage
from learn_selenium_final.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        self.click_on_add_to_basket_button()
        self.solve_quiz_and_get_code()
        self.should_be_basket_price_equal_to_product_price()
        time.sleep(1200)

    def should_be_add_to_basket_button(self):
        self.is_elemet_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON)

    def click_on_add_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_succes_add_alert(self):
        pass

    def should_be_basket_price_equal_to_product_price(self):
        product_price_text = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        basket_price_text = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        print(product_price_text)
        print(basket_price_text)


# cd learn_selenium_final
# pytest -s -v --tb=line --language=ru test_product_page.py