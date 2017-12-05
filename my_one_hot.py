#!/usr/bin/env python3.5.2
# -*- coding: utf-8 -*-
import numpy as np
#每张图2940
def to_one_hot(y,nb_class):
    len=y.shape[0]
    x=np.zeros(len*nb_class).reshape((len,nb_class))
    print('y[0]=',len)
    for i in range(len):
        print('i==',i)
        if(i<2940):
            x[i][0]=1
            continue
        elif(i<5880):
            x[i][1]=1
            continue
        else:
            x[i][2]=1


    print('one-->',x)
    return x

def one_hot_ten(y,nb_class):
    len=y.shape[0]
    x = np.zeros(len* nb_class).reshape((len, nb_class))
    print(y)
    print('ten=',len)
    for j in range(len):
        if(y[j]=='1'):
            x[j][0]=1
        elif(y[j]=='2'):
            x[j][1]=1
        else:
            x[j][2]=1
    return x


if __name__ == "__main__":

    y=one_hot_ten(3,4)
    print(y)