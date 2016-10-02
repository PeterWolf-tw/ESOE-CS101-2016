#HW 1 the function
def bin2int(N):
    keyed=N
    power=0
    results=0
    left=0
    while N>0:  #一旦數字被操作完成(也就是所有位數被從後面被拔光)，就結束。
        leftovers=(N%10)   #取數字的最末一位(1or0)
        results+=(2**power)*leftovers    #取數字的最末一位乘上二的該位數的次方，"+"是用來sum up所有的results，否則結果只會出現二進位數值中，最大2次方數的值。(EX:101只出現4)
        N=N//10   #把最末一位拔掉，算下一個。
        power=power+1  #將次方提升1，因為由後往前2的次方運算完成就加一次，繼續進行迴圈。
        #print("{0} int {1}.".format(keyed,results)) 測試
    #print("{0} abc {1}.".format(N,results))  測試
    return results
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
def int2bin(N):
    tmpLIST = []
    while N > 0:
        remainder = int(N % 2)
        tmpLIST.append(remainder)
        N = (N - remainder) / 2
    tmpLIST.append(0)
    ans = ""
    for j in tmpLIST[::-1]: #將 tmpLIST 中的數字從尾至頭傳入 j
        ans = ans + str(j)
        ans1=int(ans)
    return ans1
#-------------------------------------------------------------------------------
#this little program was for finishing the HW with convinence.
#N=1
#while N>0:
 #   binder=input("key in=")
  #  binder1=int(binder)
   # S=bin2int(binder1)
    #print(S)
    #N=N+1
    
 #---------------------------------------------------------------------------------------------   
#作業 2. 課本 Ch2. P2.19
self.Ch2P2_19a = "10"
self.Ch2P2_19b = "17"
self.Ch2P2_19c = "6"
self.Ch2P2_19d = "8"

#作業 3. 課本 Ch2. P2.20
self.Ch2P2_20a = "13"
self.Ch2P2_20b = "7"
self.Ch2P2_20c = "12"
self.Ch2P2_20d = "3"

#作業 4. 課本 Ch2. P2.22
self.Ch2P2_22a = "00010001.11101010.00100010.00001110"
self.Ch2P2_22b = "00001110.00111000.11101010.00111000"
self.Ch2P2_22c = "01101110.00001110.00111000.01001110"
self.Ch2P2_22d = "00011000.00111000.00001101.00001011"    

#作業 5. 課本 Ch3. P3.28
self.Ch3P3_28a = "234"
self.Ch3P3_28b = "overflow"
self.Ch3P3_28c = "874"
self.Ch3P3_28d = "888"

#作業 6. 課本 Ch3. P3.30
self.Ch3P3_30a = "235"
self.Ch3P3_30b = "overflow"
self.Ch3P3_30c = "875"
self.Ch3P3_30d = "889"
