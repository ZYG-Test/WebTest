from appium import webdriver

class appDriver:
    driver = None


    # 获取app driver
    @classmethod
    def get_app_driver(cls):
        # Capability配置
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'emulator-5554'
        # desired_caps['deviceName'] = '8763dc5d'
        desired_caps['appPackage'] = 'com.zybitech.juancash'
        desired_caps['appActivity'] = 'com.zybitech.juancash.ui.act.SplashScreenActivity'
        desired_caps['autoGrantPermissions'] = True
        # 启动appium
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        return driver

    #关闭driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver=None

if __name__ == '__main__':
    driver= appDriver()
    driver.get_app_driver()
    driver.quit_driver()
