import page
from base.base import Base

class PageServices(Base):

    # 点击代理服务按钮
    def page_click_services(self):
        self.base_click(page.shop_click_service)

    # 点击缴费订单
    def page_click_payOrder(self):
        self.base_click(page.shop_payment_order)

    # 选择水费
    def page_click_water(self):
        self.base_click(page.shop_water)

    # 选择供应商
    def page_click_water_supplier(self):
        # self.base_opencv_click("../data/shop_server/Bp_water.png")
        self.base_click(page.shop_water_Bp)

    # 输入缴费金额
    def page_input_amount(self,amount):
        self.base_input(page.shop_input_amount,amount)

    # 输入账户
    def page_input_accountNo(self,accountNo):
        self.base_input(page.shop_input_accountNo,accountNo)

    # 输入识别号
    def page_input_Identifier(self,Identifier):
        self.base_input(page.shop_input_Identifier,Identifier)

    # 点击下一步
    def page_click_next(self):
        self.base_click(page.shop_click_next)

    # 输入支付密码
    def page_input_paypwd(self,pwd):
        self.base_input(page.shop_pay_pwd, pwd)

    # 点击缴费
    def page_click_pay(self):
        self.base_click(page.shop_click_pay)

    # 获取缴费成功提示:您的订单已支付成功
    def page_get_pay_success_info(self):
        return self.base_get_text(page.shop_paysuccess_info)


    # 水费缴费业务组合
    def page_water(self,amount,accountNo,Identifier,pwd):
        # 进入水费供应商页面
        self.page_click_services()
        self.page_click_payOrder()
        self.page_click_water()
        self.page_click_water_supplier()


        # 输入缴费信息
        self.page_input_amount(amount)
        self.page_input_accountNo(accountNo)
        self.page_input_Identifier(Identifier)
        self.page_click_next()

        # 缴费
        self.page_input_paypwd(pwd)
        self.page_click_pay()