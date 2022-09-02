import random


def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r','p', 's'])

    if is_win(user, computer):
         print ("Victory")
    elif is_lose(user,computer):
         print ("Loss")
    elif user == computer:
        print ("Tie")
    else:
        print("Invalid option")
    print(f"Computer chose {computer} and you chose {user}")

def is_win(player,opponent):
    if ( player == 'r' and opponent =='s') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
def is_lose(opponent,player):
     if ( player == 'r' and opponent =='s') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

game_Running = ''
while game_Running != "n":
    play()
    game_Running = input("Press n if you want to stop the game, if you want to continue press any key: ")