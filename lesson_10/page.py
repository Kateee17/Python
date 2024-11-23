from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time

class CalculatorPage:
def __init__(self, driver: WebDriver):
        """
        Инициализация класса страницы калькулятора

        :param driver: Драйвер Selenium (WebDriver)
        """
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.seven_button = (By.CSS_SELECTOR, "button[value='7']")
        self.plus_button = (By.CSS_SELECTOR, "button[value='+']")
        self.eight_button = (By.CSS_SELECTOR, "button[value='8']")
        self.equals_button = (By.CSS_SELECTOR, "button[value='=']")
        self.result_display = (By.CSS_SELECTOR, "#result")

def set_delay(self, delay: int) -> None:
        """
        Устанавливает значение задерж        :param delay: Задержка в секундах (целое число)
        :return: None
        """
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(delay))

def click_button(self, button_selector: tuple) -> None:
        """
        Кликает по кнопке калькулятора

        :param button_selector: Локатор кнопки (кортеж)
        :return: None
        """
        button = self.driver.find_element(*button_selector)
        button.click()

def get_result(self) -> str:
        """
        Получает результат вычисления

        :return: Результат (строка)
        """
        result = self.driver.find_element(*self.result_display)
        return result.text

def calculate(self, delay: int) -> str:
        """
        Выполняет вычисление с заданной задержкой

        :param delay: Задержка в секундах (целое число)
        :return: Результат (строка)
        """
        self.set_delay(delay)
        time.sleep(delay)  # Ждет указанное время
        self.click_button(self.seven_button)
        self.click_button(self.plus_button)
        self.click_button(self.eight_button)
        self.click_button(self.equals_button)
        return self.get_result()