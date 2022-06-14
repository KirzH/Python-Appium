from appium import webdriver
from selenium.webdriver.common.by import By

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "11",
    "deviceName": "Pixel 5 API 30",
    "appActivities": "myAPP",
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_capabilities)

driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="Phone"]').click()
