import time
import base64
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from appium.webdriver.common.mobileby import MobileBy



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
        log.info("[base]: 正在定位：{}元素".format(loc))
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
        self.driver.get_screenshot_as_file("../report/image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    #判断元素是否存在 方法封装
    def base_element_is_exist(self,loc):
        try:
            self.base_find(loc,timeout=10)
            log.info("[base]: {} 元素查找成功，当前页面存在".format(loc))
            return True     #代表元素存在
        except:
            log.info("[base]: {} 元素不存在当前页面".format(loc))
            return False    #代表元素不存在

    # 切换farme表单
    def base_switch_iframe(self, name):
        self.driver.switch_to.farme(name)

    # 回到默认目录方法
    def base_default_content(self):
        self.driver.switch_to.default_content()

    # 通过图像获取元素坐标进行定位
    def base_opencv_click(self,image_file):
            # 导入需要定位的图片地址
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



    # 滑动封装，默认向左滑动
    def base_swipe(self,num, start_x=0.9, start_y=0.5, end_x=0.1, end_y=0.5):
        '''
        向左滑动。y轴保持不变，X轴：由大变小
        向右滑动。y轴保持不变，X轴：由小变大
        向上滑动。x轴保持不变，y轴：由大变小
        向下滑动。x轴保持不变，y轴：由小变大
        '''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        for i in range(num):
            x1 = int(x * start_x)
            y1 = int(y * start_y)   #满足启动页和首页相关滑动操作
            x2 = int(x * end_x)
            y2 = int(x * end_y)
            self.driver.swipe(x1, y1, x2, y2, 1500)


    # 通过图片进行定位
    def base_find_image(self,img_path):
        self.driver.update_settings({"getMatchedImageResult": True})
        log.info("[base:]正在进行图片定位")
        el = self.driver.find_element_by_image(img_path)
        # el.get_attribute('visual')
        el.click()


    # 支付密码
    def base_password(self):
        self.base_find_image("../data/password/n1.png").click()
