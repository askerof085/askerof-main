matrix=[]
for el in range(5):
    el=input().split()
    el=[int(i) for i in el]
    if len(el)!=5:
        print('invalid')
        exit()
    else:    
        matrix.append(el)
for row in matrix:
    a=matrix.index(row)
    if 1 in row:
        b=row.index(1)
        break
print(abs(2-a)+abs(2-b))
