M,N=map(int,input().split()) ; C=M*N ; t=0
while C>1:
    t+=1 ; C-=2
print(t)