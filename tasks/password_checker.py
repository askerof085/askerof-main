
while True:
    your_password=input('Enter your password: ')
    if your_password  in ['password','123456','admin','admin123'] or  len(your_password)<8 or  your_password.isalpha() or your_password.isdigit() or your_password.islower() or your_password.isupper(): 
        print('Password is too weak, please try again')
        continue
    else:
        print('Password is strong')
        break
print('You have successfully created a password and your new password is',your_password)
# Adi koddu

        
        