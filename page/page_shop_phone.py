import page
from base.base import Base

class pagePhone(Base):

    # 点击GLOBE话费缴费
    def page_click_globe(self):
        self.base_click(page.shop_phone_globe)

    # 输入手机号
    def page_input_number(self,number):
        self.base_input(page.shop_phone_input,number)

    # 选择缴费金额
    def page_select_recharge(self):
        self.base_click(page.shop_select_recharge)

    # 点击提交
    def page_click_submit(self):
        self.base_click(page.shop_phone_submit)

    # 输入交易密码
    def page_input_pwd(self,pwd):
        self.base_input(page.shop_phone_pwd,pwd)

    # 点击缴费
    def page_click_pay(self):
        self.base_click(page.shop_phone_pay)

    # 获取缴费成功信息：您的订单已支付成功
    def page_get_pay_info(self):
        return self.base_get_text(page.shop_paysuccess_info)


    '''globe手机充值组合业务'''
    def globe_pay(self,number,pwd):
        self.page_select_recharge()
        self.page_input_number(number)
        self.page_click_submit()
        self.page_input_pwd(pwd)
        self.page_click_pay()