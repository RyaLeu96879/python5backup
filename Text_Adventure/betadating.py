import time
import random 
def end():
    print ("You lose!")
def game():
    """Start of the game"""
print ("Welcome to epic dating simulator by Connor and Ryan!")
time.sleep(1)
print ("Disclaimer: If we offend you in any way, we apologize in advance.")
print ("Please don't get offended by our stereotypes.")
time.sleep(1)
print('Rules: Answer every question with an Yes or No(Caps sensitive)')
print('If you think there is an easter egg, type what you think it is with ')
print('proper grammar!')
time.sleep(2)
nameques = (raw_input("Whats your name?"))
if nameques == "Connor":
    print ("You win! Everyone loves Connor!")
else:
    genderques = raw_input('Do you want to date a boy or a girl?')
#boy
    if genderques == 'boy':
        print("Hi "+ nameques+ "! My name is Jeremy!")
        time.sleep(1)
        ques1boy = (raw_input("Do you play games?"))
        if ques1boy == "yes":
            print ('Good Answer! All guys love games!')
            ques2boy = (raw_input('Can I be Tracer?'))
            if ques2boy == "yes":
                print ('Good Answer! All guys love Tracer!')
            elif ques2boy == "no":
                print ("You lose! Put a better answer next time!")
            elif ques2boy == "I'm already Tracer":
                print ("You found an easter egg!")
            else:
                print ('Please type a valid question')
        elif ques1boy == "no":
            print ('You lose! Put a better answer next time!')
        else:
            print ('Please type a valid answer')
#girl
    elif genderques == 'girl':
        print ("Hi "+ nameques + "! my name is Charlotte!")
        time.sleep(1)
        ques1girl = (raw_input("Do you like pizza?"))
        if ques1girl == "yes":
            print ('Good answer! All girls love pizza tsk tsk')
        elif ques1girl == "no":
            print ('You lose! You answered incorrectly!')
        else:
            print('Please type a valid answer')
        time.sleep(1)
        ques2girl = (raw_input("Do you want to watch Avengers with me?"))
        if ques2girl == "Mr. Stark, I don't feel so good":
            print ('You found an easter egg!')
        elif ques2girl == "yes":
            print ('You lose! You answered incorrectly')
            exit()
        elif ques2girl == "no":
            print ('Good answer! No girl likes Avengers')
        time.sleep(1)
        ques3girl = (raw_input("Do you like pink nail polish?"))
        if ques3girl == "yes":
            print ('Good answer! Pink is very stereotypical')
        elif ques3girl == "no":
            print ('You lose! You answered incorrectly')
            exit()
        else:
            print ('Please type a valid option and restart the game.')
            exit()
        time.sleep(1)
        ques4girl = (raw_input("Do you watch The Office?"))
        if ques4girl == "yes":
            print ('Good answer! All genders love the office')
        elif ques4girl == "no":
            print ('You lose! You answered incorrectly')
            exit()
        else:
            print ('Please type a valid option and restart the game.')
            exit()
    else:
        print ('Please type a valid option and restart the game.')
        exit()

        
        
    
"""Yo Ryan can you try to write the story? Im really trying but I can't think
of anything"""