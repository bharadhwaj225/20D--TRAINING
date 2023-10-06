array = list(map(int,input().split()))
max_element = max(array)
count_array = [0] * (max_element +  1)
array_length = len(array)

for i in range(array_length):
    count_array[array[i]] += 1
# print(count_array)
for i in range(1,max_element+ 1):
    count_array[i] = count_array[i] + count_array[i-1]
# print(count_array)
res = [0] * array_length
for i in range(array_length):
    count_array[array[i]] -= 1
    res[count_array[array[i]]] = array[i]
print(res)