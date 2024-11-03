from selenium import webdriver
from selenium.webdriver.common.by import By
# Открыть страницу
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
# Кликнуть на синюю кнопку
# Найдем кнопку по ее тексту "Click Me!"
button = driver.find_element(By.XPATH, "//button[text()='Click Me!']")
button.click()
# Закрыть браузер
driver.quit()