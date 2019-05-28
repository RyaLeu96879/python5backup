import time
import random
#BOY QUESTIONS
def ques7boy():
    '''Answers the last question'''
    response = raw_input('Last question, Do you like Riverdale?')
    if response == 'yes':
        print('You lose! Put a better answer next time!')
        end()
    elif response == 'no':
        print('Good Answer! No guy likes Riverdale :(')
        end2()
    else:
        print('Please type a valid option.')
        ques7boy()
def ques6boy():
    """Answers the 6th question"""
    response = raw_input('Do you play golf?')
    if response == "yes":
        print('Good answer! All boys love golf?(mostly men)')
        ques7boy()
    elif response == 'no':
        print('You lose! Put a better answer next time!')
        end()
    else:
        print('Please type a valid option')
        ques6boy()
def ques5boy():
    """Answers the 5th question"""
    response = raw_input('Is reddit a bad site?')
    if response == 'no':
        print('Good answer! Everyone loves Reddit!')
        ques6boy()
    elif response == "yes":
        print('I have nothing to say to you >:(')
        end()
    else:
        print('Please type a valid option.')
        ques5boy()
def ques4boy():
    '''Asks the 4th question'''
    response = raw_input('Do you watch the office?')
    if response == "yes":
        print('Good answer! Everyone likes the office')
        ques5boy()
    elif response == 'no':
        print('You lose! Put a better answer next time!')
        end()
    else:
        print('Please type a valid option')
        ques4boy()
def ques3boy():
    '''Asks the third question'''
    response = raw_input('Want to watch the Notebook?')
    if response == 'yes':
        print('Good answer! All guys secretly love the Notebook!')
        ques4boy()
    elif response == 'no':
        print('You lose! Put a better answer next time!')
        end()
    else:
        print('Please type a valid option')
        ques3boy()
def ques2boy():
    '''Asks the second question and leads to easter egg hunt'''
    response = raw_input('Can I be tracer?')
    if response == 'yes':
        print('Good answer! Guys love Tracer!')
        ques3boy()
    elif response == 'no':
        print('You lose! Put a better answer next time!')
        end()
    elif response == "I'm already Tracer":
        print ("You found an easter egg!")
        print('You will answer a different set of questions!')
        ques1egg()
    else:
        print('Please type a valid option')
        ques2boy()
def ques1boy():
    '''Asks the first question'''
    response = raw_input("Do you like games?")
    if response == 'yes':
        print ("Good Answer! All guys love games!")
        ques2boy()
    elif response == 'no':
        print ("You lose! Put a better answer next time!")
        end()
    else:
        print ('Please type a valid option')
        ques1boy()
#END OF BOY QUESTIONS
#EASTER EGG QUESTIONS
def ques1egg():
    '''Asks the first easter egg question'''
    response = raw_input("When they hit, do they ever miss?")
    if response == 'yes':
        print ("Good Answer! Guess they never miss huh?")
        ques2egg()
    elif response == 'no':
        print ("You lose! Put a better answer next time!")
        end()
    else:
        print ('Please type a valid option')
        ques1egg()
def ques2egg():
    '''Asks the second easter egg question'''
    response = raw_input("Does Karen have the kids?")
    if response == 'yes':
        print ("Good Answer! Let's trust Karen with the kids for once!")
        ques3egg()
    elif response == 'no':
        print ("You lose! Put a better answer next time!")
        end()
    else:
        print ('Please type a valid option')
        ques2egg()
def ques3egg():
    '''Asks the third easter egg question'''
    response = raw_input("Is big chungus a good meme?")
    if response == 'no':
        print ("Good Answer! CHUNGUS GANG")
        ques4egg()
    elif response == 'yes':
        print ("You lose! I mean if you like it you suck no offense")
        end()
    else:
        print ('Please type a valid option')
        ques3egg()
def ques4egg():
    '''Asks the first easter egg question'''
    response = raw_input("Last question, Does four panels mean that it's LOSS?")
    if response == 'yes':
        print ("Good Answer! (Definately not a personal bias for loss)")
        end2()
    elif response == 'no':
        print ("You lose! Sorry for your LOSS")
        end()
    else:
        print ('Please type a valid option')
        ques4egg()
#END OF EASTER EGG QUESTIONS
#BASIC QUESTIONS
def end():
    '''end function for wrong answers answered'''
    print (":(((")
def end2():
    '''The actually end of game for winning'''
    print ("Game over! You win!!!!")
def nameques():
    '''Asks for the players name'''
    response = raw_input("Whats your name?")
    if response == "Connor":
        print ("You win! Everyone wants to date you!")
        end2()
    else:
        genderques()
def genderques():
    '''Asks for the gender the player wants to date'''
    response = raw_input("Do you want to date a Boy or a girl?")
    if response == 'boy':
        print("Hi! My name is Jeremy!")
        ques1boy()
    elif response == "girl":
        print("Hi! my name is Charlotte!")
        ques1girl()
    else:
        print('Please type in a valid answer')
        genderques()
#END OF BASIC QUESTIONS
#GIRL QUESTIONS
def ques1girl():
    '''Ask the first question'''
    response = (raw_input("Do you like pizza?"))
    if response == "yes":
        print ('Good answer! All girls love pizza tsk tsk')
        ques2girl()
    elif response == "no":
        print ('You lose! Put a better answer next time!')
        end()
    else:
        print('Please type a valid answer')
        ques1girl()
def ques2girl():
    '''Ask the 2nd question'''
    response = (raw_input("Do you want to watch Avengers with me?"))
    if response == "Mr. Stark, I don't feel so good":
        print ('You found an easter egg! You will answer a different')
        print ('set of questions!')
        ques1egg()
    elif response == "yes":
        print ('You lose! You answered incorrectly')
        end()
    elif response == "no":
        print ('Good answer! No girl likes Avengers')
        ques3girl()
    else:
        print ('Please type a valid answer.')
        ques2girl()
def ques3girl():
    '''Ask the 3rd question'''   
    response = (raw_input("Do you like pink nail polish?"))
    if response == "no":
        print ('Good answer! Pink is very stereotypical')
        ques4girl()
    elif response == "yes":
        print ('You lose! You answered incorrectly')
        end()
    else:
        print ('Please type a valid answer.')
        ques3girl()
def ques4girl():
    '''Ask the fourth question'''
    response = (raw_input("Do you watch The Office?"))
    if response == "yes":
        print ('Good answer! All genders love the office')
        ques5girl()
    elif response == "no":
        print ('You lose! You answered incorrectly')
        end()
    else:
        print("Please type a valid answer")
        ques4girl()
def ques5girl():
    '''Ask the fifth question'''
    response = (raw_input("Do you like rolling backpacks?"))
    if response == "yes":
        print ('You lose! No one likes rolling backpacks.')
        end()
    elif response == "no":
        print ('Good answer! Honestly if you do i feel bad for you')
        ques6girl()
    else:
        print("Please type a valid answer")
        ques5girl()
def ques6girl():
    '''Ask the 6th question'''
    response = (raw_input("Do you like Riverdale?"))
    if response == "yes":
        print ("No you don't, but it's ok, she doesn't know :p")
        ques7girl()
    elif response == "no":
        print ('Good answer! No one like Riverdale')
        ques7girl()
    else:
        print("Please type a valid answer")
        ques6girl()
def ques7girl():
    '''Ask the seventh question/end of game'''
    response = (raw_input("Do you love this game?"))
    if response == "yes":
        print ("No you don't, I know you hate this game")
        end()
    elif response == "no":
        print ('Good answer! This game is terrible ')
        end2()
    else:
        print("Please type a valid answer")
        ques7girl()
#END OF GIRL QUESTIONS
#MAIN GAME FUNCTIONS
print ("Welcome to epic dating simulator by Connor and Ryan!")
time.sleep(1)
print ("Disclaimer: This game contains a lot of gender stereotypes.")
print ("If you are easily offended we advise you not to play.")
time.sleep(3)
print('Rules: Answer every question with an yes or a no')
print('If you think there is an easter egg, type what you think it is with ')
print('proper grammar!')
time.sleep(1)
nameques()