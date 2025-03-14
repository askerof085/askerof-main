t=int(input())
elements=[]
for i in range(t):
    n,k=map(int,input().split())
    elements=input().split()
    elements=[int(x) for x in elements]
    if len(elements)!=n:
        print('invalid')
        exit()
    for i in range(n):
        if elements[i]==k:
            print('YES')
            break   
    else:
        print('NO')
            



    