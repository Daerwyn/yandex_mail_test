import pytest
from pom.main_page import MainPage
from pom.home_page import HomePage


@pytest.mark.usefixtures('setup')
class TestMailCycle:

    def test_log_in(self, ui):
        ui.main_page.log_in()

    def test_mail_create(self, ui):
        mail_create = HomePage(self.driver)
        mail_create.write_mail_click()  # Нажимаем на кнопку "Написать"
        mail_create.write_mail_to("valik-garkovenko@yandex.ru")  # Заполняем поле "Кому"
        mail_create.write_mail_theme(mail_create.text_generate(10))  # Заполняем поле "Тема"
        mail_create.write_mail_text(mail_create.text_generate(300))  # Пишем письмо
        mail_create.write_mail_send_click()  # Нажимаем на кнопку "Отправить"
        mail_create.write_was_sent()  # Проверяем наличие окна "Письмо отправлено"

    def test_mail_check(self):
        mail_check = HomePage(self.driver)
        mail_check.sent_mail_folder_click()  # Открываем вкладку "Отправленные"
        mail_check.mail_refresh()  # Нажимаем кнопку "Проверить, есть ли новые письма"
        mail_check.sent_mail_open()  # Открываем отправленное письмо
        mail_check.sent_mail_check()  # Проверяем, открылось ли письмо
        mail_check.mail_delete()  # Удаляем отправленное письмо
        mail_check.mail_deleted()  # Проверяем, что отправленное письмо удалено
        mail_check.income_mail_click()  # Открываем папку "Входящие"
        mail_check.income_mail_open()  # Открываем входящее письмо
        mail_check.income_mail_check()  # Проверяем, открылось ли письмо
        mail_check.mail_delete()  # Удаляем входящее письмо
        mail_check.mail_deleted()  # Проверяем, что входящее письмо удалено

    def test_log_out(self):
        validation = MainPage(self.driver)
        log_out = HomePage(self.driver)
        log_out.menu_click()  # Нажимаем на кнопку меню
        log_out.menu_check()  # Проверяем, что открылось всплывающее окно
        log_out.exit_click()  # Нажимаем кнопку "Выйти из сервисов Яндекса"
        validation.mainpage_validation()  # Проверяем, что мы на главной странице
