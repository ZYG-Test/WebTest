from selenium.webdriver.common.by import By


"""以下为项目服务器地址"""
URL="http://127.0.0.1/"


'''登录页面元素信息'''
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



