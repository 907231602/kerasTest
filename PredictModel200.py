#!/usr/bin/env python3.5.2
# -*- coding: utf-8 -*-
from keras.models import Sequential
import numpy as np
import picHandle
from keras import backend as K
from keras.models import load_model
import my_one_hot as ones
import ResultAnalysis as analysisType
import cutPic as cutPic


# input image dimensions
img_rows, img_cols =200,200
#训练的种类
nb_classes=3



# the data, shuffled and split between  test sets
(X_test, y_test) = picHandle.testPredictDataHandle200()
print(X_test.shape[0])



# 根据不同的backend定下不同的格式
if K.image_dim_ordering() == 'th':
    X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)
    #input_shape = (1, img_rows, img_cols)
else:
    X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)
    #input_shape = (img_rows, img_cols, 1)

X_test = X_test.astype('float32')
X_test /= 255
print(X_test.shape[0], 'test samples')

# 转换为one_hot类型
#Y_test = np_utils.to_categorical(y_test, nb_classes)
Y_test =ones.one_hot_ten(y_test,nb_classes)
print('one-hot-test:',Y_test)

# 构建模型
model = Sequential()
model=load_model('Cnn200.h5')
result=model.predict(X_test)
print(result)
listOne=result[0:28]
#listThree=result[28:]

oneResult=analysisType.resultType(listOne)
#threeResult=analysisType.resultType(listThree)
print('oneResult=',oneResult)
#print('threeResult=',threeResult)

cutPic.cutLoginPicByPicType(oneResult)




##结果分类
# print('total=',len(result))
#
# nb_type=2   #辨识图片种类
# num=len(result)/nb_type
# count=0
# indexNum=list();
# for kk in range(len(result)):
#     index=result[count].argmax()+1
#     indexNum.append(index)
#     count += 1
#
# print(indexNum)
# print('indexNum[0:28]:',indexNum[0:28])
# print('indexNum[28: ]:',indexNum[28:])
# list0_28=indexNum[0:28]
# print('pic1=',list0_28.count(1))
# print('pic1=',list0_28.count(2))
# print('pic1=',list0_28.count(3))









