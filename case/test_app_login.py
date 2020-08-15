#导包
import unittest
from base.driver import GetDriver


#引用log日志器
from page.app_page import Page
from tools.get_logger import GetLogger
log =GetLogger().get_logger()


class TestLogin(unittest.TestCase):

    # 用例前置条件：在执行用例之前执行，每条用例都要执行一次
    def setUp(self):
        # 获取driver
        self.driver = GetDriver().get_app_driver()
        # login页面实例化
        self.login = Page(self.driver)
        # 启动页处理
        self.login.Login.page_start()

    # 用例后置处理：执行完用例之后执行，每条用例都要执行一次
    def tearDown(self):
        # 关闭driver
        GetDriver().quit_driver()

    # 测试用例：登录成功
    def test_Login_success(self):
        self.login.Login.page_login("9520190619","789789")
        self.assertIn(self.login.Login.page_get_balance_info(),"可用余额")

if __name__ == '__main__':
    unittest.main()