import selenium
import time
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from base.seleniumbase import SeleniumBase
from selenium.webdriver.common.keys import Keys


class HomePage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.write_mail_button = "//div/a[@class='Button2 Button2_type_link Button2_view_action Button2_size_m " \
                                 "Layout-m__compose--pTDsx qa-LeftColumn-ComposeButton ComposeButton-m__root--fP-o9']"
        self.write_mail_popup = "// div[ @class ='composeReact__inner']12"
        self.write_mail_to_input = "//*[@id='compose-field-1']"
        self.write_mail_theme_input = "//*[@id='compose-field-subject-4']"
        self.write_mail_text_input = "//*[@id='cke_1_contents']/div"
        self.write_mail_send_button = "//button[@type='button' and @class='Button2 Button2_pin_circle-circle " \
                                      "Button2_view_default Button2_size_l']"
        self.mail_was_sent_popup = "//div[@class='ComposeDoneScreen-Wrapper']"
        self.sent_mail_folder = "//div[@class='Folder-m__root--iLgY8 qa-LeftColumn-Folder' and " \
                                "@aria-label='Отправленные, папка']"
        self.mail_refresh_button = "//button[@aria-label='Проверить, есть ли новые письма' and @type='button']"
        self.loading_bar_100 = "//div[@class='js-loading-bar mail-LoadingBar'][contains(@style, 'width: 100')]"
        self.my_mail = "//span[@class='mail-MessageSnippet-FromText' and @title='valik-garkovenko@yandex.ru']"
        self.message_view_container = "//div[@class='react-message-view_container']"
        self.mail_delete_button_loaded = "//span[@class='mail-Toolbar-Item-Text js-toolbar-item-title " \
                                         "js-toolbar-item-title-delete']"
        self.mail_delete_button = "//div[@title='Удалить (Delete)' and @role='button']"
        self.income_mail_folder = "//div[@class='Folder-m__root--iLgY8 qa-LeftColumn-Folder'][contains(@aria-label, " \
                                  "'Входящие, папка')]"
        self.menu_button = "//div/a[@class='user-account user-account_left-name user-account_has-ticker_yes " \
                           "user-account_has-accent-letter_yes count-me legouser__current-account " \
                           "legouser__current-account i-bem']"
        self.menu_popup = "//div[@class='light-popup light-popup_autoclosable_yes light-popup_animated_yes " \
                          "legouser__popup i-bem light-popup_visible_yes']"
        self.exit_button = "//div//a[@role='link' and @aria-label='Выйти из аккаунта']"
        self.mail_notification = "//a[@class='mail_Notifications-Item-Wrap']"
        self.all_mails_box = "//div[@class='ns-view-container-desc mail-MessagesList js-messages-list']"

    def write_mail_click(self):
        self._is_visible(self.write_mail_button).click()

    def write_mail_load(self):
        self._is_visible(self.write_mail_popup)

    def write_mail_to(self, mail_to):
        self._is_visible(self.write_mail_to_input).send_keys(mail_to)

    def write_mail_theme(self, mail_theme):
        self._is_visible(self.write_mail_theme_input).send_keys(mail_theme)

    def write_mail_text(self, mail_text):
        self._is_visible( self.write_mail_text_input).send_keys(mail_text)

    def write_mail_send_click(self):
        self._is_visible(self.write_mail_send_button).click()

    def write_was_sent(self):
        self._is_visible(self. mail_was_sent_popup)

    def sent_mail_folder_click(self):
        self._is_visible(self.sent_mail_folder).click()

    def mail_refresh(self):
        self._is_visible(self.mail_refresh_button).click()
        self._is_visible(self.loading_bar_100)

    def sent_mail_open(self):
        try:
            self._is_clickable(self.my_mail).click()
        except StaleElementReferenceException:
            self._is_clickable(self.my_mail).click()

    def sent_mail_check(self):
        self._is_visible(self.message_view_container)

    def mail_delete(self):
        self._is_visible(self.mail_delete_button_loaded)
        self._is_visible(self.mail_delete_button).click()

    def income_mail_click(self):
        self._is_visible(self.income_mail_folder).click()

    def income_mail_open(self):
        try:
            self._is_clickable(self.my_mail).click()
        except StaleElementReferenceException:
            self._is_clickable(self.my_mail).click()

    def income_mail_check(self):
        self._is_visible(self.message_view_container)

    def mail_deleted(self):
        self._is_visible(self.all_mails_box)
        self._is_invisible(self.my_mail)

    def notification_check(self):
        self._is_invisible(self.mail_notification)

    def menu_click(self):
        try:
            self._is_clickable(self.menu_button).click()
        except ElementClickInterceptedException:
            time.sleep(3)
            self._is_clickable(self.menu_button).click()

    def menu_check(self):
        self._is_visible(self.menu_popup)

    def exit_click(self):
        self._is_clickable(self.exit_button).click()
