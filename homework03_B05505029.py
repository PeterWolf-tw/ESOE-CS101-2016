
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
    resultLIST.sort(reverse=True)  #�blist���H�j��p�ƦC
    
    return(resultLIST)    #�^��




# 4 �аѦҥH�U condNOT() ���Ҥl�A�]�p�|�� func() �̥H�U����A���X condition02 ~ 04 ����

#condition00 not condition01
def condNOT(inputSTR_X):
    outputSTR = ""
    for h in inputSTR_X:
        if h == "0":      #�binputSTR_X�Y��0
            outputSTR = outputSTR + "1"    #�h���G��1
        else:    #�binputSTR_X�Y��1
            outputSTR = outputSTR + "0"   #�h���G��0 
    return outputSTR

#condition00 and condition02
def condAND(inputSTR_X, inputSTR_Y):
    
    outputSTR=""
    
    for h in range(0,len(inputSTR_X)) :      
        if inputSTR_X[h]=="1" :    #�YinputSTR_X����h������1
            if inputSTR_Y[h]=="1" :   #�YinputSTR_Y����h������1
                outputSTR=outputSTR+"1"    #���G��1
            else :                    #�YinputSTR_Y����h������0
                outputSTR=outputSTR+"0"    #���G��0
        else:                      #�YinputSTR_X����h������0
            outputSTR=outputSTR+"0"       #���G�@�߬�0
      
    return outputSTR

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    
    outputSTR=""
    
    for h in range(0,len(inputSTR_X)) :      
        if inputSTR_X[h]=="0" :        #�Y�Y����h������0
            if inputSTR_Y[h]=="0" :         #�YinputSTR_Y����h������0
                outputSTR=outputSTR+"0"         #���G��0
            else :                          #�YinputSTR_Y����h������1
                outputSTR=outputSTR+"1"         #���G��1
        else:                          #�YinputSTR_X����h������1
            outputSTR=outputSTR+"1"             #���G�@�߬�1
    
    return outputSTR


#condition00 xor condition04
def condXOR(inputSTR_X, inputSTR_Y):
    
    outputSTR=""
    for h in range(0,len(inputSTR_X)) : 
        if inputSTR_X[h]==inputSTR_Y[h] :    #�YinputSTR_X����h�Ӥ����PinputSTR_Y����h�Ӥ����ۦP
            outputSTR=outputSTR+"0"               #���G��0
        else :                               #�YinputSTR_X����h�Ӥ����PinputSTR_Y����h�Ӥ������P
            outputSTR=outputSTR+"1"               #���G��1
    return outputSTR


if __name__== "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"

    condition01 = condNOT(condition00X)
    print(condition01)
    
    condition02 = condAND(condition00X,condition00Y)
    print(condition02)
    
    condition03 = condOR(condition00X,condition00Y)
    print(condition03)    
    
    condition04 = condXOR(condition00X,condition00Y)
    print(condition04)    

