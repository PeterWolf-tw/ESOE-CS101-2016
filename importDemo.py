#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import myTools #直接取用已經寫好的 myTools.py 裡的東西，就不用一直重寫了。


# 根據 myTools.py 裡的 file2Text() 的結構，只要指定 fileName，file2Text() 就會把指定的檔案內容讀出來，並且回傳。
# 因為它會回傳 (return)，所以用個 amisSTR 和 sampleSTR 去承接 file2Text() 的回傳值。
amisSTR = myTools.file2Text("./Amis.txt")
sampleSTR = myTools.file2Text("./sample.txt")


# 如此一來，就可以寫一次程式，卻執行很多次了。
print(amisSTR)
print(sampleSTR)