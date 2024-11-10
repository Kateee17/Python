from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutExceptiondr= webdriver.Chrome()
#илидругойдрайвер
# driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
#Введитезадержку
# delay_field = (driver.find_element(By.ID, "delay"))
# delay_field.send_keys("45")
#Нажмитекнопки
# driver.find_element(By.ID, "number7").click()
# driver.find_element(By.ID, "plus").click()
# driver.find_element(By.ID, "number8").click()
# driver.find_element(By.ID, "equal").click()
try: #Ожиданиерезультатастаймаутом60секунд WebDriverWait(driver,60).until(EC.text_to_be_present_in_element((By.ID, "result"), "15"))
# result = (driver.find_element(By.ID, "result").text)
# assert result == "15", f"Ожидаемый результат 15,а получено":{result}"
print("Тест пройден успешно!")
exceptTimeoutException: print("Тест провален: Результат не появился в течение 60 секунд.")
exceptExceptionase: print(f"Произошлаошибка:{e}")
finally:driver.quit()
