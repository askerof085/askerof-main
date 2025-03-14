numbers=input("Enter the numbers: ").split()
max1=0;max2=0
for i in range(0,len(numbers)):
    for j in range(1,len(numbers)):
        if numbers[i]>numbers[j]:
            max1=numbers[i]
            max2=numbers[j]
print(max1,max2)