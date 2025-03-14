def rotate_list(lst, k):
    if not lst:
        return lst
    k = k % len(lst)
    return lst[-k:] + lst[:-k]
list=input("Enter the list: ").split()
k=int(input("Enter the number of rotations: "))
print(rotate_list(list,k))

