import pytest
from selenium.common.exceptions import NoSuchElementException

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from test.functional.test_helper import wait_for_element

from .helper.test_helper import APIDEMO_PKG_NAME, BaseTestCase, is_ci


class TestTouchAction(BaseTestCase):
    def test_tap(self) -> None:
        el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Animation')
        action = TouchAction(self.driver)
        action.tap(el).perform()
        el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Bouncing Balls')
        assert el is not None

    def test_tap_x_y(self) -> None:
        el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Animation')
        action = TouchAction(self.driver)
        action.tap(el, 100, 10).perform()

        el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Bouncing Balls')
        assert el is not None

    @pytest.mark.skipif(condition=is_ci(), reason='Need to fix flaky test during running on CI.')
    def test_tap_twice(self) -> None:
        el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Text')
        action = TouchAction(self.driver)
        action.tap(el).perform()

        el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'LogTextBox')
        action.tap(el).perform()

        el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Add')
        action.tap(el, count=2).perform()

        els = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.TextView')
        assert 'This is a test\nThis is a test\n' == els[1].get_attribute("text")

    def test_press_and_immediately_release(self) -> None:
        el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Animation')
        action = TouchAction(self.driver)
        action.press(el).release().perform()

        el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Bouncing Balls')
        assert el is not None

    def test_press_and_immediately_release_x_y(self) -> None:
        el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Animation')
        action = TouchAction(self.driver)
        action.press(el, 100, 10).release().perform()

        el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Bouncing Balls')
        assert el is not None

    def test_press_and_wait(self) -> None:
        self._move_to_custom_adapter()
        action = TouchAction(self.driver)

        el = wait_for_element(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("People Names")')
        action.press(el).wait(2000).perform()

        # 'Sample menu' only comes up with a long press, not a press
        el = wait_for_element(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sample menu")')
        assert el is not None

    def test_press_and_moveto(self) -> None:
        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Content')
        el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Animation')

        action = TouchAction(self.driver)
        action.press(el1).move_to(el2).release().perform()

        el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Views')
        assert el is not None

    def test_press_and_moveto_x_y(self) -> None:
        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Content')
        el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='App')

        action = TouchAction(self.driver)
        action.press(el1).move_to(el2, 100, 100).release().perform()

        el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Views')
        assert el is not None

    def test_long_press(self) -> None:
        self._move_to_custom_adapter()
        action = TouchAction(self.driver)

        el = wait_for_element(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("People Names")')
        action.long_press(el).perform()

        # 'Sample menu' only comes up with a long press, not a tap
        el = wait_for_element(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sample menu")')
        assert el is not None

    @pytest.mark.skipif(condition=is_ci(), reason='Skip since this check is low robust due to hard-coded position.')
    def test_long_press_x_y(self) -> None:
        self._move_to_custom_adapter()
        action = TouchAction(self.driver)

        # the element "People Names" is located at 430:310 (top left corner)
        # location can be changed by phone resolusion, OS version
        action.long_press(x=430, y=310).perform()

        # 'Sample menu' only comes up with a long press, not a tap
        el = wait_for_element(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sample menu")')
        assert el is not None

    def test_drag_and_drop(self) -> None:
        self._move_to_views()
        action = TouchAction(self.driver)

        el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Drag and Drop')
        action.tap(el).perform()

        dd3 = wait_for_element(self.driver, AppiumBy.ID, '{}:id/drag_dot_3'.format(APIDEMO_PKG_NAME))
        dd2 = self.driver.find_element(by=AppiumBy.ID, value='{}:id/drag_dot_2'.format(APIDEMO_PKG_NAME))

        # dnd is stimulated by longpress-move_to-release
        action.long_press(dd3).move_to(dd2).release().perform()

        el = wait_for_element(self.driver, AppiumBy.ID, '{}:id/drag_result_text'.format(APIDEMO_PKG_NAME))
        assert 'Dropped!' in el.text

    def test_driver_drag_and_drop(self) -> None:
        self._move_to_views()
        action = TouchAction(self.driver)

        el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Drag and Drop')
        action.tap(el).perform()

        dd3 = wait_for_element(self.driver, AppiumBy.ID, '{}:id/drag_dot_3'.format(APIDEMO_PKG_NAME))
        dd2 = self.driver.find_element(by=AppiumBy.ID, value='{}:id/drag_dot_2'.format(APIDEMO_PKG_NAME))

        self.driver.drag_and_drop(dd3, dd2)

        el = wait_for_element(self.driver, AppiumBy.ID, '{}:id/drag_result_text'.format(APIDEMO_PKG_NAME))
        assert 'Dropped!' in el.text

    def test_driver_swipe(self) -> None:
        el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views')
        action = TouchAction(self.driver)
        action.tap(el).perform()

        with pytest.raises(NoSuchElementException):
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='ImageView')

        self.driver.swipe(100, 1000, 100, 100, 800)
        el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'ImageView')
        assert el is not None

    def _move_to_views(self) -> None:
        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Content')
        el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Animation')
        self.driver.scroll(el1, el2)

        el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Views')
        action = TouchAction(self.driver)
        action.tap(el).perform()

    def _move_to_custom_adapter(self) -> None:
        self._move_to_views()
        action = TouchAction(self.driver)

        el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, 'Expandable Lists')
        action.tap(el).perform()

        el = wait_for_element(self.driver, AppiumBy.ACCESSIBILITY_ID, '1. Custom Adapter')
        action.tap(el).perform()

        # !!!!!

        from appium.webdriver.common.touch_action import TouchAction
        from AppiumLibrary import ElementFinder
        from .keywordgroup import KeywordGroup

        class _TouchKeywords(KeywordGroup):

            def __init__(self):
                self._element_finder = ElementFinder()

            # Public, element lookups
            def zoom(self, locator, percent="200%", steps=1):
                """
                Zooms in on an element a certain amount.
                """
                driver = self._current_application()
                element = self._element_find(locator, True, True)
                driver.zoom(element=element, percent=percent, steps=steps)

            def pinch(self, locator, percent="200%", steps=1):
                """
                Pinch in on an element a certain amount.
                """
                driver = self._current_application()
                element = self._element_find(locator, True, True)
                driver.pinch(element=element, percent=percent, steps=steps)

            def swipe(self, start_x, start_y, offset_x, offset_y, duration=1000):
                """
                Swipe from one point to another point, for an optional duration.

                Args:
                 - start_x - x-coordinate at which to start
                 - start_y - y-coordinate at which to start
                 - offset_x - x-coordinate distance from start_x at which to stop
                 - offset_y - y-coordinate distance from start_y at which to stop
                 - duration - (optional) time to take the swipe, in ms.

                Usage:
                | Swipe | 500 | 100 | 100 | 0 | 1000 |

                *!Important Note:* Android `Swipe` is not working properly, use ``offset_x`` and ``offset_y``
                as if these are destination points.
                """
                driver = self._current_application()
                driver.swipe(start_x, start_y, offset_x, offset_y, duration)

            def scroll(self, start_locator, end_locator):
                """
                Scrolls from one element to another
                Key attributes for arbitrary elements are `id` and `name`. See
                `introduction` for details about locating elements.
                """
                el1 = self._element_find(start_locator, True, True)
                el2 = self._element_find(end_locator, True, True)
                driver = self._current_application()
                driver.scroll(el1, el2)

            def scroll_down(self, locator):
                """Scrolls down to element"""
                driver = self._current_application()
                element = self._element_find(locator, True, True)
                driver.execute_script("mobile: scroll", {"direction": 'down', 'element': element.id})

            def scroll_up(self, locator):
                """Scrolls up to element"""
                driver = self._current_application()
                element = self._element_find(locator, True, True)
                driver.execute_script("mobile: scroll", {"direction": 'up', 'element': element.id})

            def long_press(self, locator):
                """ Long press the element """
                driver = self._current_application()
                element = self._element_find(locator, True, True)
                long_press = TouchAction(driver).long_press(element)
                long_press.perform()

            def tap(self, locator):
                """ Tap on element """
                driver = self._current_application()
                el = self._element_find(locator, True, True)
                action = TouchAction(driver)
                action.tap(el).perform()

            def click_a_point(self, x=0, y=0, duration=100):
                """ Click on a point"""
                self._info("Clicking on a point (%s,%s)." % (x, y))
                driver = self._current_application()
                action = TouchAction(driver)
                try:
                    action.press(x=float(x), y=float(y)).wait(float(duration)).release().perform()
                except:
                    assert False, "Can't click on a point at (%s,%s)" % (x, y)

            def click_element_at_coordinates(self, coordinate_X, coordinate_Y):
                """ click element at a certain coordinate """
                self._info("Pressing at (%s, %s)." % (coordinate_X, coordinate_Y))
                driver = self._current_application()
                action = TouchAction(driver)
                action.press(x=coordinate_X, y=coordinate_Y).release().perform()
