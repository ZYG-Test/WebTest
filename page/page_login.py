import page
from base.base import Base

class PageLogin(Base):

    # 点击会员中心
    def page_click_vip_center(self):
        self.base_click(page.login_vip_center)

    #点击登录链接
    def page_click_login_url(self):
        self.base_click(page.login_url)

    # 输入用户名
    def page_input_user(self,user):
        self.base_input(page.login_user, user)

    #输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    #点击登录
    def page_click_login(self):
        self.base_click(page.login_btn)

    # 点击注销登录
    def login_click_out(self):
        self.base_click(page.login_out)
        # self.base_opencv_click('../data/login_out.png')

    # 返回注销账号成功后提示信息""
    def login_assert_success_info(self):
        return self.base_get_text(page.login_out_success_info)   # 一定要返回哦

    # 返回登录失败后提示信息""
    def login_assert_failure_info(self):
        return self.base_get_text(page.login_failure_info)  # 一定要返回哦

    '''业务组合操作'''
    #登录业务组合
    def page_login(self,user,pwd):
        # 输入用户名
        self.page_input_user(user)
        # 输入密码
        self.page_input_pwd(pwd)
        # 点击登录
        self.page_click_login()

    # 成功登录业务组合，主要是给其他需要进行登录的用例进行前置操作
    def page_success_login(self,user,pwd):
        # 点击会员中心
        self.page_click_vip_center()
        # 点击登录链接
        self.page_click_login_url()
        # 输入用户名
        self.page_input_user(user)
        # 输入密码
        self.page_input_pwd(pwd)
        # 点击登录
        self.page_click_login()

    #注销账号
    def login_out(self):
        # 点击会员中心
        self.page_click_vip_center()
        # 点击注销登录
        self.login_click_out()


if __name__ == '__main__':
    from base.driver import GetDriver
    login = PageLogin(GetDriver().get_web_driver())
    login.page_success_login("18142651996@vip.com", "aaa111")
    login.login_out()
