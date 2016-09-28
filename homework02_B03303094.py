#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def bin2int(n):
    list=[]
    m=n
    while int(m)>0:
        x=int(m)%10
        list.append(x)
        m=int(m)//10
    ans=0
    while True:
        try:
            ans=ans+list[0]
            del list[0]
            list=[i*2 for i in list]
        except:
            break
    print("{0} 的十進位表示為 {1}.".format(n,ans))
    return None
