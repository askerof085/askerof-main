k,n,w=map(int,input().split())
total_cost=0
for i in range(1,w+1):
    total_cost+=k*i
if total_cost>n:
 print(total_cost-n)
else:
   print(0)