from page.page_app_login import PageAppLogin


class Page:

    def __init__(self,driver):
        self.driver =driver

    @property
    def Login(self):
        return PageAppLogin(self.driver)