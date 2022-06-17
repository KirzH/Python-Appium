import unittest
from calculator_test.pages.calc import Calculator
from appium import webdriver


class CalculatorTests(unittest.TestCase):

    def setUp(self):
        run_locally = False
        desired_caps = {}
        if run_locally:
            desired_caps["platformName"] = "Android"
            desired_caps["platformVersion"] = "9"
            desired_caps["deviceName"] = "HUAWEI P smart"
            desired_caps["automationName"] = "UiAutomator2"
            desired_caps["udid"] = "XED4C18207053961"
            desired_caps["app"] = "C:\\Users\\User\\Desktop\\mobilCalculatorApp.apk"
            desired_caps["appPackage"] = "my.android.calc"
            desired_caps["appActivity"] = "my.android.calc.MainActivity"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.calculator = Calculator(self.driver)

    def test_sum_numbers(self):
        self.calculator.sum(1, 2, 3)


    def tearDown(self):
        self.driver.back()


if __name__ == "__main__":
    unittest.main()
