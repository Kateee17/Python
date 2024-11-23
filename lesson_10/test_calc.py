import allure
import pytest
from selenium import webdriver


from calc import Calculator

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calc(driver):
    calc = Calculator(driver)
    calc.time("45")
    calc.seven()
    calc.plus()
    calc.eight()
    calc.equals()
    calc.result_test()

    allure.epic("калькулятор")
    allure.severity("blocker")
    allure.suite("Тесты на работу с калькулятором")
    allure.story("Выполнение математических операций на калькуляторе")
    allure.title("Сложение чисел на калькуляторе")
    allure.feature("CREATE")
    def test_calc():
        with allure.step("Открытие веб-страницы Chrome"):
            driver = webdriver.Сhrome(
                service=ChromeService(ChromeDriverManager().install())
            )
        with allure.step(
            "Создание переменной, которая хранит экземпляр класса CalculatorPage"
        ):
            calculator_page = CalculatorPage(driver)
        calculator_page.delay()
        calculator_page.sum_of_the_numbers()
        calculator_page.get_result()
        calculator_page.close_driver()
