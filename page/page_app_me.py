import page
from base.base import Base

class PageMe(Base):

    # 点击我的按钮
    def page_click_me(self):
        self.base_click(page.meBtn)

    # 点击退出
    def page_click_loginout(self):
        # 点击我的
        self.page_click_me()
        # 滑动
        self.base_swipe(1,0.5,0.8,0.5,0.2)
        # 点击登出
        self.base_click(page.loginout)
        #点击确定退出
        self.base_click(page.loginout_ok)


