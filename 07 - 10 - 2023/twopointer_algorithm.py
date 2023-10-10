n = list(map(int,input().split()))
target=int(input())
for i in n:
    for j in n:
        if i+j==target:
            print([i,j])