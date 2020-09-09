# coding:utf-8
import os
import time
import cv2
import numpy as np
# import matplotlib.pyplot as plt


def get_pay_keyboard_number_location(im, pwd):
    numbers = set(list(pwd))
    templates = {}
    positions = {}
    nimgpath = ""  # 数字图片不在同目录时使用
    for i in numbers:
        templates[i] = os.path.join(nimgpath, "n{}.jpg".format(i))

    start = time.time()
    img_rgb = cv2.imread(im)

    for teNum, tepath in templates.items():
        # print(tepath)
        template = cv2.imread(tepath)
        h, w = template.shape[:-1]

        res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
        threshold = .95  # 匹配度参数，1为完全匹配
        loc = np.where(res >= threshold)
        if len(loc) > 0:
            positions[teNum] = zip(*loc[::-1])[0]
        else:
            print("Can not found number: [{}] in image: [{}].".format(tepath, im))

    end = time.time()
    print(end - start)

    return [positions[n] for n in pwd]


if __name__ == "__main__":
    ls = get_pay_keyboard_number_location('keyboard.jpg', '1234567890')
    print(ls)