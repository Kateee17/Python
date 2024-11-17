import pytest
from selenium import webdriver
from form import Form

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_form(driver):
    form = Form(driver)
    form.name("РРІР°РЅ")
    form.surname("РџРµС‚СЂРѕРІ")
    form.address("Р›РµРЅРёРЅР°, 55-3")
    form.email("test@skypro.com")
    form.phone_number("+7985899998787")
    form.zip_code("")
    form.city("РњРѕСЃРєРІР°")
    form.country("Р РѕСЃСЃРёСЏ")
    form.job_position("QA")
    form.company("SkyPro")
    form.knopka_submit()
    form.danger_color()
    form.success_color()