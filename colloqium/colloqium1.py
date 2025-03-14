while True:
    strong_password=input()
    if len(strong_password)<8 or strong_password.isdigit() or strong_password.isalpha or strong_password.isupper() or strong_password.islower() or strong_password in ['password','admin','qwerty123'] :
     for i in range(0,10):
        if str(i) in strong_password:
             print(f'Strong password, your new password is {strong_password}')
             exit()
     else:
         print('Weak password, please try again')
         
    
     
    