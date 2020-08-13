#导包
import unittest
from parameterized import parameterized
from base.driver import GetDriver
from page.page_login import PageLogin

#引用log日志器
from tools.get_logger import GetLogger
log =GetLogger().get_logger()

#数据驱动：调用read_txt方法
from tools.read_txt import read_txt
def get_data():
    arrs = []
    for data in read_txt("login.txt"):
        arrs.append(tuple(data.strip().split(',')))
    # 切片忽略首行
    return arrs[1:]



# 新建TestLogin类并继承unittest.TestCase
class TestLogin(unittest.TestCase):


    #所有用例执行前执行一次
    @classmethod
    def setUpClass(cls):
        # 获取driver
        cls.driver=GetDriver().get_web_driver()
        # # login实例化
        cls.login=PageLogin(cls.driver)
        # 点击会员中心
        cls.login.page_click_vip_center()
        # 点击登录链接
        cls.login.page_click_login_url()


    #所有用例执行后执行一次
    @classmethod
    def tearDownClass(cls):
        # 关闭driver
        GetDriver().quit_driver()

    # 登录测试用例
    @parameterized.expand(get_data())
    def test_login(self, username, pwd, expect, status):
        try:
            # 调用组合登陆业务方法
            self.login.page_login(username, pwd)
            # 判断是否是正向用例
            if status == 'true':
                #退出登录
                self.login.login_out()
                # 断言登陆是否成功
                self.assertIn(self.login.login_assert_success_info(),expect)
                # 断言成功,获取日志
                log.info("登录后退出登录用例执行成功")
                # 点击会员中心：为了回到登录页面，让其他用例执行登录操作
                self.login.page_click_vip_center()
                # 点击登录链接
                self.login.page_click_login_url()
            # 反向用例
            else:
                # 断言错误信息是否与预期一致
                self.assertIn(self.login.login_assert_failure_info(),expect)
                # 断言成功,获取日志
                log.info("登录失败用例验证正确")
        except Exception as msg:
            # 断言失败，获取日志
            log.error(msg)
            # 断言失败，调用截图
            self.login.base_get_image()


if __name__ == '__main__':
    unittest.main()