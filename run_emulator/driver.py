import os
import unittest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService


class EmulatorDriver(unittest.TestCase):
    def __int__(self, driver, appium_service):
        self.driver = driver

    def setUp(self):
        self.desired_capabilities = {
            "platformName": "Android",
            "platformVersion": "11",
            "avd": "Pixel_5_API_30",
            "automationName": "UiAutomator2",
            "udid": "emulator-5554",
            "noReset": "true",
            "app": "C:\\Users\\User\\Desktop\\mobilCalculatorApp.apk",
            "appPackage": "my.android.calc",
            "appActivity": "my.android.calc.MainActivity"
        }
        self.appium_service = AppiumService()
        self.appium_service.start()

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_capabilities)
        driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.close_app()
        self.appium_service.stop()
        os.system("adb -s emulator-5554 emu kill")