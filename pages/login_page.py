from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in url of login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No login form in login page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "No register form in login page"

    def should_be_success_register_message(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_SUCCESS_MSG), \
            "No success registration message"

    def register_new_user(self, email, password):
        self.should_be_register_form()

        email_form = self.browser.find_element(*LoginPageLocators.EMAIL_FORM)
        email_form.send_keys(email)
        password_form_1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM_1)
        password_form_1.send_keys(password)
        password_form_2 = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM_2)
        password_form_2.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_btn.click()

        self.should_be_success_register_message()


