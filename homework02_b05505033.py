def bin2int(N):
    keyed=N
    power=0
    results=0
    left=0
    while N>0:  #ス计砆巨ЧΘ(碞琌┮Τ计砆眖砆┺)碞挡
        leftovers=(N%10)   #计程ソ(1or0)
        results+=(2**power)*leftovers    #计程ソ赣计Ωよ"+"琌ノㄓsum up┮Τresults玥挡狦穦瞷秈计い程2Ωよ计(EX:101瞷4)
        N=N//10   #р程ソ┺奔衡
        power=power+1  #盢Ωよ矗ど1パ┕玡2Ωよ笲衡ЧΘ碞Ω膥尿秈︽癹伴
        #print("{0} int {1}.".format(keyed,results)) 代刚
    #print("{0} abc {1}.".format(N,results))  代刚
    return results
    