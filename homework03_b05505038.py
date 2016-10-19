#!/usr/bin/env python3
    +# -*- coding:utf-8 -*-
    +
    +
    +# ú�����G2016.10.17
    +
    +# �@�~���e�G
    +# 1. �о\Ū Wikipedia ����ʬ� IEEE754 ���� (https://zh.wikipedia.org/wiki/IEEE_754)
    +
    +# 2. �иժ� http://armorgames.com/play/17826/logical-element
    +
    +# 3. �ЧQ�ΥH�U�ťսd���]�p�@��{���C�{���i��J�@�q�r��A�æ۰ʭp��X�r�ꤤ�]�A�ťզr���X�{�����v�C
    +#    �åѰ��ƨ�C�C
    
    +#def charFreqLister(inputSTR):
    +#resultLIST = [(freq, char), (freq, char), (freq, char),...]
    +
    +#return resultLIST
    def charFreqLister(inputSTR):
        
        character=input("�п�J��r")
        print("��J��r��:",character)
        
         characterLen=len(character)#�p���r����
       
        resultLIST=[]
        
        for x in character:
            arise=character.count(x)#��r�X�{����
            frequency=arise/characterLen#���v
            resultLIST.extend((frequency,x))#��o�ө�J
            s=set(resultLIST)
            resultLIST=list(s)
            resultLIST.sort(resyltLIST,key=itemgetter(0), reverse= True)
            return resultLIST
    +# 3.1 �[���D (�������[���A�S��������)�G�ХνҰ󤤴��쪺�u�N�Ұҽs�X]
    +#     (https://zh.wikipedia.org/wiki/�N�Ұҽs�X) ���A���e�]�p��
    +#     �{���[�W��X���Y���\��C
    +# e.g.,
    +#def huffmanTranslater(inputSTR):
    +#resultLIST = [(freq, char, code), (freq, char, code), (freq, char, code),...]
    +
    +#return resultLIST
    +
    +# 4 �аѦҥH�U condNOT() ���Ҥl�A�]�p�|�� func() �̥H�U����A���X condition02 ~ 04 ����
    +
    +#condition00 not condition01
    +def condNOT(inputSTR_X):
    +    outputSTR = ""
    +    for i in inputSTR_X:
    +        if i == "0":
    +            outputSTR = outputSTR + "1"
    +        else:
    +            outputSTR = outputSTR + "0"
    +    return outputSTR
    +
    +
    +#condition00 and condition02
    +def condAND(inputSTR_X, inputSTR_Y):
    +outputSTR =" "
     for(x,y)in zip(inputSTR_X, inputSTR_Y):
     if x=="1"and y=="1":
     outputSTR+="1"
     else:
          outputSTR+="0"
   return outputSTR 
    return
    +
    +#condition00 or condition03
    +def condOR(inputSTR_X, inputSTR_Y):
    +  outputSTR =" "
       for(x,y)in zip(inputSTR_X, inputSTR_Y):
       if x=="0" or y=="0":
        outputSTR+="0"
        else:
            outputSTR+="1"   
    return
    +
    +#condition00 xor condition04
    +def conXOR(inputSTR_X, inputSTR_Y):
    + outputSTR=" "
      for(x,y)in zip(inputSTR_X, inputSTR_Y):
      if x==y:
            outputSTR+="0"
        else:
            outputSTR+="1"   
    return
    +
    +
    +if __name__== "__main__":
    +    condition00X = "010111001010100001100011"
    +    condition00Y = "010000110001011100101001"
    +
    +    condition01 = condNOT(condition00X)
    +    print(condition01)
    +
    +    # 5 �Ч����H�U�ҥ����D�ñN���ץH�r�ꫬ (str or unicode) ��J�C
    +    print("Ans:")
    +    Ch3P3_20a = "01000000111001100000000000000000"
    +    Ch3P3_20b = "11000000110101001000000000000000"
    +    Ch3P3_20c = "01000001001101101000000000000000"
    +    Ch3P3_20d = "10111110110000000000000000000000"
    +    print("========")
    +    Ch3P3_28a = "234"
    +    Ch3P3_28b = "overfiow"
    +    Ch3P3_28c = "874"
    +    Ch3P3_28d = "888"
    +    print("========")
    +    Ch3P3_30a = "234"
    +    Ch3P3_30b = "560"
    +    Ch3P3_30c = "875"
    +    Ch3P3_30d = "888"
    +    print("========")
    +    Ch4P4_3a = "99"
    +    Ch4P4_3b = "99"
    +    Ch4P4_3c = "FF"
    +    Ch4P4_3d = "FF"
    +    print("========")
    +    Ch4P4_4a = "66"
    +    Ch4P4_4b = "FF"
    +    Ch4P4_4c = "11"
    +    Ch4P4_4d = "BB"
    +    print("========")
    +    Ch4P4_13a = "1184"
    +    Ch4P4_13b = "-862"
    +    Ch4P4_13c = "862"
    +    Ch4P4_13d = "-1184"
    +    print("========")
    +    Ch4P4_15a = "overflow"
    +    Ch4P4_15b = "overflow"
    +    Ch4P4_15c = "no overflow"
    +    Ch4P4_15d = "overflow"
    +    print("========")
    +    Ch4P4_16a = "0x1051"
    +    Ch4P4_16b = "overflow"
    +    Ch4P4_16c = "0x8012"
    +    Ch4P4_16d = "overflow"