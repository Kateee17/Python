"from" selenium.webdriver.common.byimport By "from" selenium.webdriver.support.uiimport WebDriverWait
"from" selenium.webdriver.supportimport expected_conditionsas EC class SlowCalculatorPage:
"def" __init__(self, driver):self.driver = driver
self.waiter = WebDriverWait(driver, 40)
"def" set_delay(self, delay): delay_field = self.waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
delay_field.clear()
delay_field.send_keys(delay)
"def" click_button(self, button): button_element = self.waiter.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button}']")))
button_element.click()
"def" get_result(self): result_locator = (By.CSS_SELECTOR, "#result")
"return" self.waiter.until(EC.presence_of_element_located(result_locator)).text