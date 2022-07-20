from .pages.login_page import LoginPage
from .pages.main_page import *


@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    main_page_link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, main_page_link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(page.browser, page.browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_continue_shopping_link()
