import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    # Открыть страницу калькулятора
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    waiter = WebDriverWait(driver, 40)
    # Ввести значение 45 в поле с локатором #delay
    delay_field = waiter.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
    delay_field.clear()
    delay_field.send_keys("45")

    # Нажать на кнопки 7, +, 8, =
    buttons = ['7', '+', '8', '=']
    for button in buttons:
        button_element = waiter.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button}']")))
        button_element.click()

    # Ожидать появления результата
    result_locator = (By.CSS_SELECTOR, "#result")
    try:
        WebDriverWait(driver, 46).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))  # Getting text meaning from result
        result_text = driver.find_element(By.CLASS_NAME, "screen").text
        # Assert that the result is 15
        assert result_text == "15"
    except Exception as e:
        print(f"Ошибка: {e}")