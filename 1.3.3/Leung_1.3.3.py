from __future__ import print_function # use Python 3.0 printing 

def age_limit_output(age):
    '''Step 9a if-else example'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT) 
def report_grade(percent):
    '''Tells grade is bad or good in percent'''
    if percent < 80:
        print('A grade of', percent, 'does not indicate mystery. Seek extra practice or help.')
    else:
        print('A grade of', percent, 'percent indicates mystery. Keep up the good work.')
        
def vowel(letter):
    '''Tells vowel in letter'''
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        return True
    else:
        return False
# should check len(letter)==1
def letter_in_word(guess, word):
    '''Guess a hangman phrase'''
    if guess in word:
        return True
    else:
        return False
        
def hint(color, secret):
    '''Give hint to secret color'''
    if color in secret:
        print('The color', color, 'IS in the secret sequence of colors')
    else:
        print('The color', color, 'IS NOT in the secret sequence of colors')
#1.3.3 Function Test
age_limit_output(10)
age_limit_output(16)
report_grade(79)
report_grade(85)
print(letter_in_word('t', 'secret hangman phrase'))
secret = ['red','red','yellow','yellow','black']
hint('red', secret)
hint('green', secret)
'''Conclusion questions:
#1) If is for hypothetical question, else is for flase/ something else than if, 
#and elif is comes before else
#2) Boolean expression is for true or false
#3) I think Kendra is right because the everything she said is right, Jayla is 
somewhere in between because it wouldbe harder to change the code later, Ira
is wrong because the program is going to run at the same speed ''' 