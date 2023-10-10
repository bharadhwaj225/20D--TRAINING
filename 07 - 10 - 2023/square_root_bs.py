def sqrt_binary_search(num,epsilon=1e-6):
    if num<0:
        raise  ValueError("Cannot Compile")
    if num < 1:
        left,right=num

    else:
        left ,right=0,num

    while abs(left-right)>epsilon:
        mid=(left+right)/2
        mid_squared=mid*mid

        if mid_squared<num:
            left = mid
        else:
            right = mid
    return (left+right)/2

# num = int(input())
num = 9
res = sqrt_binary_search(num)
print(res)