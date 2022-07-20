import pytest
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .basket_page import BasketPage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)


