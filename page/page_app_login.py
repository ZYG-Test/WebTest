from selenium.webdriver.common.by import By
from base.base import Base
#引用log日志器
from tools.get_logger import GetLogger
log =GetLogger().get_logger()

class PageAppLogin(Base):

    '''登录页面相关元素信息'''
    start=By.ID,"com.zybitech.juancash:id/btn_done"
    phone=By.ID,"com.zybitech.juancash:id/et_phone"
    vercode=By.ID,"com.zybitech.juancash:id/edit_text_view"
    nextBtn=By.ID,"com.zybitech.juancash:id/btn"
    # text文本定位可用余额
    available_balance=By.XPATH,"//*[@text='可用余额']"
    # 已在其他手机上登录提示：
    login_content = By.ID, "com.zybitech.juancash:id/tv_content"
    # 确定按钮
    login_content_ok = By.ID, "com.zybitech.juancash:id/bt_ok"



    '''登录页面相关操作'''
    # 滑动启动页介绍，点击开始按钮
    def page_start(self):
        self.base_swipe(3)
        self.base_click(self.start)

    # 输入用户名
    def page_phone(self,phone):
        self.base_input(self.phone,phone)

    # 输入密码
    def page_code(self,code):
        self.base_input(self.vercode,code)

    # 点击下一步按钮、
    def page_nextBtn(self):
        # self.base_click(self.nextBtn)
        self.base_find_image("../data/nextBtn.png")

    # 获取可用余额信息，断言是否登录成功
    def page_get_balance_info(self):
        return self.base_get_text(self.available_balance)



    # 登录业务组合
    def page_login(self,phone,code):
        # 1、输入用户名
        self.page_phone(phone)
        # 2、点击下一步
        self.page_nextBtn()
        # 3、输入验证码
        self.page_code(code)
        # 4、点击下一步
        self.page_nextBtn()

    # 登录成功业务->给其他用例调用
    def page_login_success(self,phone,code):
        try:
            self.page_login(phone,code)
            # 判断已在其他手机上登录提示是否存在，存在点击确定按钮重新登录，不存在则不进行任何操作
            if self.base_element_is_exist(self.login_content):
                self.base_click(self.login_content_ok)
                self.page_login(phone, code)
            else:
                pass
        except Exception as msg:
            log.error("[page_app_login:{}]".format(msg))

        
