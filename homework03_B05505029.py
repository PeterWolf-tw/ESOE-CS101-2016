
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

 # 5 �Ч����H�U�ҥ����D�ñN���ץH�r�ꫬ (str or unicode) ��J�C
    print("Ans:")
    Ch3P3_20a = "0100 0000 1110 0110 0000 0000 0000 0000"
    Ch3P3_20b = "1100 0001 0100 1010 0100 0000 0000 0000"
    Ch3P3_20c = "0100 0001 0011 0110 1000 0000 0000 0000"
    Ch3P3_20d = "1011 1110 1100 0000 0000 0000 0000 0000"
    print("========")
    Ch3P3_28a = "765"
    Ch3P3_28b = "439"
    Ch3P3_28c = "-874"
    Ch3P3_28d = "-888"
    print("========")
    Ch3P3_30a = "766"
    Ch3P3_30b = "440"
    Ch3P3_30c = "-875"
    Ch3P3_30d = "-889"
    print("========")
    Ch4P4_3a = "0x99"
    Ch4P4_3b = "0x99"
    Ch4P4_3c = "0xFF"
    Ch4P4_3d = "0xFF"
    print("========")
    Ch4P4_4a = "0x66"
    Ch4P4_4b = "0xFF"
    Ch4P4_4c = "0x11"
    Ch4P4_4d = "0xBB"
    print("========")
    Ch4P4_13a = "1184"
    Ch4P4_13b = "-862"
    Ch4P4_13c = "862"
    Ch4P4_13d = "-1184"
    print("========")
    Ch4P4_15a = "overflow"
    Ch4P4_15b = "not overflow"
    Ch4P4_15c = "not overflow"
    Ch4P4_15d = "overflow"
    print("========")
    Ch4P4_16a = "0x0F51"
    Ch4P4_16b = "overflow"
    Ch4P4_16c = "0x8012"
    Ch4P4_16d = "overflow"
