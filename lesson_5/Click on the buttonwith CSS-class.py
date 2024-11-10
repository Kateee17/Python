from selenium import webdriver
from selenium.webdriver.common.by import By
# Открыть страницу
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")
#Кликнуть на синюю кнопку
#Найдем кнопку по классу "btn"
button = driver.find_element(By.CLASS_NAME, "btn")
button.click()
#Закрыть браузер
driver.quit()