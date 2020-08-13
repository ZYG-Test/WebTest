import cv2
import numpy
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains

'''
安装：
1、pip install opencv-python --user
2、pip install opencv-contrib-python --user
3、pip install pillow
'''


class GraphicalLocator(object):

    def __init__(self, img_path):
        self.locator = img_path
        # 从左上角算起的x，y位置（以像素为单位）
        self.x = None
        self.y = None
        self.img = cv2.imread(img_path)
        self.height = self.img.shape[0]
        self.width = self.img.shape[1]
        self.threshold = None

    @property
    def center_x(self):
        return self.x + int(self.width / 2) if self.x and self.width else None

    @property
    def center_y(self):
        return self.y + int(self.height / 2) if self.y and self.height else None


    def find_me(self, drv):
        # 清除最后找到的坐标
        self.x = self.y = None
        # Get current screenshot of a web page
        scr = drv.get_screenshot_as_png()
        # 获取网页的当前屏幕截图
        scr = Image.open(BytesIO(scr))
        # 转换为OpenCV接受的格式
        scr = numpy.asarray(scr, dtype=numpy.float32).astype(numpy.uint8)
        # 将图像从BGR转换为RGB格式
        scr = cv2.cvtColor(scr, cv2.COLOR_BGR2RGB)

        # 图像匹配仅适用于灰色图像
        # （从RGB / BGR到灰度的颜色转换）
        img_match = cv2.minMaxLoc(
            cv2.matchTemplate(cv2.cvtColor(scr, cv2.COLOR_RGB2GRAY),
                              cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY),
                              cv2.TM_CCOEFF_NORMED))

        # 计算找到的元素的位置
        self.x = img_match[3][0]
        self.y = img_match[3][1]

        # 从与模板图像匹配的完整屏幕截图裁剪部分
        scr_crop = scr[self.y:(self.y + self.height),
                   self.x:(self.x + self.width)]

        # 计算两个模板的颜色直方图
        # 并匹配图像并进行比较
        scr_hist = cv2.calcHist([scr_crop], [0, 1, 2], None,
                                [8, 8, 8], [0, 256, 0, 256, 0, 256])
        img_hist = cv2.calcHist([self.img], [0, 1, 2], None,
                                [8, 8, 8], [0, 256, 0, 256, 0, 256])
        comp_hist = cv2.compareHist(img_hist, scr_hist,
                                    cv2.HISTCMP_CORREL)
        # 保存阈值匹配项：图形图像和图像直方图
        self.threshold = {'shape': round(img_match[1], 2),
                          'histogram': round(comp_hist, 2)}

        # 返回匹配周围带有蓝色矩形的图像
        return cv2.rectangle(scr, (self.x, self.y),
                             (self.x + self.width, self.y + self.height),
                             (0, 0, 255), 2)






if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com/')
    img_check = GraphicalLocator('../data/login.png')
    img_check.find_me(driver)
    # cv2.imwrite('这里生成一个新图片，会将匹配的图片在原图中圈出来', img_check.find_me(driver))
    is_found = True if img_check.threshold['shape'] >= 0.8 and img_check.threshold['histogram'] >= 0.4 else False
    if is_found:
        action = ActionChains(driver)
        print(img_check.center_x, img_check.center_y)
        action.move_by_offset(img_check.center_x, img_check.center_y)
        action.click()
        action.perform()
    else:
        print('无法识别')