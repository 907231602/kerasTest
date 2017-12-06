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


#裁剪三种不同类型的图片各1张,参数：路径与图片类别，大小：50*100
def loginCut(path,num):
    im = Image.open(path);
    im_size = im.size;
    print("login图片宽度和高度分别是{}".format(im_size));
    # 把图片平均分成10块
    # 第1块           个数
    w = im_size[0] / 13.66  # 设置被切长度  13.66 的倍数
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


#裁剪三种不同类型的图片各14张,参数：路径与图片类别，大小：50*100
def cutLoginType3(path,type):
    for k in range(1,15):
        im = Image.open(path+'_'+str(k)+".png");
        im_size = im.size;
        print("login图片宽度和高度分别是{}".format(im_size));
        # 把图片平均分成10块
        # 第1块           个数
        w = im_size[0] / 13.66  # 设置被切长度  13.66 的倍数
        h = im_size[1] / 14.56  # 设置被切宽度  7.28*2的倍数
        x = 0  # 长
        y = 0  # 宽
        for i in range(15):  # 循环宽度8次
            for j in range(14):  # 循环长度14次
                region = im.crop((x, y, x + w, y + h))
                region.save("image3\\crop_average" + str(type) + "-%d-%d-%d.png" % (k , i , j));
                x = x + w;
                y = y;
            x = 0  # 高依次增加，宽度从0~~边界值
            y = y + h;


#裁剪三种不同类型的图片各14张,参数：路径与图片类别，大小：200*200
def cutLoginType4(path,type):
    for k in range(1,15):
        im = Image.open(path+'_'+str(k)+".png");
        im_size = im.size;
        #print("login图片宽度和高度分别是{}".format(im_size));
        # 把图片平均分成10块
        # 第1块           个数
        w = im_size[0] / 6.83  # 设置被切长度  13.66/2 的倍数
        h = im_size[1] / 3.64  # 设置被切宽度  7.28/2的倍数
        x = 0  # 长
        y = 0  # 宽
        for i in range(4):  # 循环宽度4次
            for j in range(7):  # 循环长度7次
                region = im.crop((x, y, x + w, y + h))
                region.save("image200\\crop_average" + str(type) + "-%d-%d-%d.png" % (k , i , j));
                x = x + w;
                y = y;
            x = 0  # 高依次增加，宽度从0~~边界值
            y = y + h;

#截取测试图片，imageTest
def loginCut5(path,num):

    im = Image.open(path);
    im_size = im.size;
    print("login图片宽度和高度分别是{}".format(im_size));
    # 把图片平均分成10块
    # 第1块           个数
    w = im_size[0] / 6.83  # 设置被切长度  13.66/2 的倍数
    h = im_size[1] / 3.64 # 设置被切宽度      7.28/2的倍数
    x = 0  # 长
    y = 0  # 宽
    for i in range(4):  # 循环宽度8次
        for j in range(7):  # 循环长度14次
            region = im.crop((x, y, x + w, y + h))
            region.save("imageTests\\crop_average" + str(num) + "-%d-%d.png" % (i, j));
            x = x + w;
            y = y;
        x = 0  # 高依次增加，宽度从0~~边界值
        y = y + h;


#根据图片类型裁剪登录界面
def cutLoginPicByPicType(num):
    if(num==1):
        cutOneTypeLogin()
    elif(num==2):
        cutTwoTypeLogin()
    elif(num==3):
        cutThreeTypeLogin()
    else:
        print('该图片不属于该运行的三种范围')

#裁剪第一张微博登录界面
def cutOneTypeLogin():
    path='data\imageTest\\微博_t2.jpg'
    im = Image.open(path);
    im_size = im.size;
    print("login图片宽度和高度分别是{}".format(im_size));
    x = 940
    y = 165
    w = 300
    h = 290
    region = im.crop((x, y, x + w, y + h))
    im1=region.crop((0,0,155,50))
    im1.save('imageTypeCrop\one_1_1.png')
    im1=region.crop((155,0,300,50))
    im1.save('imageTypeCrop\one_1_2.png')

    im1=region.crop((0,50,300,100))
    im1.save('imageTypeCrop\one_1_3.png')
    im1 = region.crop((0, 100, 300, 150))
    im1.save('imageTypeCrop\one_1_4.png')

    im1 = region.crop((0, 150, 150, 170))
    im1.save('imageTypeCrop\one_1_5.png')
    im1 = region.crop((150, 150, 300, 170))
    im1.save('imageTypeCrop\one_1_6.png')

    im1 = region.crop((0, 170, 300, 220))
    im1.save('imageTypeCrop\one_1_7.png')
    im1 = region.crop((0, 220, 300, 250))
    im1.save('imageTypeCrop\one_1_8.png')
    im1 = region.crop((0, 250, 300, 280))
    im1.save('imageTypeCrop\one_1_9.png')


    region.save("imageTypeCrop\one_1.png")

#裁剪第二张移动登录界面
def cutTwoTypeLogin():
    path = 'data\imageTest\\移动_t2.jpg'
    im = Image.open(path);
    im_size = im.size;
    print("login图片宽度和高度分别是{}".format(im_size));
    x = 680
    y = 210 # 225
    w = 450
    h = 310 #310

    region = im.crop((x, y, x + w, y + h))
    region.save("imageTypeCrop\\two_2.png")

    im1 = region.crop((0, 0, 450, 35))
    im1.save('imageTypeCrop\\two_2_1.png')

    im1 = region.crop((0, 35, 225, 70))
    im1.save('imageTypeCrop\\two_2_2.png')
    im1 = region.crop((225, 35, 450, 70))
    im1.save('imageTypeCrop\\two_2_3.png')

    im1 = region.crop((0, 70, 140, 110))
    im1.save('imageTypeCrop\\two_2_4.png')
    im1 = region.crop((140, 70, 300, 110))
    im1.save('imageTypeCrop\\two_2_5.png')
    im1 = region.crop((300, 70,450, 110))
    im1.save('imageTypeCrop\\two_2_6.png')

    im1 = region.crop((0, 110, 140, 135))
    im1.save('imageTypeCrop\\two_2_7.png')
    im1 = region.crop((140, 110, 300, 135))
    im1.save('imageTypeCrop\\two_2_8.png')
    im1 = region.crop((300, 110, 450, 135))
    im1.save('imageTypeCrop\\two_2_9.png')

    im1=region.crop((0,135,450,165))
    im1.save('imageTypeCrop\\two_2_10.png')

    im1=region.crop((0,165,450,185))
    im1.save('imageTypeCrop\\two_2_11.png')

    im1=region.crop((0,185,450,225))
    im1.save('imageTypeCrop\\two_2_12.png')

    im1 = region.crop((0, 225, 450, 250))
    im1.save('imageTypeCrop\\two_2_13.png')

    im1 = region.crop((0, 250, 450, 275))
    im1.save('imageTypeCrop\\two_2_14.png')

    im1 = region.crop((0, 275, 450, 310))
    im1.save('imageTypeCrop\\two_2_15.png')


#裁剪第一张邮箱登录界面
def cutThreeTypeLogin():
    path = 'data\imageTest\\邮箱_t2.jpg'
    im = Image.open(path);
    im_size = im.size;
    print("login图片宽度和高度分别是{}".format(im_size));
    x = 780
    y = 210
    w = 300
    h = 460

    region = im.crop((x, y, x + w, y + h))
    region.save("imageTypeCrop\\three_3.png")

    im1 = region.crop((0, 0, 150, 50))
    im1.save("imageTypeCrop\\three_3_1.png")
    im1 = region.crop((150, 0, 300, 50))
    im1.save("imageTypeCrop\\three_3_2.png")

    im1 = region.crop((0, 85, 300, 135))
    im1.save("imageTypeCrop\\three_3_3.png")

    im1 = region.crop((0, 135, 300, 195))
    im1.save("imageTypeCrop\\three_3_4.png")

    im1 = region.crop((0, 195, 300, 245))
    im1.save("imageTypeCrop\\three_3_5.png")

    im1 = region.crop((0, 245, 150, 295))
    im1.save("imageTypeCrop\\three_3_6.png")
    im1 = region.crop((150, 245, 300, 295))
    im1.save("imageTypeCrop\\three_3_7.png")

    im1 = region.crop((0, 295, 300, 345))
    im1.save("imageTypeCrop\\three_3_8.png")

    im1 = region.crop((0, 345, 300, 395))
    im1.save("imageTypeCrop\\three_3_9.png")

    im1 = region.crop((0, 395, 300, 430))
    im1.save("imageTypeCrop\\three_3_10.png")

    im1 = region.crop((0, 430, 300, 460))
    im1.save("imageTypeCrop\\three_3_11.png")


if __name__ == "__main__":
    #im = Image.open("data\imageinit\\111.png")  # type:Image,Image
    #x=im.size
    #print(x)

    #裁剪imageinit里的三张图片
    #loginCut('data\imageinit\\111.png', 1)
    #loginCut('data\imageinit\\222.png', 2)
    #loginCut('data\imageinit\\333.png', 3)

    #cutPicLogin();
    #cropLogin2('data\imageinit\\111.png', 1);
    #cropLogin2('data\imageinit\\222.png', 2);
    #cropLogin2('data\imageinit\\333.png', 3);

    #截取50*100的图片，三种类型各14张
    #cutLoginType3('data\imageType3\\微博', 1)
    #cutLoginType3('data\imageType3\\移动', 2)
    #cutLoginType3('data\imageType3\\邮箱', 3)


    #截取200*200的图片，三种类型各14张
    #cutLoginType4('data\imageType3\\微博', 1)
    #cutLoginType4('data\imageType3\\移动', 2)
    #cutLoginType4('data\imageType3\\邮箱', 3)

    #qq和微信截图有区别,微信比QQ多2px
    #裁剪测试图片ImageTest
    #loginCut5('data\imageTest\\微博_t2.jpg', 1);#(1366, 728)
    #loginCut5('data\imageTest\\邮箱_t2.jpg', 3);#(1366, 728)
    loginCut5('data\imageTest\\移动_t2.jpg',2);#(1366, 738)

    #剪切图片
    #cutOneTypeLogin()
    #cutTwoTypeLogin()
    #cutThreeTypeLogin()
