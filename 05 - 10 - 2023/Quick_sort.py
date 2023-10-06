# quick sort
# def quick_sort(arr):
#     if len(arr)<=1:
#         return arr
#     pivot = arr[len(arr)//2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]

#     return quick_sort(left) + middle + quick_sort(right)

# n = [x for x in input().split()]
# sorted_list = quick_sort(n)
# print(sorted_list)


def qsorting(l,start,end):
    pivot = l[end]
    i = start - 1
    for j in range(start,end):
        if l[j]<pivot:
            i = i+1
            l[i],l[j]=l[j],l[i]
        l[i+1],l[end]=l[end],l[i+1]
    return i+1
def quick(l,start,end):
   if start < end:
       pivot = qsorting(l,start,end)
       quick(l,start,pivot-1)
       quick(l,pivot+1,end)
l = list(map(int,input().split()))
quick(l,0,len(l)-1)
print(l)