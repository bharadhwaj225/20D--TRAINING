def N_Queens(n):
    col=[]
    posdiag=[]
    negdiag=[]
    board=[["."]*n for i in range(n)]
    ans=[]
    def backtrack(r):
        if r==n:
            l=["".join(i) for i in board]
            ans.append(l)
            return
        for c in range(n):
            if c in col or (r+c) in posdiag or (r-c) in negdiag:
                continue
            board[r][c]='Q'
            col.append(c)
            posdiag.append(r+c)
            negdiag.append(r-c)
            backtrack(r+1)

            board[r][c]="."
            col.remove(c)
            posdiag.remove(r+c)
            negdiag.remove(r-c)
    backtrack(0)
    return ans

n=int(input())
res=N_Queens(n)
for i in res:
    print(*i)
print()