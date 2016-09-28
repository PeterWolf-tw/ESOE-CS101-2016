#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def file2Text(fileName):
    '''
    f : file 類型的物件。依傳入的 fileName 開啟檔案。
    text: <檔案 f> 的內容。
    回傳 text 為 <檔案 f> 的內容。
    '''
    f = open(fileName, "r")
    text = f.read()
    return text