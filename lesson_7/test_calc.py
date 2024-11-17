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