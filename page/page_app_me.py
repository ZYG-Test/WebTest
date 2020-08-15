from selenium.webdriver.common.by import By
from base.base import Base

class PageMe(Base):
    #我的
    meBtn=By.XPATH,"//*[@text='我的']"


    #通用设置
    setting = By.ID, 'com.zybitech.juancash:id/rl_setting'
    # 帮助
    contact = By.ID, 'com.zybitech.juancash:id/rl_contact'
    #退出
    loginout=By.ID,'com.zybitech.juancash:id/rl_out'





    # 点击我的按钮

    #向上滑动

    #点击退出

    #点击确认按钮退出