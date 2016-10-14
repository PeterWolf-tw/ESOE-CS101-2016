# 4 請參考以下 condNOT() 的例子，設計四個 func() 依以下條件，能算出 condition02 ~ 04 的值

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
def condAND(inputSTR_X,inputSTR_Y):
	outputSTR=""
	if len(inputSTR_X)>len(inputSTR_Y):
		A=len(inputSTR_Y)
	else:
		A=len(inputSTR_X)
	for i in range(0,A):
		if inputSTR_X[i]==inputSTR_Y[i]=="0":
			outputSTR+="1"
		else:
			outputSTR+="0"
	return outputSTR

#condition00 or condition03
def condOR(inputSTR_X,inputSTR_Y):
	outputSTR=""
	if len(inputSTR_X)>len(inputSTR_Y):
		B=len(inputSTR_Y)
	else:
		B=len(inputSTR_X)
	for i in range(0,B):
		if inputSTR_X[i]=="0":
			outputSTR+="1"
		elif inputSTR_Y[i]=="0":
			outputSTR+="1"
		else:
			outputSTR+="0"
	return outputSTR
#condition00 xor condition04
def conXOR(inputSTR_X,inputSTR_Y):
	outputSTR=""
	if len(inputSTR_X)>len(inputSTR_Y):
		C=len(inputSTR_Y)
	else:
		C=len(inputSTR_X)
	for i in range(0,C):
		if inputSTR_X[i]!="0":
			outputSTR+="1"
		elif inputSTR_Y[i]!="0":
			outputSTR+="1"
		else:
			outputSTR+="0"
	return outputSTR
