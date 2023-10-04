def check(arr, target, n):
    
    if target == 0:
        return True
    if n == 0:
        return False
        
    if arr[n-1] > target:
        return check(arr, target, n-1)
        
    return check(arr, target-arr[n-1], n-1) or check(arr, target, n-1)
arr = [ 3, 12, 5, 4, 24, 2 ]
target = 9
ans = check(arr, target, len(arr))
if ans == True:
    print("solution found")
else:
    print("solution not found")