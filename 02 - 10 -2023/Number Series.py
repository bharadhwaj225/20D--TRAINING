# 1 to n
'''n = int(input())
def fun(n):
    if n == 0:
        return
    fun(n - 1)
    print(n)
fun(n)'''
# n to 1
n = int(input())
def fun(n):
    if n == 0:
        return
    print(n)
    fun(n - 1)
fun(n)