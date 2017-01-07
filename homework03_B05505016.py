#!/usr/bin/env python3

# -*- coding:utf-8 -*-





# ú�����G2016.10.17



# �@�~���e�G

# 1. �о\Ū Wikipedia ����ʬ� IEEE754 ���� (https://zh.wikipedia.org/wiki/IEEE_754)



# 2. �иժ� http://armorgames.com/play/17826/logical-element



# 3. �ЧQ�ΥH�U�ťսd���]�p�@��{���C�{���i��J�@�q�r��A�æ۰ʭp��X�r�ꤤ�]�A�ťզr���X�{�����v�C

#    �åѰ��ƨ�C�C

def charFreqLister(inputSTR):

    resultLIST=[]

    NEWinputSTR = set(inputSTR)

    for char in NEWinputSTR:

        number=inputSTR.count(char)

        total=len(inputSTR)

        Freq=number/total

        resultLIST.append((Freq,char))

        resultLIST.sort()

        resultLIST.reverse()

    return resultLIST


# 3.1 �[���D (�������[���A�S��������)�G�ХνҰ󤤴��쪺�u�N�Ұҽs�X]

#     (https://zh.wikipedia.org/wiki/�N�Ұҽs�X) ���A���e�]�p��

#     �{���[�W��X���Y���\��C

# e.g.,

#def huffmanTranslater(inputSTR):

#resultLIST = [(freq, char, code), (freq, char, code), (freq, char, code),...]



#return resultLIST



# 4 �аѦҥH�U condNOT() ���Ҥl�A�]�p�|�� func() �̥H�U����A���X condition02 ~ 04 ����



#condition00 not condition01


def condNOT(inputSTR_X):

    outputSTR = ""

    for i in inputSTR_X:

        if i == "0":

            outputSTR = outputSTR + "1"

        else:

            outputSTR = outputSTR + "0"

    return outputSTR


#condition00 and condition02

def condAND(inputSTR_X, inputSTR_Y):

    outputSTR = ""

    for i in inputSTR_X:

        if i == "1":

            for j in inputSTR_Y:

                if j == "1":

                    outputSTR = outputSTR + "1"

                else:

                    outputSTR = outputSTR + "0"

        else:

            outputSTR = outputSTR + "0"

    return outputSTR

#condition00 or condition03

def condOR(inputSTR_X, inputSTR_Y):

    outputSTR = ""

    for i in inputSTR_X:

        if i == "0":

            for j in inputSTR_Y:

                if j == "1":

                    outputSTR = outputSTR + "1"

                else:

                    outputSTR = outputSTR + "0"

        else:

            outputSTR = outputSTR + "1"

    return outputSTR

#condition00 xor condition04

def condXOR(inputSTR_X, inputSTR_Y):

    outputSTR = ""

    for i in inputSTR_X:

        if i == "1":

            for j in inputSTR_Y:

                if j == "0":

                    outputSTR = outputSTR + "1"

                else:

                    outputSTR = outputSTR + "0"

        else:

            for j in inputSTR_Y:

                if j == "0":

                    outputSTR = outputSTR + "0"

                else:

                    outputSTR = outputSTR + "1"

    return outputSTR


if __name__== "__main__":

    condition00X = "010111001010100001100011"

    condition00Y = "010000110001011100101001"



    condition01 = condNOT(condition00X)

    print(condition01)
    
    
    
# 5 �Ч����H�U�ҥ����D�ñN���ץH�r�ꫬ (str or unicode) ��J�C


print("Ans:")

Ch3P3_20a = "01000001011001100000000000000000"

Ch3P3_20b = "11000001110010100100000000000000"

Ch3P3_20c = "01000001101101101000000000000000"

Ch3P3_20d = "10111110110000000000000000000000"

print("========")

Ch3P3_28a = "234"

Ch3P3_28b = "Overflow"

Ch3P3_28c = "874"

Ch3P3_28d = "888"

print("========")

Ch3P3_30a = "234"

Ch3P3_30b = "Overflow"

Ch3P3_30c = "875"

Ch3P3_30d = "889"

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

Ch4P4_15a = "Overflow"

Ch4P4_15b = "Not Overflow"

Ch4P4_15c = "Not Overflow"

Ch4P4_15d = "Overflow"

print("========")

Ch4P4_16a = "0F51"

Ch4P4_16b = "10F2A"

Ch4P4_16c = "8012"

Ch4P4_16d = "17F51"
