importpytest
fromseleniumimport webdriver
fromselenium.webdriver.common.byimport By
fromselenium.webdriver.support.uiimport WebDriverWait
fromselenium.webdriver.supportimport expected_conditionsas EC @pytest.fixturedef "driver():driver=webdriver.Chrome()
#Или другой браузер, например, webdriver.Firefox()
yielddriver driver.quit()
deftest_form_submission(driver):driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
#Заполнение формы
"driver.find_element(By.ID, "first-name").send_keys("Иван")
"driver.find_element(By.ID, "last-name").send_keys("Петров")
"driver.find_element(By.ID, "address").send_keys("Ленина, 55-3")
"driver.find_element(By.ID, "email").send_keys("test@skypro.com")
"driver.find_element(By.ID, "phone").send_keys("+7985899998787")
"driver.find_element(By.ID, "city").send_keys("Москва")
"driver.find_element(By.ID, "country").send_keys("Россия")
"driver.find_element(By.ID, "job-position").send_keys("QA")
"driver.find_element(By.ID, "company").send_keys("SkyPro")
# Нажатие кнопки Submit
driver.find_element(By.ID, "submit").click()
# Проверки
# Для проверки цвета лучше использовать CSS-селекторы, которые указывают на класс, отвечающий за цвет.
#  Предполагаем, что классы "is-invalid" и "is-valid"  определяют красный и зеленый цвет соответственно.
#  Если это не так, замените селекторы на корректные.zip_code_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "zip-code")))
"assert""is-invalid" inzip_code_field.get_attribute("class"), "Zip code field is not red"
first_name_field = driver.find_element(By.ID, "first-name")
"assert""is-valid" infirst_name_field.get_attribute("class"), "First name field is not green"
last_name_field = driver.find_element(By.ID, "last-name")
"assert""is-valid" inlast_name_field.get_attribute("class"), "Last name field is not green"
address_field = driver.find_element(By.ID, "address")
"assert""is-valid" inaddress_field.get_attribute("class"), "Address field is not green"
email_field = driver.find_element(By.ID, "email")
"assert""is-valid" inemail_field.get_attribute("class"), "Email field is not green"
"phone_field = driver.find_element(By.ID, "phone")
"assert""is-valid" inphone_field.get_attribute("class"), "Phone field is not green"
city_field = driver.find_element(By.ID, "city")
"assert""is-valid" incity_field.get_attribute("class"), "City field is not green"
country_field = driver.find_element(By.ID, "country")
"assert""is-valid" incountry_field.get_attribute("class"), "Country field is not green"
job_position_field = driver.find_element(By.ID, "job-position")
"assert""is-valid" injob_position_field.get_attribute("class"), "Job position field is not green"
company_field = driver.find_element(By.ID, "company")
"assert""is-valid" incompany_field.get_attribute("class"), "Company field is not green"