n=int(input()) ; t=0
for _ in range(n):
    a,b=map(int,input().split())
    if b-a>=2:
        t+=1
print(t)
# Problem- 467A, George and Accomodation