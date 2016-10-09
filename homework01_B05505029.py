#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼

c=open("sample.txt",encoding='utf8')
d=c.read()
sampleWordList = []

#��sampleWordList�إߤ@�Ӷ��X

d=d.replace("?"," ")
d=d.replace("-"," ")
d=d.replace("."," ")
d=d.replace(","," ")
d=d.replace("\n," ")

#�N���I�Ÿ������קK���J�r�Ƥ�

c=d.split(" ")

#�N���ɮ��ର�C��

for a in c:
    if len(a) > 5:
        sampleWordList.append(a)

#��r�Ƥj�󤭪��r�[�JsampleWordList

print(sampleWordList)
