n=int(input()) ; suf_capacity=0 ; current_capacity=0
for _ in range(n):
    left,join=map(int,input().split())
    current_capacity= current_capacity+(join-left)
    if suf_capacity<current_capacity:
        suf_capacity=current_capacity
print(suf_capacity)

