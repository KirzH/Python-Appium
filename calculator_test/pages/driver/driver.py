from appium import webdriver


class Driver:
    def __init__(self, **kwargs):
        self.caps = {}
        self.caps["platformName"] = "Android"
        self.caps["platformVersion"] = "9"
        self.caps["deviceName"] = "HUAWEI P smart"
        self.caps["automationName"] = "UiAutomator2"
        self.caps["udid"] = "XED4C18207053961"
        self.caps["noReset"] = True
        self.caps["app"] = "C:\\Users\\User\\Desktop\\mobilCalculatorApp.apk"
        self.caps["appPackage"] = "my.android.calc"
        self.caps["appActivity"] = "my.android.calc.MainActivity"

        for key, value in kwargs.items():
            self.caps[str(key)] = value
            print(str(key) + "changed to" + value)

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.caps)
