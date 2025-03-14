word=input()
word= 'a' + word
word=list(word)
sum=0 ; distance=0
cycle=(len(word))
for el in range(0,cycle):
   if el+1==cycle:
     break
   else: 
    letter1=word[el] 
    letter2=word[el+1]  
    distance+=abs((ord(letter1)-ord(letter2)))
    if distance<14:
     sum+=distance
    else:
     sum=sum+(26-distance)
    distance=0
print(sum)