n=int(input())
i=0
for _ in range(n):
	a,b,c= map(int, input().split())
	if a+b+c>=2:
		i=i+1
print(i)
	
	