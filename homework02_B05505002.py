#帳號未授權,借同學帳號上傳
number=input("請輪入一個數字：")
number2=int(number)
n=0
while 10**n<=number2:
    n=n+1
n=n-1
k=0
while n>=0:
    t=number2//10**n
    k=k*2
    k=k+t
    number2=number2-t*(10**n)
    n=n-1
print(k)
