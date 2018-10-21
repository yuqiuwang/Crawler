Author  : yuqiuwang
Mail    : yuqiuwang929@gmail.com
Website : https://www.yuqiulearn.cn
Created : 2018/10/13 12:44


import pytesseract
from PIL import Image
import numpy as np

def image_denoising(img, threshold=130):
    img = np.array(img)
    img[img > threshold] = 255
    img[img <= threshold] = 0
    img = Image.fromarray(img)
    return img

my_image = Image.open('test.png')
# my_image = my_image.convert('L') # 这样可以转化为灰度图，具体请查看PIL包的用法
my_image = image_denoising(my_image)
test_code = pytesseract.image_to_string(my_image)
test_code = test_code.strip()
print(test_code)
