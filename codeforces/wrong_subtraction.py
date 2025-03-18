n,k=map(int,input().split())
for _ in range(k):
    n=str(n)
    if n[-1]=='0':
        n=n[:-1]
    else:
        n=int(n)
        n-=1
print(int(n))