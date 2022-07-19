import pytest
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def should_be_login_link(self):  # заранее провальный
        assert self.is_elemet_present(*MainPageLocators.LOGIN_LINK)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()


