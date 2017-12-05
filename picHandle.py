from PIL import Image
import numpy as np
import os
import random
#灰度处理
def imageHanle(imgName):
    imageHandle = Image.open(imgName)
    #imageHandle.show()
    L= imageHandle.convert('L')   #转化为灰度图
    #L = imageHandle.convert('1')   #转化为二值化图
    #L.show
    im_array = np.array(L)
    #print('im_array=',im_array)
    #print(len(im_array))
    #print(len(im_array[1]))
    return im_array

#获取image下的所有图片进行训练，并进行标注是那种类型图片，灰度化后的图片
def trainDataHandle():
    X = list()
    Y = list()
    files = os.listdir('image')
    for item in files:
        ele = item.split('e')
        picCat = ele[2].split('-')[0]
        #print(item)
        #print(picCat)
        X.append(imageHanle('image/'+item))
        Y.append(picCat)
    print('000-->',X)
    x = np.array(X)
    print('type(x)===',type(x))
    print('111-->',x)
    y = np.array(Y)

    return(x,y)




#获取image下面的随机10张图片进行测试用，灰度化后的图片
def testDataHandle():
    X = list()
    Y = list()
    files = os.listdir('image')
    for item in random.sample(files,10):
        ele = item.split('e')
        picCat = ele[2].split('-')[0]
        #print(item)
        #print(picCat)
        X.append(imageHanle('image/' + item))
        Y.append(picCat)
    #print(len(X))
    #print('x--->',X)
    #print('x--->', type(X))
    X = np.array(X)
    Y = np.array(Y)
    return(X,Y)



#获取image下的所有图片进行训练，并进行标注是那种类型图片，灰度化后的图片
def trainDataHandle2():
    X = list()
    Y = list()
    files = os.listdir('image1')
    for item in files:
        ele = item.split('e')
        picCat = ele[2].split('-')[0]
        #print(item)
        #print(picCat)
        X.append(imageHanle('image1/'+item))
        Y.append(picCat)
    #print(X)
    X = np.array(X)
    print(X)
    Y = np.array(Y)
    return(X,Y)


#获取image下面的随机10张图片进行测试用，灰度化后的图片
def testDataHandle2():
    X = list()
    Y = list()
    files = os.listdir('image1')
    for item in random.sample(files,10):
        ele = item.split('e')
        picCat = ele[2].split('-')[0]
        #print(item)
        #print(picCat)
        X.append(imageHanle('image1/' + item))
        Y.append(picCat)
    #print('x===,',X)
    x = np.array(X)  #.reshape(1,10,100,100)
    #print('x==>',x)
    y = np.array(Y)
    return(x,y)

#image1训练的图片，通过循环把解析的图片的维度放入数组中
def trainDataHandle22():
    area = np.zeros(shape=(210,49,100))
    files = os.listdir('image1')
    Y=list()

    #for item in files:

    for j in range(210):
        item=files[j]
        ele = item.split('e')
        picCat = ele[2].split('-')[0]

        area[j]=imageHanle('image1/' + item)
        Y.append(picCat)

    return area,Y

#image1测试的图片，通过循环把解析的图片的维度放入数组中
def testDataHandle22():
    area = np.zeros(shape=(10,49,100))

    Y = list()
    files = os.listdir('image1')
    for j in range(10):
        item = random.sample(files, 10)
        print('item=',item)
        ele = item.split('e')
        picCat = ele[2].split('-')[0]
        area[j]= imageHanle('image1/' + item)
        Y.append(picCat)
    return area,Y

#image3训练的图片，把图片的黑白化，然后把维度存放到X.list中，对应的图片类别也放到相应的Y.list中
def trainDataHandle3():
    X = list()
    Y = list()
    files = os.listdir('image3')
    for item in files:
        ele = item.split('e')
        picCat = ele[2].split('-')[0]
        X.append(imageHanle('image3/' + item))
        Y.append(picCat)
    x = np.array(X)
    y = np.array(Y)

    return (x, y)
#image3训练的图片
def testDataHandle3():
    X = list()
    Y = list()
    files = os.listdir('image3')
    for item in random.sample(files, 10):
        ele = item.split('e')
        picCat = ele[2].split('-')[0]
        X.append(imageHanle('image3/' + item))
        Y.append(picCat)
        print('Y-->',Y)
    x = np.array(X)
    y = np.array(Y)
    print('y==>>',y)
    return (x, y)

#image200训练的图片，把图片的黑白化，然后把维度存放到X.list中，对应的图片类别也放到相应的Y.list中
def trainDataHandle200():
    X = list()
    Y = list()
    files = os.listdir('image200')
    for item in files:
        ele = item.split('e')
        picCat = ele[2].split('-')[0]
        X.append(imageHanle('image200/' + item))
        Y.append(picCat)
    x = np.array(X)
    y = np.array(Y)
    return (x, y)

#image200训练的图片
def testDataHandle200():
    X = list()
    Y = list()
    files = os.listdir('image200')
    for item in random.sample(files, 10):
        ele = item.split('e')
        picCat = ele[2].split('-')[0]
        X.append(imageHanle('image200/' + item))
        Y.append(picCat)
        print('Y-->',Y)
    x = np.array(X)
    y = np.array(Y)
    print('y==>>',y)
    return (x, y)