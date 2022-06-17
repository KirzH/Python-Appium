from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy


class Calculator:
    def __init__(self, driver):
        self.driver = driver
        self.eq = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            MobileBy.ID, 'my.android.calc:id/b044'
        )))
        self.equals = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            MobileBy.ID, 'my.android.calc:id/b044'
        )))
        self.delete = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            MobileBy.ID, 'my.android.calc:id/b013'
        )))
        self.multiply = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            MobileBy.ID, 'my.android.calc:id/b023'
        )))
        self.minus = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            MobileBy.ID, 'my.android.calc:id/b033'
        )))
        self.plus = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            MobileBy.ID, 'my.android.calc:id/b043'
        )))


    def final_result(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            MobileBy.ID, 'my.android.calc:id/b044'
        ))).text

    def checkNumArgs(self, numbers):
        if (len(numbers) < 2):
            raise Exception("Minimum of 2 numbers!")

    def clicknumber(self, number):
        _num = str(number)
        for char in _num:
            if (char == '.'):
                self.dec_point.click()
            else:
                num_id = 'my.android.calc:id/' + char
                self.driver.find_element(MobileBy.ID, num_id).click()

    def sum(self, *args):
        self.checkNumArgs(args)
        result = 0

        for i, num in enumerate(args):
            self.clicknumber(num)
            result += num
            if i < len(args) - 1:
                self.plus.click()

        self.eq.click()
        calc_result = float(self.final_result())
        assert result == calc_result, 'Different results for sum'

    def multiplying(self, *args):
        self.checkNumArgs(args)
        result = 1

        for i, num in enumerate(args):
            self.clicknumber(num)
            result = result * num
            if i < len(args) - 1:
                self.multiply.click()

        self.eq.click()
        calc_result = float(self.final_result())
        assert result == calc_result, 'Different results for multiplication'

    def dividing(self, *args):
        self.checkNumArgs(args)
        result = args[0]

        for i, num in enumerate(args):
            self.clicknumber(num)

            if i > 0:
                result = result / num

            if i < len(args) - 1:
                self.divide.click()

        self.eq.click()
        calc_result = float(self.final_result())
        assert result == calc_result, 'Different results for division'
