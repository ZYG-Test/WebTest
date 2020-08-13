import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import page

#引用log日志器
from tools.get_logger import GetLogger
from tools.opencv import GraphicalLocator

log =GetLogger().get_logger()

class Base:

    def __init__(self,driver):
        log.info("[base]: 正在获取初始化driver对象：{}".format(driver))
        self.driver=driver

    # 查找元素 方法封装
    def base_find(self,loc,timeout=30,poll=0.5):
        log.info("[base]: 正在定位：{}元素，超时时间为：{}秒".format(loc,timeout))
        #使用显示等待查找元素(快速导包快捷键：ctrl+Alt+空格)
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x:x.find_element(*loc))


    # 下拉框定位
    def base_select_find(self,loc,value):
        select=Select(self.base_find(loc))
        log.info('[Base]正在对下拉框：{}进行选择'.format(value))
        select.select_by_visible_text(value)

    # iframe定位
    def base_switch_frame(self):
        pass

    # 点击元素 方法封装
    def base_click(self,loc):
        el=self.base_find(loc)
        log.info("[base]: 正在对：{}元素进行点击操作".format(loc))
        el.click()

    # 输入元素 方法封装
    def base_input(self,loc,value):
        #获取元素
        el=self.base_find(loc)
        #清空内容
        log.info("[base]: 正在对：{}元素进行清空操作".format(loc))
        el.clear()
        #输入内容
        log.info("[base]: 正在对：{}元素进行输入操作，输入内容：{}".format(loc,value))
        el.send_keys(value)

    # 获取文本信息 方法封装
    def base_get_text(self,loc):
        log.info("[base]: 正在获取：{}元素文本信息".format(loc))
        return self.base_find(loc).text

    # 截图 方法封装
    def base_get_image(self):
        log.info("[base]: 用例执行失败开始截图")
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    #判断元素是否存在 方法封装
    def base_element_is_exist(self,loc):
        try:
            self.base_find(loc,timeout=10)
            log.info("[base]: {} 元素查找成功，当前页面存在".format(loc))
            return True     #代表元素存在
        except:
            log.info("[base]: {} 元素查找失败，不存在当前页面".format(loc))
            return False    #代表元素不存在

    # 回到首页
    def base_home(self):
        self.driver.get(page.URL)

    # 切换farme表单
    def base_switch_iframe(self, name):
        self.driver.switch_to.farme(name)

    # 回到默认目录方法
    def base_default_content(self):
        self.driver.switch_to.default_content()

    # 通过图像获取元素坐标进行定位
    def base_opencv_click(self,image_file):
        img_check = GraphicalLocator(image_file)
        img_check.find_me(self.driver)
        is_found = True if img_check.threshold['shape'] >= 0.8 and img_check.threshold['histogram'] >= 0.4 else False
        if is_found:
            action = ActionChains(self.driver)
            log.info("[base]: {} :图片坐标{},{}".format(image_file,img_check.center_x, img_check.center_y))
            action.move_by_offset(img_check.center_x, img_check.center_y)
            action.click()
            action.perform()
        else:
            log.error("[base]: {} 图片无法识别".format(image_file))