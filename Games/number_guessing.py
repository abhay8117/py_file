'''Number Guessing'''

import random

attempts_list =[]

def showScore():
    if not attempts_list:
        print(f'There is currently no high score.' )
    else:
        print(f'The current high score is {min(attempts_list)} attempts')

def startGame():
    attempts = 0
    rand_num = random.randint(1,10)
    print('Welcome to the game of guessess!')
    player_name = input('What is your name?')
    wanna_play = input(f'Hi {player_name}, would you like to play the guessing game?'
                       f'Enter Yes (Y)/No (N): ')
    
    if wanna_play.lower() != 'yes':
        print('That\'s fine, Thanks! See you again.')
        exit()
    else:
        showScore()

    while wanna_play.lower() == 'yes':
        try:
            guess = int(input('Pick anumber between 1 to 10: '))
            if guess <1 or guess>10:
                raise ValueError('Please guess a number within the given range.')
            
            attempts += 1
            attempts_list.append(attempts)

            if guess == rand_num:
                print('Nice! You got it.')
                print(f'It took you {attempts} attempts')
                wanna_play = input('Would you like to play again? Enter Yes(Y)/No(N): ')
                if wanna_play.lower() != 'yes':
                    print ('That\'s cool, have a good one!')
                    break
                else:
                    attempts =0
                    rand_num = random.randint(1,10)
                    showScore()
                    continue
            else:
                if guess > rand_num:
                    print('It\'s lower.')
                elif guess < rand_num:
                    print('It\'s higher.')
        except ValueError as er:
            print('Oh no!, That is not a valid value. Try again...')
            print(er)

if __name__ =='__main__':
    startGame()