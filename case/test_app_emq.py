#导包
import unittest
import warnings
from base.appDriver import appDriver

#引用log日志器
from page.page import Page
from tools.get_logger import GetLogger
log =GetLogger().get_logger()


class TestTransfer(unittest.TestCase):

    # 用例前置条件：在执行用例之前执行，每条用例都要执行一次
    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning) # 忽略警告
        # 获取driver
        self.driver = appDriver().get_app_driver()
        # login页面实例化
        self.transfer = Page(self.driver)
        # 启动页处理
        self.transfer.AppLogin.page_start()
        # 登录
        self.transfer.AppLogin.page_login_success("9520200623", "789789")

    # 用例后置处理：执行完用例之后执行，每条用例都要执行一次
    def tearDown(self):
        # 退出登录
        self.transfer.AppMe.page_click_loginout()
        # 关闭driver
        appDriver().quit_driver()

    # 测试用例：跨境汇款成功
    def test_emq_success(self):
        # 进入emq页面
        self.transfer.AppTransfer.page_click_emq()
        # 进行emq汇款
        self.transfer.AppTransfer.page_emq_transfer("100")
        #断言
        self.assertIn("跨境汇款",self.transfer.AppTransfer.page_get_emq_info())
        #返回首页
        self.transfer.AppTransfer.page_emq_back()

if __name__ == '__main__':
    unittest.main()