from selenium import webdriver
from selenium.webdriver.common.by import By
# Открыть страницу
driver = webdriver.Chrome()  # Замените на ваш браузер
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
# Кликнуть на кнопку "Add Element" 5 раз
add_button = driver.find_element(By.CSS_SELECTOR, "#content > button")
for _ in range(5):
    add_button.click()
# Собрать список кнопок "Delete"
delete_buttons = driver.find_elements(By.CSS_SELECTOR, "#elements > button")
# Вывести размер списка
print(f"Размер списка кнопок 'Delete': {len(delete_buttons)}")
# Закрыть браузер
driver.quit()