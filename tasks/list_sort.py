list=input("Enter the list: ").split()
sorted=list
sorted.sort()
if list==sorted:
    print("The list is already sorted.")
else:
    print("The list is not sorted.")
print(list, sorted)