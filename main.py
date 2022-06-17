from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "HUAWEI P smart",
    "automationName": "UiAutomator2",
    "udid": "XED4C18207053961",
    "noReset": "true",
    "app": "C:\\Users\\User\\Desktop\\mobilCalculatorApp.apk",
    "appPackage": "my.android.calc",
    "appActivity": "my.android.calc.MainActivity"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_capabilities)

driver.implicitly_wait(5)
driver.find_element(By.ID, 'my.android.calc:id/b003').click()
driver.find_element(By.ID, 'my.android.calc:id/b011').click()
driver.find_element(By.ID, 'my.android.calc:id/b012').click()
driver.find_element(By.ID, 'my.android.calc:id/b023').click()
driver.find_element(By.ID, 'my.android.calc:id/b030').click()
driver.find_element(By.ID, 'my.android.calc:id/b040').click()
driver.find_element(by=AppiumBy.ID, value='my.android.calc:id/b044').click()
driver.back()


