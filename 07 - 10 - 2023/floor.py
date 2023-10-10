def floor(arr,low,high,key):
    mid = (low+high)//2
    if low > high:
        return arr[high] if high>=0 else -1
    elif arr[mid] == key:
        return mid + 1
    elif arr[mid] > key:
        return floor(arr,low,mid-1,key)
    else:
        return floor(arr,mid+1,high,key)
arr = list(map(int,input().split()))
arr.sort()
arr_length = len(arr)
key = int(input())
print(floor(arr,1,arr_length,key))


# def bs_floor(l,target,si,li,floor):
#     if si<=li:
#         mid = (si+li)//2
#         if l[mid]<target:
#             floor=l[mid]
#             return bs_floor(l,target,mid+1,li,floor)
#         else:
#             return bs_floor(L,target,si,mid-1,floor)
# l = [2,6,8,9,10]
# target = 7
# print(bs_floor(l,target))