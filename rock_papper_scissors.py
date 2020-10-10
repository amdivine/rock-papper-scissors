import random

choices = ['rock','papper', 'scissors']

def genRand(start, end):
    return random.randrange(start, end)


def play(player1, player2):
    if player1 == player2:
        print('it is a tie')
    else:
        if player1 == 'rock' and player2 == 'papper':
            print(f'Player1 picked {player1} & Player2 picked {player2}\n\nPlayer2 wins!!!')
        elif player1 == 'rock' and player2 == 'scissors':
            print(f'Player1 picked {player1} & Player2 picked {player2}\n\nPlayer1 wins!!!')
        elif player1 == 'papper' and player2 == 'rock':
            print(f'Player1 picked {player1} & Player2 picked {player2}\n\nPlayer1 wins!!!')
        elif player1 == 'papper' and player2 == 'scissors':
            print(f'Player1 picked {player1} & Player2 picked {player2}\n\nPlayer2 wins!!!')
        elif player1 == 'scissors' and player2 == 'rock':
            print(f'Player1 picked {player1} & Player2 picked {player2}\n\nPlayer2 wins!!!')
        elif player1 == 'scissors' and  player2 == 'papper':
            print(f'Player1 picked {player1} & Player2 picked {player2}\n\nPlayer1 wins!!!')



ply1 = choices[genRand(0, 3)]
ply2 = choices[genRand(0, 3)]

play(ply1, ply2)
