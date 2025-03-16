a,b=map(int,input().split())
t=0
while True:
    if a<=b:
        a*=3 ; b*=2 ; t+=1
    else:
        break
print(t)
        