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
    