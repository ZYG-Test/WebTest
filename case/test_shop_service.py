#导包
import unittest
from base.webDriver import webDriver


#引用log日志器
from page.page import Page
from tools.get_logger import GetLogger
log =GetLogger().get_logger()


class TestServices(unittest.TestCase):

    # 用例前置条件：在执行用例之前执行，每条用例都要执行一次
    def setUp(self):
        # 获取driver
        self.driver = webDriver().get_web_driver()
        # login页面实例化
        self.services = Page(self.driver)
        # 进行登录
        # self.services.shopLogin.shop_login("1149@admin", "639520200624")
        self.services.shopLogin.shop_login("1135@admin", "639520200623")

    # 用例后置处理：执行完用例之后执行，每条用例都要执行一次
    def tearDown(self):
        # 关闭driver
        # webDriver().quit_driver()
        pass

    # 测试用例：缴纳水费
    def test_water(self):
        self.services.Services.page_water("300","1663441836","1836","147258")
        self.assertIn(self.services.Services.page_get_pay_success_info(),"您的订单已支付成功")

if __name__ == '__main__':
    unittest.main()