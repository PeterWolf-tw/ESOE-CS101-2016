#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Please always remember to use these two lines!

class HW02:
    def ch2(self):
        '''
        �бN�A�p��X�Ӫ����׶�J�H�U�ܼơA�U�з|�g�{���۰ʧ��C
        Ch2P2_19a = "xxx"
        �N��O
        Ch2   : �ĤG��
        P2_19a: �ĤG�������B�� PRACTICE SET �q���B�� Problems �� P2-19 �D�� a �p�D
        "xxx" �G �A�n��J�A�����a��C
        #�@�~ 2. �ҥ� Ch2. P2.19        '''
        self.Ch2P2_19a="010"
        self.Ch2P2_19b="017"
        self.Ch2P2_19c="006"
        #Ch2P2_19d = "???"
        #�@�~ 3. �ҥ� Ch2. P2.20
        self.Ch2P_20a="014"
        self.Ch2P_20b="008"
        self.Ch2P_20c="013"
        self.Ch2P_20d="004"  #"6"
        #�@�~ 4. �ҥ� Ch2. P2.22
        self.Ch2P_22a="00010001 11101010 00100010 00001110"
        self.Ch2P_22b="00001110 00111000 11101010 00111000"
        self.Ch2P_22c="01101110 00001110 00111000 01001110"
        self.Ch2P_22d="00011000 00111000 00001101 00001011"
    def ch3(self):
        '''
        �бN�A�p��X�Ӫ����׶�J�H�U�ܼơA�U�з|�g�{���۰ʧ��C
        Ch3P3_28a = "xxx"
        �N��O
        Ch3   : �ĤT��
        P3_28a: �ĤT�������B�� PRACTICE SET �q���B�� Problems �� P3-28 �D�� a �p�D
        "xxx" �G �A�n��J�A�����a��C
        '''
        #�@�~ 5. �ҥ� Ch3. P3.28
        self.Ch3P_28a="234"
        self.Ch3P_28b="560"
        self.Ch3P_28c="874"
        self.Ch3P_28d="888"
        #�@�~ 6. �ҥ� Ch3. P3.30
        self.Ch3P_30a="234"
        self.Ch3P_30b="560"
        self.Ch3P_30c="875"
        self.Ch3P_30d="889"

        if __name__ == '__main__': #�{���i�J�I�A�{���Ѧ���}�l����C�H�U�ܽd�U�Ъ����{���C
            checkHW02 = HW02()
            checkHW02.ch2()
            if checkHW02.Ch2P2_19a == 10: #10 �O�o�D�����ѡC�����ˬd�o�D�����סC
                print("Ch2P2_19a:{0}".format("Correct!"))
            else:
                print("Ch2P2_19a:{0}".format("Incorrect!"))



#1
def int2bin(N):
    G=[]
    while N > 0:
        gg=int(N%2)
        G.append(gg)
        N=(N-gg)/2
    G.append(0)

    ans=""
    for n in G[::-1]:
        ans=ans+str(n)
    print("{0},{1}".format(N,ans))
    return None
