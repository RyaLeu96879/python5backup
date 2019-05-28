import time
import random 

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
    print ("You lose, No one would ever want to date you!")
else:
    #Real Questions
    def genderques():
        """Gender question to get the gender of the player"""
        response = raw_input("Do you want to date a Boy or a girl? (caps sensitive.)")
        if response == "Yes":
            print ("Hi "+ nameques+ "! My name is Jeremy!")
            return True
            def ques1boy():
                response = raw_input("Do you like pizza?")
                if response == "Yes":
                    print ("Good Answer! All guys love games!")
                    def ques2boy():
                        response = raw_input('Can I be tracer?')
                        if response =="Yes":
                            print('')
                elif response == "No":
                    print ("You lose! Put a better answer next time!")
                else:
                    print ('Please type a valid option')
                    ques2boy()
        elif response == "No":
            print ("You lose! Put a better answer next time!")
        else:
            print ('Please type a valid option')
        genderques()
        
        
"""Yo Ryan can you try to write the story? Im really trying but I can't think
of anything"""