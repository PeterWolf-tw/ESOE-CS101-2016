#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Python 程式的第一、二行一定是如上所示，請不要略過了。

def bin2int(N):
        List=0
        i=0
        end=len(str(N))
        for i in range(0,end):
                figure=(int(str(N)[end-i-1]))*2**i
                List=List+figure
        print("{0}的十進位表示法是{1}.".format(N,List))