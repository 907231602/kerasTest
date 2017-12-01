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
    #print(im_array)
    #print(len(im_array))
    #print(len(im_array[1]))
    return im_array

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
    X = np.array(X)
    Y = np.array(Y)

    return(X,Y)

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
    print(len(X))
    X = np.array(X)
    Y = np.array(Y)
    return(X,Y)
