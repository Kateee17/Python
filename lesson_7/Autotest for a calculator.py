import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# Исправлено: Time на TimeoutException
@pytest.mark.parametrize ("delay", [45])
# Добавлено: параметризация для теста
def: test_slow_calculator(delay):
# Исправлено: добавлен пробел между def и именем функции driver = webdriver.Chrome()
# или другой браузер
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html") (delay_field = driver.find_element(By.ID,"delay")
delay_field.clear()
delay_field.send_keys(str(delay))
# Приведение к строке для корректной передачи значения
driver.find_element(By.ID, "number7").click()
driver.find_element(By.ID, "plus").click()
driver.find_element(By.ID, "number8").click()
driver.find_element(By.ID, "equal").click()
    try:
# Ожидаем появления результата с небольшой задержкой
WebDriverWait(driver, 50).until(EC.text_to_be_present_in_element((By.ID, "result"), "15"))  # Раскомментировано result=driver.find_element(By.ID, "result").text assertresult== "15"  # Исправлено: добавлен пробел между assert и условием
except TimeoutException:
# Исправлено: добавлен пробел между except и именем исключения
assert False, "Результат не появился в течение 50 секунд"
# Исправлено: добавлен пробел между assert и условием
 finally:driver.quit()  # Исправлено: добавлен пробел перед вызовом метод