def binary_search(array,low,high,key):
    mid = (low + high) // 2
    if low > high:
        return -1
    elif array[mid] == key:
        return mid+1
    elif array[mid] > key:
        return binary_search(array,low,mid-1,key)
    else:
        return binary_search(array,mid+1,high,key)
   
array = list(map(int,input().split()))
array_length = len(array)
key = int(input())
print(binary_search(array,0,array_length,key))