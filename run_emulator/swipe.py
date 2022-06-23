from driver import EmulatorDriver
from appium.webdriver.common.touch_action import TouchAction

class Swipe(EmulatorDriver):
    def swipe(self, begin, end, duration=None):
        """Swipe from one point to another point, for an optional duration.
        :Args:
         - start_x - x-coordinate at which to start
         - start_y - y-coordinate at which to start
         - end_x - x-coordinate at which to stop
         - end_y - y-coordinate at which to stop
         - duration - (optional) time to take the swipe, in ms.
        :Usage:
            driver.swipe(800, 200, 800, 800)
        """
        start_x, start_y = begin
        end_x, end_y = end
        action = TouchAction()
        action.press(x=start_x, y=start_y)
        action.wait(ms=duration)
        action.move_to(x=end_x, y=end_y)
        action.release()
        action.perform()