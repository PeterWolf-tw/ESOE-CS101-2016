
#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 3. �ЧQ�ΥH�U�ťսd���]�p�@��{���C�{���i��J�@�q�r��A�æ۰ʭp��X�r�ꤤ�]�A�ťզr���X�{�����v�C
#    �åѰ��ƨ�C�C
#def charFreqLister(inputSTR):
#resultLIST = [(freq, char), (freq, char), (freq, char),...]

#return resultLIST


def charFreqLister(STR):     #�w�q�禡
    
    STR=input("Please enter some words: ")
    length=len(STR)   #�p��r���`���ץH�����
    resultLIST=[]     #�إߪŶ��X
    
    for n in STR:
        times=STR.count(n)    #�p��r�ꤤ�U�r���X�{������
        fre=times/length      #�Hfre��ܬ����v
        resultLIST.append((fre,n))    #�N��X���U�r�������v�[�i���e�ҫت����X
        
    resultLIST=set(resultLIST)     #�N�i���N�̫إ߬�set���A������
    resultLIST=list(resultLIST)    #�N�i���N�̫إ߬�list���A������
    resultLIST.sort(reverse=True)  #�blist���H�p��j�ƦC
    
    return(resultLIST)    #�^��


print(charFreqLister(""))