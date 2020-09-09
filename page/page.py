from page.page_app_login import PageAppLogin
from page.page_app_me import PageMe
from page.page_app_transfer import pageAppTransfer
from page.page_shop_login import PageShopLogin
from page.page_shop_phone import pagePhone
from page.page_shop_services import PageServices
from page.page_shop_transfer import PageTransfer


class Page:

    def __init__(self,driver):
        self.driver =driver
    '''juancash'''
    @property
    def AppLogin(self):
        # 登录页面
        return PageAppLogin(self.driver)

    @property
    def AppMe(self):
        #我的页面
        return PageMe(self.driver)

    @property
    def AppTransfer(self):
        #emq页面
        return pageAppTransfer(self.driver)

    '''商家平台'''
    @property
    def shopLogin(self):
        return PageShopLogin(self.driver)

    @property
    def Services(self):
        return PageServices(self.driver)

    @property
    def Transfer(self):
        return PageTransfer(self.driver)

    @property
    def Phone(self):
        return pagePhone(self.driver)
