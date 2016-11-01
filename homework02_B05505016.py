#!/usr/bin/env python3

# -*- coding:utf-8 -*-





#<�о�>

# �H "#" �r�Ÿ��}�Y�����e�N�Q Python �����u���ѡv�C���|����C



# #########################################����########################################

# �� Python �Ө��A if __name__ == "__main__" �Y���{�����i�J�I�C�@�ӵ{���u�঳�u�@�ӡv�i�J�I�C

# �������A���{���q�o�@��}�l����C



#def sayHi():

    #'''

    #�o�̩w�q�F�@�Ө禡�A�W�s sayHi

    #'''

    # #�o��禡�ߤ@���\��N�O�L�X�U���o�@�y�ܡK

    #print("Hi�I�o�O�@��u�|�� Hi ���禡�C")







#if __name__ == '__main__': #�o�̬O�{���i�J�I�C���{���q�o�̶}�l����K

    # #�H�U���� sayHi() �禡

    #sayHi()



#</�о�>

# #####################################################################################





number = 100  #�]�w number �o���ܼƪ��Ȭ� 2

print("number ���G�i���ܪk���G{0}".format(bin(number))) #�N 2 ���J bin(n) �禡���A�ç� bin(n) �^�Ǫ����G�A�������� print() ��X�b�ù��e���W�C



# �A�i�H�յۧ� number ���ȧאּ�䥦���Ʀr�A�[��ݬݡC



# bin(n) ����z�j�P�p�U�G

def int2bin(N):

    '''

    ���禡�N int ����ର bin �G�i����ܡC�@�ε��P�� bin(N)

    '''

    tmpLIST = []

    while N > 0:

        remainder = int(N % 2)

        tmpLIST.append(remainder)

        N = (N - remainder) / 2

    tmpLIST.append(0)



    ans = ""

    for j in tmpLIST[::-1]: #�N tmpLIST �����Ʀr�q�����Y�ǤJ j

        ans = ans + str(j)

    print("{0} ���G�i���ܬ� {1}.".format(N, ans))

    return None


#�@�~ 1.

# �аѦҤW�ҡA�ۤv�g�@�ӱN�G�i���ܼ��ର�Q�i���禡�ѵy�᪺�@�~�ϥΡG


def int2bin(N):

    '''

    ���禡�N int ����ର bin �G�i����ܡC�@�ε��P�� bin(N)

    '''

    tmpLIST = []

    while N > 0:

        remainder = int(N % 2)

        tmpLIST.append(remainder)

        N = (N - remainder) / 2

    tmpLIST.append(0)



    ans = ""

    for j in tmpLIST[::-1]: #�N tmpLIST �����Ʀr�q�����Y�ǤJ j

        ans = ans + str(j)

    print("{0} ���G�i���ܬ� {1}.".format(N, ans))

    return None


class HW02:

    def ch2(self):

        '''

        �бN�A�p��X�Ӫ����׶�J�H�U�ܼơA�U�з|�g�{���۰ʧ��C

        Ch2P2_19a = "xxx"

        �N��O

        Ch2   : �ĤG��

        P2_19a: �ĤG�������B�� PRACTICE SET �q���B�� Problems �� P2-19 �D�� a �p�D

        "xxx" �G �A�n��J�A�����a��C

        '''
        #�@�~ 2. �ҥ� Ch2. P2.19

        self.Ch2P2_19a = "10"

        self.Ch2P2_19b = "17"

        self.Ch2P2_19c = "6"

        self.Ch2P2_19d = "8"



        #�@�~ 3. �ҥ� Ch2. P2.20

        self.Ch2P2_20a = "14"

        self.Ch2P2_20b = "8"

        self.Ch2P2_20c = "13"

        self.Ch2P2_20d = "4" #"6"



        #�@�~ 4. �ҥ� Ch2. P2.22

        self.Ch2P2_22a = "00010001 11101010 00100010 00001110"

        self.Ch2P2_22b = "00001110 00111000 11101010 00111000"

        self.Ch2P2_22c = "01101110 00001110 00111000 01001110"

        self.Ch2P2_22d = "00011000 00111000 00001101 00001011"


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

        self.Ch3P3_28a = "234"

        self.Ch3P3_28b = "560"

        self.Ch3P3_28c = "874"

        self.Ch3P3_28d = "888"



        #�@�~ 6. �ҥ� Ch3. P3.30

        self.Ch3P3_30a = "234"

        self.Ch3P3_30b = "560"

        self.Ch3P3_30c = "875"

        self.Ch3P3_30d = "889"

#Please use an UTF-8 compatible IDE. I can't read your characters in Chinese.
#Or you can leave all your comments in English.

if __name__ == '__main__': #�{���i�J�I�A�{���Ѧ���}�l����C�H�U�ܽd�U�Ъ����{���C

    checkHW02 = HW02()

    checkHW02.ch2()

    if checkHW02.Ch2P2_19a == 10: #10 �O�o�D�����ѡC�����ˬd�o�D�����סC

        print("Ch2P2_19a:{0}".format("Correct!"))

    else:

        print("Ch2P2_19a:{0}".format("Incorrect!"))