def som(lis,f,l):#sum of list with divide and conquer!
    if(l-f==1):
        return lis[f]+lis[l]
    if(l-f==0):
        return lis[f]
    mid=f+(l-f)//2
    return som(lis,f,mid)+som(lis,mid+1,l)
l=list(map(int,input("Enter a list of integers:\n").split()))
print("Sum of integers in list is:",som(l,0,len(l)-1))
#-----------------------------------------------
def maxx(l):
    def logic(s,e):
        if(s-e==1):
            return l[s] if l[s]>l[e] else l[e]
        if(s-e==0):
            return l[s]
        mid=s+(e-s)//2
        left=logic(s,mid)
        right=logic(mid+1,e)
        return left if left>right else right
    return logic(0,len(l)-1)
l=list(map(int,input("Enter a list of integers:\n").split()))
print("The largest element in the list is:",maxx(l))