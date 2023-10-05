n = [int(x) for x in input().split()]
a = len(n)
flag = True
for i in range (a - 1):
    for j in range(a - i - 1):
        if n[j] > n[j+1]:
            flag = False
            n[j],n[j+1] = n[j+1],n[j]
    if flag:
        break

print(n)