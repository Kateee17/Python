import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import Timeou
def test_slow_calculator():
driver = webdriver.Chrome() # или другой браузер
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
delay_field = driver.find_element(By.ID, "delay")
delay_field.clear()
delay_field.send_keys("45")
driver.find_element(By.ID, "number7").click()
driver.find_element(By.ID, "plus").click()
driver.find_element(By.ID, "number8").click()
driver.find_element(By.ID, "equal").click()
try:
# Ожидаем появления результата с небольшой задержкой
# WebDriverWait(driver, 50).until(EC.text_to_be_present_in_element((By.ID, "result"), "15"))
result = driver.find_element(By.ID, "result").text
assert result == "15"
except TimeoutException:
assert False, "Результат не появился в течение 50 секунд"
finally:
driver.quit()
