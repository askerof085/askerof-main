n=int(input()) ; oldmagnet=[] ; t=0 
for _ in range(n):
    newmagnet=int(input())
    if oldmagnet==[]:
        oldmagnet=newmagnet
    if oldmagnet==newmagnet:
        oldmagnet=newmagnet
        continue
    else:
        t+=1
        oldmagnet=newmagnet
print(t+1 if n!=0 else t)
#Problem - 344A , Magnets


