sampleText=open("C:\\Users\WIN\Desktop\sample.txt","r")
sample=sampleText.read()
alpha=sample.replace("?"," ")
beta=alpha.replace(","," ")
gamma=beta.replace("."," ")
delta=gamma.replace("0"," ")
epsilon=delta.replace("1"," ")
zeta=epsilon.replace("2"," ")
eta=zeta.replace("\n"," ")
theta=eta.replace("\""," ")
b=theta.split(" ")
k=0
word=[]
for n in b:
    if len(n)>5:
        print(n)
        word.append(n)

c=0
w=input("請輪入一個單字：")
while c<len(word): #讓計數器在有限的範圍內跑
    if w==word[c]:
        print("有這個字")
        c=len(word) #讓while指令結束
    elif c==len(word)-1: #表示跑到最後一個c，w==word[c]仍不成立
        print("沒這個字")
        c=c+1
    else:
        c=c+1
#123
