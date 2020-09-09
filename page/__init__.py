from selenium.webdriver.common.by import By


"""以下为项目服务器地址"""
# URL="http://127.0.0.1/"
URL="http://merchant.juanwallet.net/#/login?redirect=%2Fhome"



'''APP'''
# 二维码
OR=By.XPATH,"//*[@text='二维码']"

'''二维码与商家页面'''
#商家服务
shop_service=By.ID,'com.zybitech.juancash:id/ll_merchant'

#添加商店
add_shop=By.ID,'com.zybitech.juancash:id/iv_right'
# 输入店铺名称
input_shopName=By.ID,'com.zybitech.juancash:id/et_input'
# 输入代理ID
input_agentID=By.ID,'com.zybitech.juancash:id/et_promoter_id'
# 选择企业,默认个人
enterprise=By.XPATH,"//*[@text='企业']"
# 点击下一步
nextBtn=By.XPATH,"//*[@text='下一步']"
# 输入联系电话
input_phone=By.ID,'com.zybitech.juancash:id/tab_contact_number'
# 输入店铺地址
input_address=By.ID,'com.zybitech.juancash:id/et_content'
# 上传门店照片
store_photo=By.ID,'com.zybitech.juancash:id/rl_store_photo'
# 以下为企业所需要的+个人
articles=By.XPATH,"//*[@text='Articles of Corporation']"
laws=By.XPATH,"//*[@text='By Laws']"
# 以下为个人需要的
permit=By.XPATH,"//*[@text='Business Permit']"
BIR=By.XPATH,"//*[@text='BIR']"
contract=By.XPATH,"//*[@text='合同']"
store_photos=By.XPATH,"//*[@text='门店照']"
# 点击确认按钮
confirmBtn=By.ID,'com.zybitech.juancash:id/bt_confirm'

'''跨境汇款'''
# 跨境汇款
app_abroad_transfer=By.XPATH,"//*[@text='跨境汇款']"
#人民币输入框
app_emq_amount=By.ID,"com.zybitech.juancash:id/emq_amount_rmb"
#选择优惠券
app_emq_coupon=By.ID,"com.zybitech.juancash:id/ll_coupon"
#点击下一步
app_emq_next=By.ID,"com.zybitech.juancash:id/btn"
#选择收款人
app_emq_receiving_account=By.XPATH,"//*[@text='收款帐号']"
#勾选已实名认证
app_emq_verified=By.ID,"com.zybitech.juancash:id/cb_verified"
# 确定
app_emq_confirm=By.ID,"com.zybitech.juancash:id/btn_confirm"
# 点击立即付款
app_emq_pay=By.ID,"com.zybitech.juancash:id/bt_to_pay"
# 跨境汇款成功信息
app_emq_info=By.ID,"com.zybitech.juancash:id/tv_type"
# 完成按钮
app_emq_complete=By.ID,"com.zybitech.juancash:id/bt_complete"
# 返回按钮
app_emq_back=By.ID,"com.zybitech.juancash:id/ll_back"

'''我的页面元素'''
# 我的
meBtn = By.XPATH, "//*[@text='我的']"
# 通用设置
setting = By.ID, 'com.zybitech.juancash:id/rl_setting'
# 帮助
contact = By.ID, 'com.zybitech.juancash:id/rl_contact'
# 退出
loginout = By.ID, 'com.zybitech.juancash:id/rl_out'
# 确定退出按钮
loginout_ok=By.ID,"com.zybitech.juancash:id/md_button_positive"





'''-------------juancah商家平台---------------------'''

'''登录页面'''
# 输入账号
shop_ID=By.XPATH,".//*[@id='pane-login']/form/div[1]/div/div[1]/input"
# 输入密码
shop_pwd=By.XPATH,".//*[@id='pane-login']/form/div[2]/div/div/input"
# 点击登录
shop_loginBtn=By.CSS_SELECTOR,'.el-button.el-button--primary'
# 切换中文
shop_language=By.XPATH,".//*[@id='app']/section/header/div/div[3]/div[2]/div"

'''代理服务页面'''
# 点击代理服务按钮
shop_click_service=By.XPATH,".//*[@id='app']/section/header/div/div[2]/ul/li[2]"
# 点击缴费订单
# shop_payment_order=By.XPATH,".//*[@class='el-scrollbar__view']/div/div[2]/div[1]/a/span"
shop_payment_order=By.XPATH,'//span[text()=\"缴费订单\"]'
# 水费
shop_water=By.XPATH,".//*[@class='el-collapse-item__content']/div[1]"
# 水费供应商
shop_water_Bp=By.XPATH,".//*[@class='el-scrollbar__view']/div[10]"
#输入缴费金额
shop_input_amount=By.XPATH,".//*[@id='app-body']/section/main/div/div[2]/div/section/section/main/div/div/div[1]/div/form/div[2]/div/div[1]/input"
#输入账户
shop_input_accountNo=By.XPATH,".//*[@id='app-body']/section/main/div/div[2]/div/section/section/main/div/div/div[1]/div/form/div[3]/div/div/input"
#输入识别号
shop_input_Identifier=By.XPATH,".//*[@id='app-body']/section/main/div/div[2]/div/section/section/main/div/div/div[1]/div/form/div[4]/div/div/input"
#点击下一步
shop_click_next=By.XPATH,".//*[@class='el-form-item__content']/button[2]"
# 输入支付密码
shop_pay_pwd=By.XPATH,".//*[@id='app-body']/section/main/div/div[2]/div/section/section/main/div[2]/div/div[1]/div/form/div[3]/div/div/input"
# 点击缴费
shop_click_pay=By.XPATH,".//*[@class='el-form']/div[5]/button[2]"
# 缴费成功提示
shop_paysuccess_info=By.CSS_SELECTOR,'.title'

'''电话充值'''
#GLOBE
# shop_phone_globe=By.XPATH,".//*[@class='el-scrollbar__view']/div/div[3]/div[1]/a/span"
shop_phone_globe=By.XPATH,'//span[text()=\"GLOBE\"]'
# 手机号码输入框
shop_phone_input=By.CSS_SELECTOR,".el-input__inner"
# 选择充值金额
shop_select_recharge=By.XPATH,".//*[@id='pane-phoneCharge']/div/div[1]/div/div[3]/div/span"
#提交按钮
shop_phone_submit=By.XPATH,".//*[@class='el-row']/div[2]/button"
# 输入交易密码
shop_phone_pwd=By.XPATH,".//*[@class='el-scrollbar']/div[1]/div/form/div[5]/div/div/input"
# 点击缴费
shop_phone_pay=By.XPATH,".//*[@class='el-form']/div[6]/div/button[2]"


'''跨境汇款'''
# 点击境外汇款
shop_money_transfer=By.XPATH,'//span[text()=\"境外汇款\"]'
#收款人姓名
shop_receive_name=By.XPATH,".//*[@class='el-form']/div[1]/div[2]/div/div[1]/div/div/div/input"
#收款人姓氏
shop_receive_lastname=By.XPATH,".//*[@class='el-form']/div[1]/div[2]/div/div[3]/div/div/div/input"
#收款人账户名
shop_receive_account=By.XPATH,".//*[@class='el-form']/div[1]/div[3]/div/div/input"
#收款金额
shop_receive_amount=By.XPATH,".//*[@class='el-form']/div[1]/div[4]/div/div/input"
#收款人联系电话
shop_receive_number=By.XPATH,".//*[@class='el-form']/div[1]/div[5]/div/div/input"
#汇款用途
shop_receive_use=By.XPATH,".//*[@class='el-form']/div[1]/div[6]/div/div/div[1]/input"
shop_receive_use_select=By.XPATH,'//span[text()=\"Family/living expense\"]'
# 汇款人姓名
shop_remitter_name=By.XPATH,".//*[@class='el-form']/div[2]/div[1]/div/div[1]/div/div/div[1]/input"
# 汇款人姓氏
shop_remitter_lastname=By.XPATH,".//*[@class='el-form']/div[2]/div[1]/div/div[3]/div/div/div/input"
#生日
shop_remitter_birthday=By.XPATH,".//*[@class='el-form']/div[2]/div[2]/div/div/input"
#国籍
shop_remitter_country=By.XPATH,".//*[@class='el-form']/div[2]/div[3]/div/div[1]/input"
#证件类型
shop_remitter_certificate=By.XPATH,".//*[@class='el-form']/div[2]/div[4]/div/div/div[1]/input"
#证件类型选择national
shop_certificate_select=By.XPATH,'//span[text()=\"national\"]'
#证件所属国籍
shop_certificate_country=By.XPATH,".//*[@class='el-form']/div[2]/div[5]/div/div/input"
#证件号
shop_certificate_number=By.XPATH,".//*[@class='el-form']/div[2]/div[6]/div/div[1]/input"
#地址
shop_certificate_address=By.XPATH,".//*[@class='el-form']/div[2]/div[7]/div/div/input"
#市区
shop_certificate_area=By.XPATH,".//*[@class='el-form']/div[2]/div[8]/div/div/input"
#勾选已认证
shop_certification_check=By.XPATH,".//*[@class='el-form']/div[3]/label/span[1]/span"
#点击下一步
shop_nextBtn=By.CSS_SELECTOR,'.el-button.el-button--primary'
#继续点击下一步
shop_nextBtn_two=By.XPATH,".//*[@class='el-form']/div[4]/button[2]"
#支付输入框
shop_input_pay=By.XPATH,".//*[@id='app-body']/section/main/div/div[2]/div/section/div/div[3]/div/div[2]/div/div[1]/div[1]/input"
#确定按钮
shop_determine=By.XPATH,".//*[@class='dialog-footer']/button[2]"
#汇款成功提示：您的订单已 汇款 成功
shop_remittance_info=By.CSS_SELECTOR,".title"






'''-------------------web项目登录页面元素信息----------------'''
#点击会员中心
login_vip_center=By.XPATH,".//*[@id='top-links']/ul/li[2]/a/span[1]"
# 登录链接
login_url=By.PARTIAL_LINK_TEXT,'会员登录'
# 用户名输入框
login_user = By.CSS_SELECTOR, '#input-email'
# 密码输入框
login_pwd = By.CSS_SELECTOR, '#input-password'
# 登录按钮
login_btn = By.XPATH, ".//*[@id='content']/div/form/input"
# 注销登录
login_out=By.PARTIAL_LINK_TEXT,'注销退出'
# 获取退出账号提示信息"您已成功退出了您的账户。"
login_out_success_info=By.XPATH,".//*[@id='content']/div/div/div[2]/div[1]/p[1]"
#密码错误登录失败提示信息"警告：邮箱地址/电话号码或密码不匹配。"
login_failure_info=By.CSS_SELECTOR,".fa-exclamation-circle"




