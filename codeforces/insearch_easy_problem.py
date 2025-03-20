n=int(input())
people=input().split()
for i in range(n):
    if people[i]=='1':
        print('HARD')
        exit()
print('EASY')