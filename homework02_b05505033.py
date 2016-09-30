def bin2int(N):
    keyed=N
    power=0
    results=0
    left=0
    while N>0:
        leftovers=(N%10)
        results+=(2**power)*leftovers
        N=N//10
        power=power+1
        #print("{0} int {1}.".format(keyed,results))
    #print("{0} abc {1}.".format(N,results))
    return results
    