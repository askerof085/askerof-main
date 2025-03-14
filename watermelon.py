w = int(input())
for i in range(w):
    a=w-i
    if a%2==0 and i%2==0:
        print('Yes')
        break
else:
    print('No')