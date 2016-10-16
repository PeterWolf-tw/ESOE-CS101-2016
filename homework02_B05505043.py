def bin2int(N):
    list=[]
    a=0
    i=1
    while N>0:
        remainder= int(N%10)
        N=(N-remainder)/10
        a=a+remainder*i
        i=i*2
        
    return a

print(bin2int(N))

==================================================================
HW2-2
Ch2P2_19a = "10"
Ch2P2_19b = "17"
Ch2P2_19c = "6"
Ch2P2_19d = "8"
'''
def f(a):
    i=0
    while 2**i < a:
        i=i+1
    return i

print(f())
'''

==================================================================
HW2-3
Ch2P2_20a = "14"
Ch2P2_20b = "8"
Ch2P2_20c = "13"
Ch2P2_20d = "4"
==================================================================
HW2-4
Ch2P2_22a = "00010001  11101010  00100010  00001110"
Ch2P2_22b = "00001110  00111000  11101010  00111000"
Ch2P2_22c = "01101110  00001110  00111000  01001110"
Ch2P2_22d = "00011000  00111000  00001101  00001011"

'''
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def f(N):
    list=[]
    while N>0:
        a=int(N % 2)
        N=(N-a)/2
        list.append(a)
    list.append(0)
    b=""
    for j in list[::-1]:
        b=b+str(j)
    print("{0} 的二進位表示為 {1}.".format(N,b))
    return None
    
print(f())
'''
        
===================================================================
HW2-5
Ch3P3_28a = "234"
Ch3P3_28b = "560"
Ch3P3_28c = "874"
Ch3P3_28d = "888"

'''
def f(n):
    a=n
    n=str(n)
    if n[0]=="-":
        b=len(n)
        c=10**(b-1)-1+a
        print(c)
    else:
        print(n)
    return None
'''        
    
=====================================================================
HW2-6
Ch3P3_30a = "234"
Ch3P3_30b = "560"
Ch3P3_30c = "875"
Ch3P3_30d = "889"

'''
def f(n):
    a=n
    n=str(n)
    if n[0]=="-":
        b=len(n)
        c=10**(b-1)+a
        print(c)
    else:
        print(n)
    return None
'''        
