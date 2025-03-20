n,h=map(int,input().split()) ; n_person=input().split() ; t=0
for i in range(n):
        if int(n_person[i])>h:
         t+=2
        else:
         t+=1
print(t)

    

   