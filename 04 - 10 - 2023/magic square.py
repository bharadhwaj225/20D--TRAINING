# n = int(input())
# sq = [[0] * n for i in range(n)]
# num = 1
# i = n//2
# j = n - 1
# while num <= n*n:
#     if i < 0 and j == n:
#         i = 0
#         j = n - 2
#     else:
#         if i < 0:
#             i = n - 1
#         if j == n:
#             j = 0
#         if sq[i][j]:
#             i = i + 1
#             j = j - 2
#             continue
#     sq[i][j] = num
#     num = num + 1
#     i = i - 1
#     j = j + 1

# for i in sq:
#     print(*i)






# Using Recursion
def mag_square(n):
    sq = [[0] * n for i in range(n)]
    def fill(i,j,num):
        if num > (n * n):
            return sq
        if i < 0 and j ==n:
            i = 0
            j = n - 2
        else:
            if i < 0:
                i = n - 1
            if j == n:
                j = 0
            if sq[i][j]:
                i = i + 1
                j = j - 2
                return fill(i,j,num)
        sq[i][j] = num
        return fill(i-1,j+1,num+1)

    return fill(n//2,n-1,1)

n = int(input())

if n%2 == 0:
    print("Enter valid Numnber")
    exit()
a = mag_square(n)
for i in a:
    print(*i)