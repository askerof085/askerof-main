Total_cost=int(input('Enter the total cost: '))
if Total_cost>=1000:
    discount=Total_cost*0.1
    print('You have qualified for a discount of 10% and your discount is',discount)
    Total_cost-=discount
    print('Your new total cost is',Total_cost)
elif Total_cost>=500:
    discount=Total_cost*0.05
    print('You have qualified for a discount of 5% and your discount is',discount)
    Total_cost-=discount
    print('Your new total cost is',Total_cost)
else:
    print('You have not qualified for any discount and your total cost is',Total_cost)