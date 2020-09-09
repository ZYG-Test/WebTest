#导包
import unittest
from base.webDriver import webDriver


#引用log日志器
from page.page import Page
from tools.get_logger import GetLogger
log =GetLogger().get_logger()


class TestTransfer(unittest.TestCase):

    # 用例前置条件：在执行用例之前执行，每条用例都要执行一次
    def setUp(self):
        # 获取driver
        self.driver = webDriver().get_web_driver()
        # login页面实例化
        self.transfer = Page(self.driver)
        # 进行登录
        self.transfer.shopLogin.shop_login("1135@admin", "639520200623")
        # 进入代理服务页面
        self.transfer.Services.page_click_services()

    # 用例后置处理：执行完用例之后执行，每条用例都要执行一次
    def tearDown(self):
        # 关闭driver
        webDriver().quit_driver()
        # pass

    # 测试用例：跨境汇款
    def test_remittance(self):
        # 进入跨境汇款页面
        self.transfer.Transfer.page_click_money_transfer()
        # 汇款
        self.transfer.Transfer.cross_remittance("hui","lu","6217900100010200001","150","13800001111","147258")
        #断言
        self.assertIn(self.transfer.Transfer.page_get_remittance_info(),"您的订单已 汇款 成功")

if __name__ == '__main__':
    unittest.main()