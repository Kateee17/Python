from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Основной тест
def test_form_submission():
    # Инициализация драйвера
    driver = webdriver.Chrome()  # Используйте Ваш драйвер, например Chrome
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    (driver.find_element(By.NAME, "first-name").send_keys("Иван"))
    # Заполнить поле Last name
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    # Заполнить поле Address
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    # Заполнить поле E-mail
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    # Заполнить поле Phone number
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    # Заполнить поле City
    driver.find_element(By.NAME, "city").send_keys("Москва")
    # Заполнить поле Country
    driver.find_element(By.NAME, "country").send_keys("Россия")
    # Заполнить поле Job position
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    # Заполнить поле Company
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    # Нажатие на кнопку Submit
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    # Явное ожидание, чтобы убедиться, что элементы загружены
    wait = WebDriverWait(driver, 10)

    assert "danger" in driver.find_element(By.ID, "zip-code").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "first-name").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "last-name").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "address").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "e-mail").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "phone").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "city").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "country").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "job-position").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "company").get_attribute("class")
    driver.quit ()