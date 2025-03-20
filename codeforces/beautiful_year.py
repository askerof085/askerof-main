y=int(input()) 
while True:
    t=[]
    y=int(y)
    y+=1
    y=str(y)
    for i in y:
        if i not in t:
            t.append(i)
    if len(t)==4:
        print(y)
        exit()
           
    

        


    