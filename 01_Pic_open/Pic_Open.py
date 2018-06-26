# -*- coding: UTF-8 -*-
from PIL import Image
import os

pil_im = Image.open('timg.jpg').convert('L')
pil_im.thumbnail((128,128)) #创建缩略图

box = (100,100,400,400) #坐标依次是（左，上，右，下）
region = pil_im.crop(box) #使用 crop() 方法可以从一幅图像中裁剪指定区域

region = region.transpose(Image.ROTATE_180) #旋转
pil_im.paste(region,box) #粘贴

out = pil_im.resize((128,128)) #调整一幅图像的尺寸

out = pil_im.rotate(45) #旋转一幅图像