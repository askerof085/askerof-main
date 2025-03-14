n=int(input())
x=0
for _ in range(n):
	v=input()
	v=list(v)
	v.sort()
	v=''.join(v)
	if v=='++X':
		x+=1
	elif v=='--X':
		x-=1
print(x)
	
	
	