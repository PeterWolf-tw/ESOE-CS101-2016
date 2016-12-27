#作業3
def charlistfreq(inputSTR):  
    L=len(inputSTR)#機率的分母
    inputSTR.lower()#把大寫都變小寫
    list1=[]#建一個list
    listWANT=[]#建立第二個表單
    for n in inputSTR:#對於每個在inputSTR裡面的字母
        M=inputSTR.count(n)#M＝數字母有幾個
        freq=M/L#求機率
        list1.append((n,freq))#在list1新增某個字母與他出現的頻率
 
    list1set=set(list1)#刪除list1重複的東西
    for e in list1set:#對於每個在list1set內的東西
        listWANT.append(e)
    listWANT.sort(reverse=True)
    
    return listWANT

#4
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
    outputSTR=""
    L=len(inputSTR_X)
    for n in range(L):
        if inputSTR_X[n]=="1" and inputSTR_Y[n]=="1":
            outputSTR=outputSTR+"1"
        else:
            outputSTR=outputSTR+"0"
            
    return outputSTR

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR=""
    L=len(inputSTR_X)
    for n in range[L]:
        if inputSTR_X[n]=="0" and inputSTR_Y[n]=="0":
            outputSTR=outputSTR+"0"
        else:
            outputSTR=outputSTR+"1"
    return outputSTR


#condition00 xor condition04
def conXOR(inputSTR_X, inputSTR_Y):
    outputSTR=""
    L=len(inputSTR_X)
    for n in range[L]:
        if inputSTR_X[n]==inputSTR_Y[n]:
            outputSTR=outputSTR+"0"
        else:
            outputSTR=outputSTR+"1"
    return outputSTR


# 5 請完成以下課本習題並將答案以字串型 (str or unicode) 填入。
print("Ans:")
Ch3P3_20a = "0 1000 0001 110 0110 0000 0000 0000 0000"
Ch3P3_20b = "1 1000 0010 100 1010 0100 0000 0000 0000"
Ch3P3_20c = "0 1000 0010 011 0110 1000 0000 0000 0000"
Ch3P3_20d = "1 0111 1101 100 0000 0000 0000 0000 0000"
print("========")
Ch3P3_28a = "234"
Ch3P3_28b = "overflow"
Ch3P3_28c = "874"
Ch3P3_28d = "888"
print("========")
Ch3P3_30a = "235"
Ch3P3_30b = "overflow"
Ch3P3_30c = "875"
Ch3P3_30d = "889"
print("========")
Ch4P4_3a = "1001 1001"
Ch4P4_3b = "1001 1001"
Ch4P4_3c = "1001 1001"
Ch4P4_3d = "1111 1111"
print("========")
Ch4P4_4a = ""
Ch4P4_4b = ""
Ch4P4_4c = ""
Ch4P4_4d = ""
print("========")
Ch4P4_13a = ""
Ch4P4_13b = ""
Ch4P4_13c = ""
Ch4P4_13d = ""
print("========")
Ch4P4_15a = ""
Ch4P4_15b = ""
Ch4P4_15c = ""
Ch4P4_15d = ""
print("========")
Ch4P4_16a = ""
Ch4P4_16b = ""
Ch4P4_16c = ""
Ch4P4_16d = ""

