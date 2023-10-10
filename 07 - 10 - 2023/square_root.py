def square_root(n,low,high):
    mid = (low+high)//2
    if mid*mid==n:
        return mid
    elif mid*mid<n:
        if(mid+1)*(mid+1)>n:
            return n/mid
        return square_root(n,mid+1,high)
    else:
        return square_root(n,low,mid-1)
    
n = int(input())
print(square_root(n,0,n//2))



# n = int(input())
# si = 0
# li = n//2
# floor=-1
# while si<=li:
#     mid = (si+li)//2
#     sqr = mid * mid
#     if sqr==n:
#         print(sqr)
#         break
#     elif sqr<n:
#         floor = mid+1
#     else:
#         li =mid-1
# print(floor)