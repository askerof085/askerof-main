n,k=map(int,input().split())
t=0
i=input().split()
for b in range(n):
    if int(i[b])>=int(i[k-1]) and int(i[b])>0:
        t+=1
print(t)
