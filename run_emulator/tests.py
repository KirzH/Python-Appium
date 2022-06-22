import pytest
from selenium.webdriver.common.by import By
from driver import EmulatorDriver


class Tests(EmulatorDriver):

    def test_multiplication(self):
        self.driver.find_element(By.ID, 'my.android.calc:id/b003').click()
        self.driver.find_element(By.ID, 'my.android.calc:id/b011').click()
        self.driver.find_element(By.ID, 'my.android.calc:id/b012').click()
        self.driver.find_element(By.ID, 'my.android.calc:id/b023').click()
        self.driver.find_element(By.ID, 'my.android.calc:id/b030').click()
        self.driver.find_element(By.ID, 'my.android.calc:id/b040').click()
        self.driver.find_element(By.ID, 'my.android.calc:id/b044').click()

        cal_numb = self.driver.find_element(By.ID, 'my.android.calc:id/input').text
        assert '890' in cal_numb, f'expected number to be {cal_numb}'
