r,c=map(int , input().split())
matrix=[]
for el in range(r):
    el=input().split()
    el=[int(i) for i in el]
    if len(el)!=c:
        print('invalid')
        exit()
    else:    
        matrix.append(el)
for row in matrix:
    print(row)



