import time
from learn_selenium_final.pages.base_page import BasePage
from learn_selenium_final.pages.locators import BasePageLocators,BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Products present in basket, but they shouldn't to"

    def should_be_continue_shopping_link(self):
        assert self.is_element_present(*BasketPageLocators.CONTINUE_SHOPPING_LINK), \
            "No continue shopping link in basket"