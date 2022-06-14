from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["platformName"] = "Android"
caps["appium:platformVershion"] = "11.0"
caps["appium:deviceName"] = "Android Emulator"
caps["appium:automationName"] = "Appium"
caps["appium:avd"] = "Pixel_5_API_30"
caps["appium:udid"] = "emulator-5554"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Phone")
el2.click()
driver.quit()
