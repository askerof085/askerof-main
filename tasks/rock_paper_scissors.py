Player1=(input("Enter your name player 1: "))
Player2=(input("Enter your name player 2: "))
total_games=0
player1_wins=0
player2_wins=0
while True:
    Player1_choice=input(f"{Player1} Enter your choice: ").lower()
    Player2_choice=input(f"{Player2} Enter your choice: ").lower()
    if Player1_choice not in ['rock','paper','scissors'] or Player2_choice not in ['rock','paper','scissors']:
        print('Invalid input')
        continue
    if Player1_choice==Player2_choice:
        print('It is a tie')
    elif Player1_choice=='rock':
        if Player2_choice=='scissors':
            print(f'{Player1} wins')
            player1_wins+=1
        else:
            print(f'{Player2} wins')
            player2_wins+=1
    elif Player1_choice=='scissors':
        if Player2_choice=='paper':
            print(f'{Player1} wins')
            player1_wins+=1
        else:
            print(f'{Player2} wins')
            player2_wins+=1
    elif Player1_choice=='paper':
        if Player2_choice=='rock':
            print(f'{Player1} wins')
            player1_wins+=1
        else:
            print(f'{Player2} wins')
            player2_wins+=1
    
    total_games+=1
    while True:
        another=input('Do you want to play another round? Y/N: ').upper()
        if another=='N':
            print(f'Total games played: {total_games}')
            print(f'{Player1} wins: {player1_wins}')
            print(f'{Player2} wins: {player2_wins}')
            if player1_wins>player2_wins:
                print(f'{Player1} wins the game')
            elif player1_wins<player2_wins:
                print(f'{Player2} wins the game')
            else:
                print('It is a tie')
            exit()

        elif another=='Y':
            break
        else:
            print('Invalid input')    
       
# Ən çox detal buna əlavə eləmişəm çünki o birilərdə çox elə qeyri-adi eləməyə nəsə yoxdu 
# Bütün oyunları sayıb , hər bir oyunçunun neçə dəfə qalib gəldiyini və hansı oyunçunun sonda ümumi hesabla qazandığını  əlavə etmişəm 
# hətta elə etmişəm ki invalid input daxil etdikdə oynanılan oyun kimi sayılmasın və oyunların sayına təsir etməsin    
        
        
