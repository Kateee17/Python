import pytest
from selenium import webdriver

class TestCalculator:
    @pytest.fixture
def setup(self):
        """
        Фикстура для настройки Selenium WebDriver

        :return: Объект драйвера
        """
        driver = webdriver.Chrome()
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        yield driver
        driver.quit()

def test_calculator(self, setup):
        """
        Тест для проверки работы калькулятора

        :param setup: Установленный драйвер (WebDriver)
        :return: None
        """
        calculator_page = CalculatorPage(setup)
        result = calculator_page.calculate(45)
        assert result == "15", f"Ожидалось '15', но получено '{result}'"