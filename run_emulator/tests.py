from selenium.webdriver.common.by import By
from driver import EmulatorDriver
from swipe import Swipe
import time


class BaseTests(EmulatorDriver, Swipe):

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

    def test_swipe(self):
        self.driver.find_element(By.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow/android.widget.LinearLayout/android.widget.TextView').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[4]').click()
        self.driver.swipe('760', '1900', '760', '500', 2000)
        self.driver.swipe('800', '800', '200', '800')

    def test_swipe_left(self):
        self.driver.find_element(By.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow/android.widget.LinearLayout/android.widget.TextView').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[4]').click()
        time.sleep(2)
        self.swipe_left()
        self.swipe_right()
        self.swipe_down()
        self.swipe_up()