#!/usr/bin/env python3.5.2
# -*- coding: utf-8 -*-

#结果分析：
def resultType(result):
    #print('total=', len(result))

    nb_type = 2  # 辨识图片种类
    num = len(result) / nb_type
    count = 0
    indexNum = list();
    for kk in range(len(result)):
        index = result[count].argmax() + 1
        indexNum.append(index)
        count += 1

    #print(indexNum)
    #print('indexNum[0:28]:', indexNum[0:28])
    #print('indexNum[28: ]:', indexNum[28:])
    list0_28 = indexNum[0:28]
    #print('pic1=', list0_28.count(1))
    #print('pic1=', list0_28.count(2))
    #print('pic1=', list0_28.count(3))
    index1=list0_28.count(1);
    index2=list0_28.count(2)
    index3=list0_28.count(3)
    #print('最大值=',max([index1,index2,index3]))
    maxValue=max([index1,index2,index3])
    if(index1==maxValue):
        return 1
    elif(index2==maxValue):
        return 2
    else:
        return 3




