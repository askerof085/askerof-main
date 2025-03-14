name1,name2,name3=(input().split())
quantity1,quantity2,quantity3=map(int,input().split())
while True:
    sell_name = input("Enter the product name to sell (or 'exit' to quit): ")
    if sell_name.lower() == 'exit':
        break
    sell_quantity = int(input(f"Enter quantity to sell for {sell_name}: "))
    if sell_name==name1:
        if quantity1<sell_quantity:
            print(f"Warning: Insufficient stock for {sell_name}.")
        else:
            quantity1-=sell_quantity
            print(f"Sold {sell_quantity} of {sell_name}. Remaining stock: {quantity1}")
    elif sell_name==name2:
        if quantity2<sell_quantity:
            print(f"Warning: Insufficient stock for {sell_name}.")
        else:
            quantity2-=sell_quantity
            print(f"Sold {sell_quantity} of {sell_name}. Remaining stock: {quantity2}")
    elif sell_name==name3:
        if quantity3<sell_quantity:
            print(f"Warning: Insufficient stock for {sell_name}.")
        else:
            quantity3-=sell_quantity
            print(f"Sold {sell_quantity} of {sell_name}. Remaining stock: {quantity3}")
    else:
        print(f"Warning: {sell_name} does not exist in the inventory.")
print("Final inventory:")
print(f"{name1}: {quantity1}")
print(f"{name2}: {quantity2}")
print(f"{name3}: {quantity3}")
# Normal koddu


