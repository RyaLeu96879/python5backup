from __future__ import print_function # must be first in file 
import random
#1
def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'
#Answers for #1
'''1a: line 17 execute
1b:
    i)orange
    ii)apple, banana
    iii)potato
    iv)connor
1c: The banana didn't result in starchy because the fruit in food comes first
so the starchy didn't run'''
#2
def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()' 
    # Add tests so that all lines of code are visited during test
    
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False
#No question
#3
def f(n):
    '''Define if number is integer'''
    if int(n)==n:
        if n % 2:
            print('Number is odd')
        else:
            if n % 3:
                print('Number is even')
            else:
                print('Number is mutiple of 6')
    else:
        print('Nuber is not an integer')
#No question
#4
'''Try numbers that are even, odd, mutiple of 6, and a number that's not a 
integer like fractions'''
#5
def f_test():
    ''' Unit test for f_test
    returns True if good, returns False and prints error if not 
    good'''
    works = True
    if f(1) != 'Number is odd':
        works = 'bug in number'
    if f(2) != 'Number is even':
        works ='bug in number'
    if f(1.1) != 'Number is not an integer':
        works = 'bug in number'
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
#No question
#7
'''Using + as concatenation is adding a bunch of words together, and using + as
numeric addition is adding numbers together'''
#8
def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess != secret:
        if guess >= guess:
            print('Too low! - my number was', secret)
        else:
                print('Too high! - my number was', secret)
    else:
        print('Right on! my number is', guess, end='!\n')
#a
'''When the number the user guess is right, it prints that line'''
#9
def quiz_decimal(low, high):
    decimal = random.randint
    print('Type a number between', low, 'and', high.)
    guess = int(raw_input('Guess: '))
    if number != decimal:
        if guess >= guess:
            print('No, - my number was', secret)
        else:
                print('Too high! - my number was', secret)
    else:
        print('Right on! my number is', guess, end='!\n')
    
#1.3.4 Function Test/ Assignment check
print(food_id('apple'))
food_id_test()
#1.3.4 Function Test
print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
f_test()
guess_once()
guess_once()
'''quiz_decimal(4, 4.1)
quiz_decimal(4, 4.1)
f_challenge(1.1)
f_challenge(2)
f_challenge(3)
f_challenge(6)'''

