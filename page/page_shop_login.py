import page
from base.base import Base

class PageShopLogin(Base):

    # 输入用户名
    def page_input_user(self,user):
        self.base_input(page.shop_ID, user)

    #输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.shop_pwd, pwd)

    #点击登录
    def page_click_login(self):
        self.base_click(page.shop_loginBtn)

    # 切换语言为中文
    def page_click_chinese(self):
        self.base_click(page.shop_language)
        self.base_opencv_click("../data/shop_server/chinese.png")

    # 组合登录
    def shop_login(self,user,pwd):
        self.page_input_user(user)
        self.page_input_pwd(pwd)
        self.page_click_login()
        self.page_click_chinese()

if __name__ == '__main__':
    from base.webDriver import GetDriver
    login = PageShopLogin(GetDriver().get_web_driver())
    login.shop_login("1123@admin", "639520200623")