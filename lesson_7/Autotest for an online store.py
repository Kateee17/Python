"import pytest
fromseleniumimport webdriver
fromselenium.webdriver.common.byimport By
fromselenium.webdriver.support.uiimport WebDriverWait
fromselenium.webdriver.supportimport expected_conditionsas EC
fromselenium.common.exceptionsimport TimeoutExceptiondef test_saucedemo_checkout():
# Инициализация драйвера (замените на Ваш путь к драйверу)
"driver = webdriver.Chrome()"
# или webdriver.Firefox(), etc. try:
# 1. Откройте сайт магазина
"driver.get("https://www.saucedemo.com/")"
# 2. Авторизация
"driver.find_element(By.ID, "user-name").send_keys("standard_user")"
"driver.find_element(By.ID, "password").send_keys("secret_sauce")"
"driver.find_element(By.ID, "login-button").click()"
# 3. Добавление товаров в корзину
"backpack = "driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
"tshirt = "driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
"onesie = "driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
backpack.click()
tshirt.click()
onesie.click()
# 4. Переход в корзину
"driver.find_element(By.ID, "shopping_cart_container").click()"
# 5. Нажмите Checkout
"driver.find_element(By.ID, "checkout").click()"
# 6. Заполнение формы (замените на Ваши данные)
"driver.find_element(By.ID, "first-name").send_keys("John")"
"driver.find_element(By.ID, "last-name").send_keys("Doe")"
"driver.find_element(By.ID, "postal-code").send_keys("12345")"
# 7. Нажмите кнопку Continue
"driver.find_element(By.ID, "continue").click()"
# 8. Прочтите итоговую стоимость
"total = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text"
# 9. Проверка итоговой суммы
asserttotal == "$58.29"
exceptTimeoutException:
print("TimeoutException: Element not found within the timeout period.")
pytest.fail("Test failed due to timeout.")
exceptExceptionase: (print(f"An error occurred:{e}"))
pytest.fail(f"Test failed:{e}")
"finally":
# Закрытие браузера
driver.quit()