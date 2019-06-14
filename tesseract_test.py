# -*- coding: UTF-8 -*-
# 验证码识别

import pytesseract
from PIL import Image

if __name__ == '__main__':
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

    image = Image.open(r'C:\Users\Administrator\Desktop\test\a.png')

    # text = pytesseract.image_to_string(image) #默认英文
    text = pytesseract.image_to_string(image,lang='chi_sim')  # 指定中文

    print text



