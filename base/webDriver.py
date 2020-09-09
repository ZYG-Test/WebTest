from selenium import webdriver
import page

class webDriver:
    driver = None

    # 获取 driver
    @classmethod
    def get_web_driver(cls):
        if cls.driver is None:
            #启动浏览器
            # cls.driver = webdriver.PhantomJS()
            cls.driver = webdriver.Chrome()
            # cls.driver = webdriver.Firefox(executable_path='C:\Python\geckodriver-firefox57.exe')
            #浏览器最大化
            cls.driver.maximize_window()
            #打开url
            cls.driver.get(page.URL)
        #返回driver
        return cls.driver



    #关闭driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver=None

if __name__ == '__main__':
    driver= webDriver()
    driver.get_web_driver()
    driver.quit_driver()

