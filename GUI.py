import time
import tkinter
from tkinter import *
import sys
import speech_recognition as sr
import random
import pyttsx3
import os
import datetime
import wikipedia

main_screen = Tk()
main_screen.attributes('-fullscreen',True)
main_screen.configure(background='black')


def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',200)
    print(f"Cofrasoron: ",audio)
    engine.say(audio)
    engine.runAndWait()



  
class Redirect():

    def __init__(self, widget, autoscroll=True):
        self.widget = widget
        self.autoscroll = autoscroll

    def write(self, text):
        self.widget.insert('end', text)
        if self.autoscroll:
            self.widget.see("end")  # autoscroll
            


def main_function_():
    speak("Hello there! I am Cofrasoron a intelligent chat bot system Developed By ADNAN")
    print(" ")
    speak("Do you want to change my voice or are you good with this one, please type here yes or no")
    condition_for_voice = input("Yes or no: ")
    if "yes" == condition_for_voice:
        print(" ")
        speak("please type 0 for a male voice and 1 for a female voice")
        voice = int(input("please type 1 for a male voice and 2 or 3 for a female voices: "))
        def user_speak(audio):
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            engine.setProperty('voice',voices[voice].id)
            engine.setProperty('rate',270)
            print(f"Cofrasoron: ",audio)
            engine.say(audio)
            engine.runAndWait()
        user_speak("what is your name, type here")
        name = input("What is your name, please type here: ")
        print(' ')
        user_speak("What's your gender, please type here: ")
        Gender = input("what is your Gender please type here: ")
        with open('C:\\Users\\ALI\\3D Objects\\Chat bot\\User Information','r') as Info_Read:
            var_check_name = Info_Read.readline()
            var_check_Gender = Info_Read.readline()
            if name in var_check_name and Gender in var_check_Gender:
                if "yes" in condition_for_voice:
                    recognised_reply = "welcome It's good to see you back."
                    user_speak(recognised_reply)
                else:
                    Recognised_reply = "welcome It's good to see you back."
                    speak(Recognised_reply)
            else:
                if "yes" in condition_for_voice:
                    print(" ")
                    user_speak("What's your Birth-year ?")
                    print(" ")
                    birth_year = input("What's your Birth-year ?, please type here: ")
                else:
                    speak("What's your gender, please type here: ")
                    print(' ')
                    Gender = input("What's your gender, please type here: ")
                    print(" ")
                    speak("What's your Birth-year ?")
                    print(" ")
                    birth_year = input("What's your Birth-year ?, please type here: ")


    else:
        print("ok not changing voice..")
        speak("what is your name, type here")
        name = input("What is your name, please type here: ")
        print(' ')
        speak("what's your gender")
        Gender = input("what is your gender , please type here: ")
        with open('C:\\Users\\ALI\\3D Objects\\Chat bot\\User Information','r') as Info_Read:
            var_check_name = Info_Read.readline()
            var_check_Gender = Info_Read.readline()
            if name in var_check_name and Gender in var_check_Gender:
                birth_year_data = Info_Read.readline()
                if "yes" in condition_for_voice:
                    recognised_reply = "welcome It's good to see you back."
                    speak(recognised_reply)
                    birth_year_data = Info_Read.readline()
                else:
                    Recognised_reply = "welcome It's good to see you back."
                    birth_year_data = Info_Read.readline()
                    speak(Recognised_reply)
            else:
                if "yes" in condition_for_voice:
                    print(" ")
                    speak("What's your Birth-year ?")
                    print(" ")
                    birth_year = input("What's your Birth-year ?, please type here: ")
                else:
                    speak("What's your gender, please type here: ")
                    print(' ')
                    Gender = input("What's your gender, please type here: ")
                    print(" ")
                    speak("What's your Birth-year ?")
                    print(" ")
                    birth_year = input("What's your Birth-year ?, please type here: ")



    def without_voice_change_commands():
        
        if "male" == Gender:
            gender = "Sir"
        else:
            gender = "Ma'am"
        print("Hello ",gender,'\n')

        def current_time():
            current_hour = datetime.datetime.now().hour
            current_minute = datetime.datetime.now().minute
            time = "The time is now ", current_hour," hours ",current_minute," minutes."
            speak(time)


        def WishMe():
            hour = datetime.datetime.now().hour
            wishing_morning = "good morning ",name,gender
            wishing_afternoon = "good afternoon ",name,gender
            wishing_evening = "good evening ",name,gender
            if hour >= 0 and hour < 12 :
                speak(wishing_morning)
                print("Good morning",gender)
            elif hour >= 12 and hour < 16 :
                speak(wishing_afternoon)
                print("Good afternoon",gender)
            elif hour >= 16 and hour < 24 :
                speak(wishing_evening)
                print("Good evening",gender)
            
        print(" ")
        WishMe() 
        print(" ")
        first_Command = 1
        def LOOP():
            while True:
                if first_Command == 1 : 
                    store_1 = "Welcome",gender," I am here to help you!"
                    store_2 = "So, what would you like me to help you with your first command", gender,"?"
                    store_3 = "Cofrasoron in your service", gender
                    command_reply = [store_1,store_2,store_3]
                    speak(random.choice(command_reply))
                else:
                    store_4 = "What's the next command for me", gender
                    store_5 = "What's your next command", gender,"?"
                    next_command_reply = ["What would you like me to help you next with?","How can i help you next?",store_4,"Ready to take next command, Your commands at priority",store_5 ]
                    speak(random.choice(next_command_reply))
                print(" ")
                query = input("Please type your command here: ")
                print(" ")

                if "time" in query:
                    try:
                        current_time()
                    except:
                        speak("Unable to get current time.")

                elif "99 names of allah" in query:
                    reply_ok = "ok", gender,".."
                    speak(reply_ok)
                    os.startfile("C:\\Users\\ALI\\Videos\\yt1s.com - Coke Studio Special  AsmaulHusna  The 99 Names  Atif Aslam.mp4")

                elif 'how are you' in query:
                    health_type_how_are_you = ['i am fine how about you sir?','i am great how about you sir?','My A I mood levels are always positive sir , how about you sir?']
                    speak(random.choice(health_type_how_are_you))

                elif 'fine' in query:
                    health_type_fine = ["it's good to know that you are fine sir",'I am impressed.']            
                    speak(random.choice(health_type_fine))

                elif 'wikipedia' in query:
                    try:
                        speak("searching wikipedia")
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences = 3)
                        speak("According to Wikipedia")
                        speak(results)
                    except:
                        speak("unable to get the information..")

                else:
                    speak("Sorry, I don't have the answer for that.")
                    first_Command += 1
                    LOOP()
                    break


    def with_voice_change_commands():
        
        if "male" == Gender:
            gender = "Sir"
        else:
            gender = "Ma'am"
        print(gender)

        def current_time():
            current_hour = datetime.datetime.now().hour
            current_minute = datetime.datetime.now().minute
            time = "The time is now ", current_hour," hours ",current_minute," minutes."
            user_speak(time)


        def WishMe():
            hour = datetime.datetime.now().hour
            wishing_morning = "good morning ",name,gender
            wishing_afternoon = "good afternoon ",name,gender
            wishing_evening = "good evening ",name,gender
            if hour >= 0 and hour < 12 :
                user_speak(wishing_morning)
            elif hour >= 12 and hour < 16 :
                user_speak(wishing_afternoon)
            elif hour >= 16 and hour < 24 :
                user_speak(wishing_evening)
            
        print(" ")
        WishMe() 
        print(" ")
        first_Command = 1
        def loop():
            while True:
                if first_Command == 1 : 
                    store_1 = "Welcome",gender," I am here to help you!"
                    store_2 = "So, what would you like me to help you with your first command", gender,"?"
                    store_3 = "Cofrasoron in your service", gender
                    command_reply = [store_1,store_2,store_3]
                    user_speak(random.choice(command_reply))
                else:
                    store_4 = "What's the next command for me", gender
                    store_5 = "What's your next command", gender,"?"
                    next_command_reply = ["What would you like me to help you next with?","How can i help you next?",store_4,"Ready to take next command, Your commands at priority",store_5 ]
                    user_speak(random.choice(next_command_reply))
                print(" ")
                query = input("Please type your command here: ")
                print(" ")

                if "time" in query:
                    try:
                        current_time()
                    except:
                        user_speak("Unable to get current time.")

                elif "99 names of allah" in query:
                    reply_ok = "ok", gender,".."
                    user_speak(reply_ok)
                    os.startfile("C:\\Users\\ALI\\Videos\\yt1s.com - Coke Studio Special  AsmaulHusna  The 99 Names  Atif Aslam.mp4")

                elif 'how are you' in query:
                    health_type_how_are_you = ['i am fine how about you sir?','i am great how about you sir?','My A I mood levels are always positive sir , how about you sir?']
                    user_speak(random.choice(health_type_how_are_you))
                
                elif 'fine' in query:
                    health_type_fine = ["it's good to know that you are fine sir",'I am impressed.']
                    user_speak(random.choice(health_type_fine))

                elif 'wikipedia' in query:
                    try:
                        user_speak("searching wikipedia")
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences = 3)
                        user_speak("According to Wikipedia")
                        speak(results)
                    except:
                        user_speak("unable to get the information..")
            


                else:
                    user_speak("Sorry, I don't have the answer for that.")
                    first_Command += 1
                    loop()
                    break


    with open("C:\\Users\\ALI\\3D Objects\\Chat bot\\User Information",'w') as Info_WRITE:
        Info_WRITE.write('Name of the user: ')
        Info_WRITE.write(name)
        Info_WRITE.write('\n')
        Info_WRITE.write('Gender of the user: ')
        Info_WRITE.write(Gender)
        Info_WRITE.write('\n')
        Info_WRITE.write('Birth Year of the user: ')
        Info_WRITE.write(birth_year)
            
        if "yes" in condition_for_voice:
            with_voice_change_commands()
        else:
            without_voice_change_commands()
        a_file = open('C:\\Users\\ALI\\3D Objects\\Chat bot\\User Information','r')
        # birth_year 
        for position, line in enumerate(a_file):
            if position in birth_year:
                print(line)    
                Info_WRITE.write(line)
                Info_WRITE.write('\n')
        








terminal = Text(main_screen)
terminal.configure(background="Black",foreground="Green")
terminal.configure(width=35,height=31)
terminal.configure(font=('austere',15))
terminal.place(x=40,y=90)


old_stdout = sys.stdout    
sys.stdout = Redirect(terminal)



main_screen.mainloop()
sys.stdout = old_stdout
