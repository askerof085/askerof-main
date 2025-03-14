print('Welcome to the Yusif Bank')
your_name=input('Enter your name: ')
init_deposit=int(input('Enter your initial deposit: '))
while True:
    deposit_withdraw=input('Enter D for deposit or W for withdraw: ').upper()
    if deposit_withdraw not in ['D','W']:
        print('Invalid input, please try again')
        continue
    amount=int(input('Enter amount: '))
    if deposit_withdraw=='D':
        init_deposit+=amount
    elif deposit_withdraw=='W':
        if amount>init_deposit:
            print('Oops! Insufficient balance')
            continue
        else:
            init_deposit-=amount
    print(f'Succesfully! Your current balance {your_name} is {init_deposit}$') 
    while True:
        another=input('Do you want to make another transaction? Y/N: ').upper()
        if another=='N':
            print(f'Thank you for banking with Yusif Bank,{your_name}. See you next time') 
            exit()

        elif another=='Y':
            break
        else:
            print('Invalid input')
# kiçik bir toxunuş olaraq sadəcə əlavə olaraq ad daxil etməyi istəmişəm və hər bir əməliyyatdan sonra istifadəçinin adı ilə balansını ekrana çap etmişəm
# Birdə ki seminarda baxdıyımız kodda Bank dayanmadan işləyirdi və istifadəçi əməliyyatdan sonra başqa bir əməliyyat etmək istəsə ona soruşulmurdu
# Amma banklarda əməliyyatdan sonra istifadəçinin başqa bir əməliyyat etmək istəyib istəmədiyini soruşmaq lazımdır
  



