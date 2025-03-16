s=input()
s=list(s) ; upper=0 ; lower=0
for i in s:
    if i==i.upper():
        upper+=1
    else:
        lower+=1
s=''.join(s)
if upper>lower:
    print(s.upper())
else:
    print(s.lower())