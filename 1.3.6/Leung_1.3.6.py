#1
'''N/A'''
#2
'''N/A'''
#3 
'''N/A'''
#4
'''(3,6,7)'''
#5
'''A convention required by teacher is never type across the line in the work area
when working in cloud 9'''
#6
#6a
'''the outcome is 'b' because the number in the parentheses after the variable
some_values represent which value to get in the tuple'''
#6b
'''the outcome would be 'a', 'b' because 0:2 represent the last two values and 
the last two values is a and b'''
#7
#7a
'''the outcome is true because the second value in b is 10 and since it start at 
zero, the first value is represent in b[0]'''
#7b
'''the outcome is 15 because the second value is b is a which is earlier stated 
as 15 so the outcome is 15'''
#8 
'''the outcome is 'b', 3 because [1:0] saids to show any vlaue after the first one
and the value b and three are all the value come after the first one'''
#9
'''the outcome is false because the first line of command change values[2] to '3'
instead of three'''
#10
#10a
'''the outcome is 'a', 'b', '3', 4, 5 because the variable values is euqal to all
the values inside it and , 5 after the first line of command I added'''
#10b
'''the outcome is values + [6, 7] at the end because the first commandi I added in 
this excercise add ([6, 7]) at the end of the values in the variable values.'''
#11
'''It doesn't work because you can only add list, not integers onto the tuple'''
#12
'''the outcome is 18 because a is equal to 6 and when a times 3, it represent 
6 times 3 which is 18'''
#13
'''N/A'''
#14
import random
def roll_two_dice():
    '''define numbers that two dices could roll'''
    return random.randint (1,6) + random.randint (1,6)
#CONLCUSION
#1
'''a is a word, b is a tuple, and c is a list'''
#2
'''because having variety of variable types can let the programmer choose what
he/she want to use, more flexibility'''
#3
'''how to use tuples, lists, strings, branching, inputs, outputs and functions of python'''
#ASSIGNMENT CHECK
#1
'''I got different numbers combinations that two dices can have when rolling it''' 

print(roll_two_dice())
