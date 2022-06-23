from appium.webdriver.common.touch_action import TouchAction


class Swipe:

    def swipe(self, begin, end, duration=None):
        """
            Swipe from one point to another point, for an optional duration.
            :Args:
                - start_x - x-coordinate at which to start
                - start_y - y-coordinate at which to start
                - end_x - x-coordinate at which to stop
                - end_y - y-coordinate at which to stop
                - duration - (optional) time to take the swipe, in ms.
            :Usage:
                self.driver.swipe(800, 200, 800, 800)
        """
        start_x, start_y = begin
        end_x, end_y = end
        action = TouchAction()
        action.press(x=start_x, y=start_y)
        action.wait(ms=duration)
        action.move_to(x=end_x, y=end_y)
        action.release()
        action.perform()

    def swipe_left(self):
        self.size = self.driver.get_window_size()
        start_x = self.size['width'] / 1.5
        start_y = self.size['height'] / 2
        end_x = start_x / 4
        end_y = start_y
        self.driver.swipe(start_x, start_y, end_x, end_y)

    def swipe_right(self):
        self.size = self.driver.get_window_size()
        start_x = self.size['width'] / 4
        end_x = self.size['width'] / 1.5
        start_y = self.size['height'] / 2
        end_y = start_y
        self.driver.swipe(start_x, start_y, end_x, end_y)

    def swipe_down(self):
        self.size = self.driver.get_window_size()
        start_x = self.size['width'] / 2
        end_x = start_x
        start_y = self.size['height'] / 1.5
        end_y = self.size['height'] / 4
        self.driver.swipe(start_x, start_y, end_x, end_y)

    def swipe_up(self):
        self.size = self.driver.get_window_size()
        start_x = self.size['width'] / 2
        end_x = start_x
        start_y = self.size['height'] / 4
        end_y = self.size['height'] / 1.5
        self.driver.swipe(start_x, start_y, end_x, end_y)
