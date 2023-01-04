from base.seleniumbase import SeleniumBase
from selenium.webdriver.common.keys import Keys


class MainPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.username = "valik-garkovenko"  # введите логин
        self.password = ""  # введите пароль
        self.main_page_wrapper = "//div[@class='PageWrapper_2aGaNaGauHNRzr8W2U0GwV']"
        self.authorisation_button = "//button[@class='Button2 Button2_size_m Button2_view_orange " \
                                    "Button2_weight_500 Button_3bxRfn2dtuSMoNjFiugM29 PSHeader-NoLoginButton']"
        self.username_input = "//input[@name='login']"
        self.password_input = "//input[@id='passp-field-passwd' and @name='passwd']"
        self.mail_folders = "// div[ @class ='Folders-m__root--cgVbj qa-LeftColumn-Folders']"

    def mainpage_validation(self):
        self._is_visible(self.main_page_wrapper)

    def log_click(self):
        self._is_visible(self.authorisation_button).click()

    def enter_username(self, username):
        self._is_visible(self.username_input).send_keys(username, Keys.ENTER)

    def enter_password(self, password):
        self._is_visible(self.password_input).send_keys(password, Keys.ENTER)

    def homepage_load(self):
        self._is_visible(self.mail_folders)

    def log_in(self):
        self._is_visible(self.authorisation_button).click()
        self._is_visible(self.username_input).send_keys(self.username, Keys.ENTER)
        self._is_visible(self.password_input).send_keys(self.password, Keys.ENTER)
        self._is_visible(self.mail_folders)
