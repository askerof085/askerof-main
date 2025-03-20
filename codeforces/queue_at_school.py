n,t=map(int,input().split())
s=input()
s=list(s)
for _ in range(t):
    i=0
    for _ in range(len(s)):
        if i<len(s)-1 and s[i]=='B' and s[i+1]=='G':
            s[i],s[i+1]=s[i+1],s[i]
            i+=2
        else:
            i+=1
print(''.join(s))
   