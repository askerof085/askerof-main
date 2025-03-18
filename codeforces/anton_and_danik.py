n=int(input())
s=input() ; D=0 ; A=0
for el in range(n):
    if s[el]=='D':
        D+=1
    else:
        A+=1
if D>A:
    print('Danik')
elif D<A:
    print('Anton')
else:
    print('Friendship')


