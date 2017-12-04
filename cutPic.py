#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image

#im = Image.open("pic\login.png")
# 图片的宽度和高度
#img_size = im.size
#print("图片宽度和高度分别是{}".format(img_size))
'''
裁剪：传入一个元组作为参数
元组里的元素分别是：（距离图片左边界距离x， 距离图片上边界距离y，距离图片左边界距离+裁剪框宽度x+w，距离图片上边界距离+裁剪框高度y+h）
'''

#截取登录界面块
def cutPicLogin(picPath):
    im = Image.open(picPath)
    x =782
    y =113
    w =292
    h =460
    region = im.crop((x, y, x + w, y + h))
    region.save("pic\loginTable2.png")

#截取登录界面块,但不存储到文件系统中
def cutPicLogin2(picPath):
    im = Image.open(picPath)
    x =782
    y =113
    w =292
    h =460
    region = im.crop((x, y, x + w, y + h))
    #region.save("pic\loginTable2.png")

#登录界面分块，version1,只能实现单个
def cropLogin():
    im=Image.open("pic\loginTable.png");
    im_size=im.size;
    print("login图片宽度和高度分别是{}".format(im_size));
    #把图片平均分成10块
    # 第1块
    w = im_size[0] / 10.0  #宽
    h = im_size[1] / 8.0 #长
    x = 0
    y = 0
    region = im.crop((x, y, x + w, y + h))
    region.save("pic\crop_average-1.png")

#登录界面分块，version2，for循环分块
def cropLogin2(imageName,num):
    im=Image.open(imageName);
    im_size=im.size;
    print("login图片宽度和高度分别是{}".format(im_size));
    #把图片平均分成10块
    # 第1块
    w = im_size[0] / 13.66  #宽
    h = im_size[1] / 7.36 #高
    x = 0                   #宽
    y = 0                   #高
    for i in range(10): #循环宽度8次       ，10
        for j in range(5):  #循环长度14次   ，5
            region = im.crop((x, y, x + w, y + h))
            region.save("image\\crop_average"+str(num)+"-%d-%d.png" % (i,j));
            x=x+w;
            y=y;
        x=0                 #高依次增加，宽度从0~~边界值
        y=y+h;


def loginCut(path,num):
    im = Image.open(path);
    im_size = im.size;
    print("login图片宽度和高度分别是{}".format(im_size));
    # 把图片平均分成10块
    # 第1块           个数
    w = im_size[0] / 13.66  # 设置被切长度  13.66*2 的倍数
    h = im_size[1] / 14.72 # 设置被切宽度      7.36*2的倍数
    x = 0  # 长
    y = 0  # 宽
    for i in range(15):  # 循环宽度8次
        for j in range(14):  # 循环长度14次
            region = im.crop((x, y, x + w, y + h))
            region.save("image1\\crop_average" + str(num) + "-%d-%d.png" % (i, j));
            x = x + w;
            y = y;
        x = 0  # 高依次增加，宽度从0~~边界值
        y = y + h;



def cutLoginType3():
    pass



if __name__ == "__main__":
    #im = Image.open("data\imageinit\\111.png")  # type:Image,Image
    #x=im.size
    #print(x)
    loginCut('data\imageinit\\111.png', 1)
    loginCut('data\imageinit\\222.png', 2)
    loginCut('data\imageinit\\333.png', 3)

    #cutPicLogin();
    #cropLogin2('data\imageinit\\111.png', 1);
    #cropLogin2('data\imageinit\\222.png', 2);
    #cropLogin2('data\imageinit\\333.png', 3);



