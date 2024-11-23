import pytest
from selenium import webdriver
from form import Form

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
def test_form(driver):
    form = Form(driver)
    form.name("РРІР°РЅ")
    form.surname("РџРµС‚СЂРѕРІ")
    form.address("Р›РµРЅРёРЅР°, 55-3")
    form.email("test@skypro.com")
    form.phone_number("+7985899998787")
    form.zip_code("")
    form.city("РњРѕСЃРєРІР°")
    form.country("Р РѕСЃСЃРёСЏ")
    form.job_position("QA")
    form.company("SkyPro")
    form.knopka_submit()
    form.danger_color()
    form.success_color()

    @allure.story("Тестирование формы подачи заявки")
    @allure.title("Форма должна корректно принимать входные данные")
    def test_form(driver):
        form = Form(driver)

        with allure.step("Заполнение полей формы"):
            form.name("Иван")
            form.surname("Петров")
            form.address("Ленинская, 55-3")
            form.email("test@skypro.com")
            form.phone_number("+7985899998787")
            form.zip_code("")
            form.city("Москва")
            form.country("Россия")
            form.job_position("QA")
            form.company("SkyPro")

        with allure.step("Отправка формы"):
            form.knopka_submit()

        with allure.step("Проверка цвета ошибки"):
            form.danger_color()

        with allure.step("Проверка цвета успешного результата"):
            form.success_color()