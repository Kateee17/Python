import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SauceDemoTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Или другой браузер
        self.driver.implicitly_wait(10) #явное ожидание

    def test_checkout(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        # Авторизация
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Добавление товаров в корзину
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        # Переход в корзину
        driver.find_element(By.ID, "shopping_cart_container").click()

        # Checkout
        driver.find_element(By.ID, "checkout").click()

        # Заполнение формы (замените на Ваши данные)
        driver.find_element(By.ID, "first-name").send_keys("John")
        driver.find_element(By.ID, "last-name").send_keys("Doe")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()


        # Получение итоговой стоимости
        try:
            total_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
            )
            total = total_element.text
        except TimeoutException:
            self.fail("Итоговая стоимость не найдена")

        # Проверка итоговой суммы
        self.assertEqual(total, "$58.29")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()