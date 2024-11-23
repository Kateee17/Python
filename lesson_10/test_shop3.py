import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from shop import Shop

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_shop(driver):
    shop = Shop(driver)
    shop.login("standard_user")
    shop.password("secret_sauce")
    shop.input()
    shop.tovar1()
    shop.tovar2()
    shop.tovar3()
    shop.korzina()
    shop.knopka_checkout()
    shop.first_name("РђРЅРЅР°")
    shop.last_name("РџРµС‚СЂРѕРІР°")
    shop.postal_code("123456")
    shop.knopka_continue()
    text = shop.text()
    assert text == "Total: $58.29"

    @allure.story("Тестирование магазина")
    @allure.feature("Процесс покупки")
    def test_shop(driver):
        shop = Shop(driver)

        with allure.step("Логин пользователя"):
            shop.login("standard_user")
            shop.password("secret_sauce")
            shop.input()

        with allure.step("Добавление товаров в корзину"):
            allure.sub_step("Добавляем первый товар")
            shop.tovar1()
            allure.sub_step("Добавляем второй товар")
            shop.tovar2()
            allure.sub_step("Добавляем третий товар")
            shop.tovar3()

        with allure.step("Переход к корзине"):
            shop.korzina()
            shop.knopka_checkout()

        with allure.step("Заполнение данных для покупки"):
            shop.first_name("РђРЅРЅР°")
            shop.last_name("РџРµС‚СЂРѕРІР°")
            shop.postal_code("123456")
            shop.knopka_continue()

        with allure.step("Проверка текста на странице"):
            text = shop.text()
            assert text == "Total: $58.29", f"Ожидалось 'Total: $58.29', но получено '{text}'"