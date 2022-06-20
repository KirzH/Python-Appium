import os
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.appium_service import AppiumService


class EmulatorCalculatorTest(unittest.TestCase):

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

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_capabilities)

    def test_multiplication(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.find_element(By.ID, 'my.android.calc:id/b003').click()
        driver.find_element(By.ID, 'my.android.calc:id/b011').click()
        driver.find_element(By.ID, 'my.android.calc:id/b012').click()
        driver.find_element(By.ID, 'my.android.calc:id/b023').click()
        driver.find_element(By.ID, 'my.android.calc:id/b030').click()
        driver.find_element(By.ID, 'my.android.calc:id/b040').click()
        driver.find_element(By.ID, 'my.android.calc:id/b044').click()

        cal_numb = driver.find_element(By.ID, 'my.android.calc:id/input').text
        assert '890' in cal_numb, f'expected number to be {cal_numb}'

    def tearDown(self):
        self.driver.close_app()
        self.appium_service.stop()
        os.system("adb -s emulator-5554 emu kill")

    if __name__ == "__main__":
        unittest.main()