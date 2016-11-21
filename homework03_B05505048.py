def charFreqLister(inputSTR):
    LIST=[]
    inputSTR=input("string:")
    lena=len(inputSTR)
    List=[]
    [List.append(element) for element in inputSTR if element not in List]
    for element in List:
        z=inputSTR.count(element)
        w=z/lena
        LIST.append((w¡Aelement))
    LIST.sort(reverse=True)
    return LIST

    