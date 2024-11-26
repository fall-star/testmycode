"""
学习使用PIL库读取图片并转换为numpy数组
学习使用transforms库将图片转换为tensor
思考一下numpy和tensor的区别
可以用调试器查看变量的类型和值
"""

#导入库
from PIL import Image
from torchvision import transforms
import numpy as np

#打开并读取图片
img = Image.open('./test.png')
print(img.size)
print(img.format)
print(img)

#转换为numpy数组
img1 = np.array(img)
print(img1.shape)
print(img1.dtype)
print(img1[0])

#转换为tensor
img2 = transforms.ToTensor()(img)
print(img2.shape)
print(img2.dtype)
print(img2)
