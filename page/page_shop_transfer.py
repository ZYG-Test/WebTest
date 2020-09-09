import time
import page
from base.base import Base
import faker
f = faker.Faker()


class PageTransfer(Base):

    # 点击跨境汇款
    def page_click_money_transfer(self):
        self.base_click(page.shop_money_transfer)

    #收款人
    def page_receive(self,name,lastname,account,amount,number):
        # 输入收款人姓名
        self.base_input(page.shop_receive_name, name)
        # 输入姓氏
        self.base_input(page.shop_receive_lastname, lastname)
        # 输入收款人账户
        self.base_input(page.shop_receive_account, account)
        # 输入收款金额
        self.base_input(page.shop_receive_amount, amount)
        # 输入收款人联系电话
        self.base_input(page.shop_receive_number, number)
        # 选择汇款用途
        self.base_click(page.shop_receive_use)
        time.sleep(1)
        self.base_click(page.shop_receive_use_select)

    # 汇款人
    def page_certificate(self,country="CHN"):
        #输入姓名
        self.base_input(page.shop_remitter_name,f.last_name())
        #输入姓氏
        self.base_input(page.shop_remitter_lastname,f.last_name())
        #输入生日
        self.base_input(page.shop_remitter_birthday,f.date())
        #输入国籍
        self.base_input(page.shop_remitter_country,country)
        #证件类型选择
        self.base_click(page.shop_remitter_certificate)
        time.sleep(1)
        self.base_click(page.shop_certificate_select)
        #证件所属国籍
        self.base_input(page.shop_certificate_country, country)
        #输入证件号
        self.base_input(page.shop_certificate_number, f.credit_card_number())
        #输入地址
        self.base_input(page.shop_certificate_address,f.street_address())
        #输入市区
        self.base_input(page.shop_certificate_area, f.city_suffix())

    # 勾选认证点击下一步
    def page_check_next(self):
        self.base_click(page.shop_certification_check)
        self.base_click(page.shop_nextBtn)
        self.base_click(page.shop_nextBtn_two)

    # 输入支付密码
    def page_input_pwd(self,pwd):
        self.base_input(page.shop_input_pay,pwd)

    # 点击确认汇款
    def page_click_determine(self):
        self.base_click(page.shop_determine)

    # 获取跨境汇款成功返回信息
    def page_get_remittance_info(self):
        return self.base_get_text(page.shop_remittance_info)


    '''跨境汇款组合业务'''
    def cross_remittance(self,name,lastname,account,amount,number,pwd):
        # 点击跨境汇款
        self.page_click_money_transfer()
        # 输入收款人信息
        self.page_receive(name,lastname,account,amount,number)
        # 输入汇款人信息
        self.page_certificate()
        # 勾选已认证点击下一步
        self.page_check_next()
        # 输入支付密码
        self.page_input_pwd(pwd)
        # 确认缴费
        self.page_click_determine()