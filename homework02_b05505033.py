#HW 1 the function
def bin2int(N):
    keyed=N
    power=0
    results=0
    left=0
    while N>0:  #�@���Ʀr�Q�ާ@����(�]�N�O�Ҧ���ƳQ�q�᭱�Q�ޥ�)�A�N�����C
        leftovers=(N%10)   #���Ʀr���̥��@��(1or0)
        results+=(2**power)*leftovers    #���Ʀr���̥��@�쭼�W�G���Ӧ�ƪ�����A"+"�O�Ψ�sum up�Ҧ���results�A�_�h���G�u�|�X�{�G�i��ƭȤ��A�̤j2����ƪ��ȡC(EX:101�u�X�{4)
        N=N//10   #��̥��@��ޱ��A��U�@�ӡC
        power=power+1  #�N���责��1�A�]���ѫ᩹�e2������B�⧹���N�[�@���A�~��i��j��C
        #print("{0} int {1}.".format(keyed,results)) ����
    #print("{0} abc {1}.".format(N,results))  ����
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
    for j in tmpLIST[::-1]: #�N tmpLIST �����Ʀr�q�����Y�ǤJ j
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
#�@�~ 2. �ҥ� Ch2. P2.19
self.Ch2P2_19a = "10"
self.Ch2P2_19b = "17"
self.Ch2P2_19c = "6"
self.Ch2P2_19d = "8"

#�@�~ 3. �ҥ� Ch2. P2.20
self.Ch2P2_20a = "13"
self.Ch2P2_20b = "7"
self.Ch2P2_20c = "12"
self.Ch2P2_20d = "3"

#�@�~ 4. �ҥ� Ch2. P2.22
self.Ch2P2_22a = "00010001.11101010.00100010.00001110"
self.Ch2P2_22b = "00001110.00111000.11101010.00111000"
self.Ch2P2_22c = "01101110.00001110.00111000.01001110"
self.Ch2P2_22d = "00011000.00111000.00001101.00001011"    

#�@�~ 5. �ҥ� Ch3. P3.28
self.Ch3P3_28a = "234"
self.Ch3P3_28b = "overflow"
self.Ch3P3_28c = "874"
self.Ch3P3_28d = "888"

#�@�~ 6. �ҥ� Ch3. P3.30
self.Ch3P3_30a = "235"
self.Ch3P3_30b = "overflow"
self.Ch3P3_30c = "875"
self.Ch3P3_30d = "889"
