numbers=input('Enter the numbers: ').split()
numberlist=[]
for number in numbers:
    if number not in numberlist:
        numberlist.append(number)
print(numberlist)


