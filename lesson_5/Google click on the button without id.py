from selenium import webdriver
from selenium.webdriver.common.by import By
#Открытьстраницу
driver = webdriver.Chrome()
#Заменитенавашбраузер
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
#Кликнутьнакнопку"Add Element"5раз
add_button = driver.find_element(By.CSS_SELECTOR, "#content > button")
for_in range(5): add_button.click()
#Собратьсписоккнопок"Delete"
delete_buttons = driver.find_elements(By.CSS_SELECTOR, "#elements > button")
#Вывестиразмерсписка
print(f"Размер списка кнопок 'Delete':"{len(delete_buttons)}")
#Закрытьбраузер
driver.quit()