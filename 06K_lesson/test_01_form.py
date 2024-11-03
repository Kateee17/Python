from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создаем экземпляр драйвера
driver = webdriver.Chrome() try:
# Открываем страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
# Заполняем форму
driver.find_element(By.NAME, "firstname").send_keys("Иван")
driver.find_element(By.NAME, "lastname").send_keys("Петров")
driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
driver.find_element(By.NAME, "email").send_keys("test@skypro.com")
driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
driver.find_element(By.NAME, "zipcode").send_keys("")  # Оставляем пустым
driver.find_element(By.NAME, "city").send_keys("Москва")
driver.find_element(By.NAME, "country").send_keys("Россия")
driver.find_element(By.NAME, "job").send_keys("QA")
driver.find_element(By.NAME, "company").send_keys("SkyPro")
# Нажимаем кнопку Submit
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Ожидаем, пока форма будет обработана и элементы станут видимыми
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "form")))

# Проверяем, что поле Zip code подсвечено красным
zip_code_field = driver.find_element(By.NAME, "zipcode")
assert "border-color: red" in zip_code_field.get_attribute("style"), "Zip code field is not highlighted in red"

# Проверяем, что остальные поля подсвечены зеленым
fields = ["firstname", "lastname", "address", "email", "phone", "city", "country", "job", "company"]
for field in fields:
input_field = driver.find_element(By.NAME, field)
assert "border-color: green" in input_field.get_attribute("style"), f"{field} field is not highlighted in green"

finally:
# Закрываем драйвер
driver.quit()