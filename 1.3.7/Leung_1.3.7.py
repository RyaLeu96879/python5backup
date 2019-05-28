from __future__ import print_function
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random
#1
'''N/A'''
#2
'''N/A'''
#3
'''N/A'''
#4
def days():
    ''' Put days on the end of every months
    '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')
#5


def picks():
    a = [] # make an empty list
    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list]
    #    random.choice(   [brackets here to choose from a list])

    a += [random.choice([1, 3, 10])]
    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.savefig('1.3.7/picks')
#6
#a
def roll_hundred_pair():
    '''Rolls a hundred pair of dices'''
    dice=[]    
    for item in range(100):
        dice.append(random.randint(1, 6))
    dice2=[]    
    for item in range(100):
        dice2.append(random.randint(1, 6))
    plt.hist(dice)
    plt.savefig('connorisawsome...')
#b
def dice(n):
    '''Rolls how ever many dice the user wants to roll'''
    dice=[]
    for item in range(n):
        dice.append(random.randint(1, 6))
    total = sum(dice)
    return total
#7
'''line 2 is neccesary because it ensures you that the player only have one guess'''
def validate():
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')
#8

def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''The arguments are names of players given in strings.  The value returned
    is an integer representing how many guesses you take to guess the winner
    right
    '''
    winner = random.choice(players) 

    ####
    # Print out the prompt by listing the arguments after the print statement
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: # explain index here
        print(p+', ', end='')
    print(players[len(players)-1]) # explain this line here

    ####
    # Take in user's guess and check to see if it match the what is wanted
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses    
#9
def goguess():
    """Take a guess and check to see if it's the right number chosen between
    1 - 20"""
    guess_number = 0
    correct = random.randint(1, 20)
    print ('I have a number between 1 and 20 inclusive.')
    guess = int(raw_input('Guess: '))
    while guess != correct:
        if guess < correct:
            print (guess, ' is too low.')
            guess_number += 1
            guess = int(raw_input('Guess: '))
        else:
            print(guess, ' is too high.')
            guess_number += 1
            guess = int(raw_input('Guess: '))
    print('Right! My number is', correct, ' ! You guessed in', guess_number,\
    'guesses!')
#10
'''It would take about 7 guesses for me to get right because I would type like 
1500 and I would see if it's too hgh or too low and if too low, then I would guess
something like 500 and I would find the right number between two or keep guessing 
lower and if higher, then I would guess a really hggh number and taking what
the result is, I would figure out what the number is.'''
#11
#a
def matches(ticket, winners):
    '''How many tickets match winnner'''
    common = 0
    for num in winners:
        if num in ticket:
            common += 1
        else:
            common += 0
    print (common)
    return common
#b 
def report(guess,secret):
    '''Make mastermind in python'''
    right_place = 0
    wrong_place = -2
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            right_place += 1
        elif guess[i] != secret[i]:
            wrong_place +=1
    return [right_place, wrong_place]
    
    
#Conclusion
#1
'''Disadvantage is that you need to know the loop you are making right now very
well or else you have a bg chance of messing up the code if you are not clear 
about the loop.'''
#2
'''Iteration can help you go through the analyss of a large set of data and find
what you need quickly.'''
#3
'''A while loop would keep running until condition becomes flase and a for loop 
would run what you want once.'''
#4
'''My partner and me work very efficiently together because we make sure that each
other understand the functions that we use and we would reach out to other people
if both of us don't know how to do it.  My proccess and style is to let my partner 
start the problem off, then I would help us finish the problem.'''

'''Assignment Check'''
#1.3.7 Function Test
days()
print (dice(3))
validate()
guess_winner()
goguess()
matches([11, 12, 13, 14, 15], [3, 8, 12, 13, 17])
guess = ['red','red','red','green','yellow']
secret = ['red','red','yellow','yellow','black']
print (report(guess, secret))
'''I believe that I have successfully completed the assignment base on my 
result'''