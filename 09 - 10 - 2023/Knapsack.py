W=int(input())
wt=list(map(int,input().split()))
pr=list(map(int,input().split()))
perkg=[]
for i in range(len(wt)):
    perkg.append(pr[i]/wt[i])
l= list(zip(wt,pr,perkg))
l.sort(key=lambda x:x[2],reverse=True)
print(list(l))