t=int(input())
for i in range(t):
    elements=input().split('+')
    elements=[int(x) for x in elements]
    print(sum(elements))
