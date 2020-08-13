#导包
import unittest
from base.driver import GetDriver
from page.page_login import PageLogin

#引用log日志器
from tools.get_logger import GetLogger
log =GetLogger().get_logger()

# 新建TestLogin类并继承unittest.TestCase
class TestLogin(unittest.TestCase):

    #用例前置条件：在执行用例之前执行，每条用例都要执行一次
    def setUp(self):
        # 获取driver
        self.driver=GetDriver().get_web_driver()
        # login页面实例化
        self.login=PageLogin(self.driver)
        #点击会员中心
        self.login.page_click_vip_center()
        #点击登录链接
        self.login.page_click_login_url()


    #用例后置处理：执行完用例之后执行，每条用例都要执行一次
    def tearDown(self):
        # 关闭driver
        GetDriver().quit_driver()


    #登录测试用例
    def test_login_success(self):
        try:
            #调用组合登陆业务方法
            self.login.page_login("18142651996@163.com","aaa111")
            #调用退出登录业务方法
            self.login.login_out()
            # 断言
            self.assertIn(self.login.login_assert_success_info(), "您已成功退出了您的账户。")
            # 断言成功,获取日志
            log.info("登录后退出登录用例执行成功")
        except Exception as msg:
            # 断言失败，获取日志
            log.error(msg)
            # 断言失败，调用截图
            self.login.base_get_image()

    # 登录失败测试用例
    def test_login_failure(self):
        try:
            #调用组合登陆业务方法
            self.login.page_login("18142651996@163.com","aaa222")
            # 断言
            self.assertIn(self.login.login_assert_failure_info(), "警告：邮箱地址/电话号码或密码不匹配。")
            # 断言成功,获取日志
            log.info("登录失败用例验证正确")
        except Exception as msg:
            # 断言失败，获取日志
            log.error(msg)
            # 断言失败，调用截图
            self.login.base_get_image()

if __name__ == '__main__':
    unittest.main()