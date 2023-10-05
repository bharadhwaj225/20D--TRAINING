def subset_sum(nums, target):
    def backtrack(start, current_sum, current_subset):
        if current_sum == target:
            return True
        
        
        if current_sum > target or start == len(nums):
            return False
        current_subset.append(nums[start])


        if backtrack(start + 1, current_sum + nums[start], current_subset):
            return True
        
        current_subset.pop()
        return backtrack(start + 1, current_sum, current_subset)

    subset = []
    if backtrack(0, 0, subset):
        return True, subset
    else:
        return False, []

num = list(map(int, input().split()))
target = int(input())

found, result_subset = subset_sum(num, target)

if found:
    print("Subset found:", result_subset)
else:
    print("No subset found")
