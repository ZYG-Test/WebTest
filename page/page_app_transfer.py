import time
from base.base import Base
import page


class pageAppTransfer(Base):

    #点击跨境汇款
    def page_click_emq(self):
        # 首页向左滑动
        time.sleep(3)
        self.base_swipe(1,0.8,0.4,0.2,0.4)
        self.base_click(page.app_abroad_transfer)

    # emq输入金额
    def page_input_amount(self,amount):
        self.base_input(page.app_emq_amount,amount)

    # 点击下一步
    def page_next(self):
        self.base_click(page.app_emq_next)

    # 点击选择收款人
    def page_click_payee(self):
        self.base_click(page.app_emq_receiving_account)

    # 勾选已实名认证
    def page_click_verified(self):
        self.base_click(page.app_emq_verified)

    # 点击确定
    def page_click_confirm(self):
        self.base_click(page.app_emq_confirm)

    # 点击立即付款
    def page_click_pay(self):
        self.base_click(page.app_emq_pay)

    # 获取跨境汇款成功信息：na xie跨境汇款
    def page_get_emq_info(self):
        return  self.base_get_text(page.app_emq_info)

    # 跨境汇款组合业务
    def page_emq_transfer(self,amount):
        pass
        # 输入汇款金额
        self.page_input_amount(amount)
        # 点击下一步
        self.page_next()
        # 选择收款人
        self.page_click_payee()
        # 点击下一步
        self.page_next()
        # 勾选已实名认证
        self.page_click_verified()
        # 点击确定
        self.page_click_confirm()
        # 点击立即付款
        self.page_click_pay()
        # 点击支付密码
        self.base_password()

    # 跨境汇款完成后处理
    def page_emq_back(self):
        # 点击完成
        self.base_click(page.app_emq_complete)
        # 点击返回
        self.base_click(page.app_emq_back)

    # 完善汇款人信息
