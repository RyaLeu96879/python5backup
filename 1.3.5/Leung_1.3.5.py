#1
'''N/A'''
#2
'''N/A'''
#3
'''N/A'''
#4
'''N/A'''
#5
'''Float and int can represent the number six million'''
#6
'''The second one, type('tr' + 5) has error because one's string and the other
one's integer'''
#7
'''Slogan + [#] would count from the start and reach that number of letter in that
sentence and show the letter and when you type slogan + [-#], it would count backwards 
and counting backwards have no zero'''
#8
'''N/A'''
#9
'''N/A'''
#10
#a)
'''the length of activity is equal to theater therefore it's 7 words'''
#b)
'''activity is equal to theater so everything about activity will show up as 
theater and since it's length of activity -1, it's equal to theater -1'''
#11
'''The answer is true because the words, test goo, is in the sentence of Greatest 
good for the greatest number!'''
#12
def how_eligible(essay):
    '''tell if essay is eligible'''
    points = 0
    if '?' in essay:
        points += 1
    if '"' in essay:
        points += 1
    if ',' in essay:
        points += 1
    if '!' in essay:
        points += 1
    print points
#Assignment check
#1.3.5 Function Test
print(how_eligible('This? "Yes." No, not really!'))
print(how_eligible('Really, not a compound sentence.'))
'''4 none 1 none, i belive i've succesfully complete the assignment base on the 
result'''