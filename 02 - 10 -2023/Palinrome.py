'''n = input()
def pal(str):
    for i in range(0,len(str)//2):
        if str[i] == str[len(str)-i-1]:
            return True
        return False
print(pal(n))'''


'''s = input()
i = 0
j = len(s) - 1
while (i < j):
    if s[i]!=s[j]:
        print('Not Palindrome')
    break
    i+=1
    j-=1
else:
    print("Palindrome")'''

def pal(s, i, j):
    if i > j:
        return True
    if s[i]!=s[j]:
        return False
    return pal(s,i+1,j-1)
s = input()
print(pal(s,0,len(s)-1))