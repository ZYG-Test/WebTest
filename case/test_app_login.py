#导包
import unittest
from base.appDriver import appDriver

#引用log日志器
from page.page import Page
from tools.get_logger import GetLogger
log =GetLogger().get_logger()


class TestLogin(unittest.TestCase):

    # 用例前置条件：在执行用例之前执行，每条用例都要执行一次
    def setUp(self):
        # 获取driver
        self.driver = appDriver().get_app_driver()
        # login页面实例化
        self.login = Page(self.driver)
        # 启动页处理
        self.login.AppLogin.page_start()

    # 用例后置处理：执行完用例之后执行，每条用例都要执行一次
    def tearDown(self):
        # 退出登录
        self.login.AppMe.page_click_loginout()
        # 关闭driver
        appDriver().quit_driver()

    # 测试用例：登录成功
    def test_Login_success(self):
        self.login.AppLogin.page_login_success("9520190619","789789")
        self.assertIn(self.login.AppLogin.page_get_balance_info(),"可用余额")

if __name__ == '__main__':
    unittest.main()