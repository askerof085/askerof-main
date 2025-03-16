n=int(input()) ; s=input() ; t=0 
s=list(s)
if len(s)==n:
    for i in range(len(s)):
        if len(s)>i+1:
         if s[i]==s[i+1]:
            t+=1
print(t)


    