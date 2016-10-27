#!/usr/bin/env python3
# -*- coding:utf-8 -*-



#這是功課3，只做了英文小寫和空白鍵

def countingstar(inputstr):
    inputstr=str(inputstr)
    total = len(str(inputstr))

    space=[" "]
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    h=0
    i=0
    j=0
    k=0
    l=0
    m=0
    n=0
    o=0
    p=0
    q=0
    r=0
    s=0
    t=0
    u=0
    v=0
    w=0
    x=0
    y=0
    z=0
    space[0] = 0

    
    for na in inputstr:
        if na == "a":
            a=a+1
            
        elif na =="b":
            b=b+1
        elif na =="c":
            c=c+1
        elif na =="d":
            d=d+1
        elif na =="e":
            e=e+1
        elif na =="f":
            f=f+1
        elif na =="g":
            g=g+1
        elif na =="h":
            h=h+1
        elif na =="i":
            i=i+1
        elif na =="j":
            j=j+1
        elif na =="k":
            k=k+1
        elif na =="l":
            l=l+1
        elif na =="m":
            m=m+1
        elif na =="n":
            n=n+1
        elif na =="o":
            o=o+1
        elif na =="p":
            p=p+1
        elif na =="q":
            q=q+1
        elif na =="r":
            r=r+1
        elif na =="s":
            s=s+1
        elif na =="t":
            t=t+1
        elif na =="u":
            u=u+1
        elif na =="v":
            v=v+1
        elif na =="w":
            w=w+1
        elif na =="x":
            x=x+1
        elif na =="y":
            y=y+1
        elif na =="z":
            z=z+1
        elif na ==" ":
            space[0]=space[0]+1

    那該死的list = [(a/total,"a"),(b/total,"b"),(c/total,"c")
                   ,(d/total,"d"),(e/total,"e"),(f/total,"f")
                   ,(g/total,"g"),(h/total,"h"),(i/total,"i")
                   ,(j/total,"j"),(k/total,"k"),(l/total,"l")
                   ,(m/total,"m"),(n/total,"n"),(o/total,"o")
                   ,(p/total,"p"),(q/total,"q"),(r/total,"r")
                   ,(s/total,"s"),(t/total,"t"),(u/total,"u")
                   ,(v/total,"v"),(w/total,"w"),(x/total,"x")
                   ,(y/total,"y"),(z/total,"z"),(space[0]/total,"空白鍵")]
  


    小到大list = sorted(那該死的list, key = lambda x : x[0])
    大到小list = sorted(小到大list, reverse = True)
    return 大到小list
    

ppap=input("打字先")

answer=countingstar(ppap)
print(answer)


####################################

#這是作業4

def condAND(inputSTR_X,inputSTR_Y):
    outputSTR = ""
    for i in range(0,len(inputSTR_X)):
        if inputSTR_X[i] == inputSTR_Y[i] == "1":
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"

    return outputSTR


def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""

    for i in range(0,len(inputSTR_X)):

        if inputSTR_X[i] == "1":
            outputSTR = outputSTR + "1"

        elif inputSTR_Y[i] == "1":
            outputSTR = outputSTR + "1"
    
        else:
            outputSTR = outputSTR + "0"

    return outputSTR



def condXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""

    for i in range(0,len(inputSTR_X)):

        if inputSTR_X[i] == "1" and inputSTR_Y[i] == "0":
            outputSTR = outputSTR + "1"

        elif inputSTR_Y[i] == "1" and inputSTR_X[i] == "0":
            outputSTR = outputSTR + "1"
    
        else:
            outputSTR = outputSTR + "0"

    return outputSTR


if __name__== "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"


    condition02 = condAND(condition00X,condition00Y)
    print(condition02)

    condition03 = condOR(condition00X,condition00Y)
    print(condition03)

    condition04 = condXOR(condition00X,condition00Y)
    print(condition04)








