#class HW02-1
def bin2int(N):
        # 本函式將 bin 二進位制表示數轉為 int 整數
        List=0    
        for i in range(0,len(str(N))):
                figure=(int(str(N)[len(str(N))-i-1]))*2**i
                List=List+figure
        print("{0}的十進位表示法是{1}.".format(N,List))


 class HW02:
	def ch2(self):
          #作業 2. 課本 Ch2. P2.19
	  #suppose all signs are positive
          self.Ch2P2_19a = "10"
          self.Ch2P2_19b = "17"
          self.Ch2P2_19c = "6"
          self.Ch2P2_19d = "8"

          #作業 3. 課本 Ch2. P2.20
          self.Ch2P2_20a = "14"
          self.Ch2P2_20b = "8"
          self.Ch2P2_20c = "13"
          self.Ch2P2_20d = "4"

          #作業 4. 課本 Ch2. P2.22
          self.Ch2P2_22a = "00010001 11101100 00100010 00001110"
          self.Ch2P2_22b = "01101110 00001110 00111000 01001110"
          self.Ch2P2_22c = "00001110 00111000 11101100 00111000"
          self.Ch2P2_22d = "00011000 00111000 00011001 00001011"
          
        def ch3(self):

          #作業 5. 課本 Ch3. P3.28
          self.Ch3P3_28a = "234"
          self.Ch3P3_28b = "560"
          self.Ch3P3_28c = "874"
          self.Ch3P3_28d = "888"

          #作業 6. 課本 Ch3. P3.30
          self.Ch3P3_30a = "234"
          self.Ch3P3_30b = "560"
          self.Ch3P3_30c = "875"
          self.Ch3P3_30d = "889"

if __name__ == '__main__': #程式進入點，程式由此行開始執行。以下示範助教的批改程式。
    checkHW02 = HW02()
    checkHW02.ch2()
    if checkHW02.Ch2P2_19a == "10": #10 是這題的正解。此行檢查這題的答案。
            #Let me ask a question:要加""嗎？
        print("Ch2P2_19a:{0}".format("Correct!"))
    else:
        print("Ch2P2_19a:{0}".format("Incorrect!"))
