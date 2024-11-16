from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Функция для проверки цвета рамки поля
def get_border_color(element):
    return element.value_of_css_property('border-color')


# Основной тест
def test_form_submission():
    # Инициализация драйвера
    driver = webdriver.Chrome()  # Используйте Ваш драйвер, например Chrome
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Нажатие на кнопку Submit
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    # Явное ожидание, чтобы убедиться, что элементы загружены
    wait = WebDriverWait(driver, 10)

    # Проверка поля "Zip code", оно должно быть подсвечено красным
    zip_code_field = wait.until(EC.visibility_of_element_located((By.ID, "zip")))
    zip_code_color = get_border_color(zip_code_field)

    assert zip_code_color == 'rgb(255, 0, 0)'  # Проверка, что цвет рамки красный

    # Проверка остальных полей, они должны быть подсвечены зеленым
    fields = [
        (By.ID, "first-name"),
        (By.ID, "last-name"),
        (By.ID, "email")
    ]

    for by, value in fields:
        field = driver.find_element(by, value)
        field_color = get_border_color(field)
        assert field_color == 'rgb(0, 128, 0)'  # Проверка, что цвет рамки зеленый

    print("Все проверки пройдены успешно!")

    # Закрытие драйвера
    driver.quit()


# Запуск теста
if __name__ == "__main__":
    test_form_submission()