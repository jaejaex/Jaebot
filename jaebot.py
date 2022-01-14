#FIXME: PRE-CONFIG

from tkinter import Y
from matplotlib.pyplot import xcorr
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
import random 
import math
     

#TODO: CLEAR
def clear():
    import os
    os.system("cls")
    return 1

    
bot = ChatBot('Jae')

bot = ChatBot(
    'Jae',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

#FIXME: INTRODUCTION

print('Type something to begin...')
print ('Jae: Hi there! My name is Jae!')
time.sleep(3)
print("Jae: What do you want me to call you?")
user_name = input()

print("Jae: Hello, " + user_name + "! ")
 

#TODO: FEELING/EMOTION

time.sleep(2)
feeling = input("Jae: How are you today? ")

if "good" in feeling:
    print("Jae: I'm good too! ")
if "great" in feeling:
    print("Jae: I'm glad to hear that! ")
if "not good" in feeling:
    print("Jae: I'm sorry to hear that! ")
if "bad" in feeling:
    print("Jae: Aw, I hope your day gets better! ")
if "okay" in feeling:
    print("Jae: I'm glad you are okay! ")


#FIXME: TASKS


while True:


    time.sleep(2)
    tasks = input("Jae: How may I help you? ")


    games = ("Magic 8 Ball", "Heads or Tails")
    # GAMES: MAGIC 8-BALL
    eight_ball_responses = ["Jae: Yes!", "Jae: It is certain.", "Jae: It is decidedly so.", "Jae: Without a doubt!", "Jae: Yes, definitely!", "Jae: You may rely on it.", "Jae: As I see it, yes.", "Jae: Most likely.", "Jae: Outlook good!", "Jae: Signs point to yes!", "Jae: No.", "Jae: Reply hazy, try again.", "Jae: Ask again later.", "Jae: Better not to tell you now.", "Jae: Cannot predict now.", "Jae: Concentrate and ask again.", "Jae: Don't count on it.", "Jae: My sources say no.", "Jae: Outlook not so good.", "Jae: Very doubtful.", "Jae: ...Maybe", ]
    # GAMES: HEADS OR TAILS
    heads_or_tails_responses = ["Jae: I got...heads!", "Jae: I got...tails!"]
#TODO: TIME
    if "time" in tasks:
        print(f"Jae: The current time is {time.asctime()}")
        # conner was here
#FIXME: GAMES
    elif "game" in tasks.lower():
        games = input("Jae: Okay! I can play mutliple games: Heads or Tails, or Magic 8-Ball. ")
#TODO: 8BALL
        if "magic 8-ball" in games.lower(): 
            eight_ball_question = input("Jae: Okay! Ask me a yes or no question. ")
            time.sleep(3)
            print(random.choice(eight_ball_responses)) 
            time.sleep(2)
            eight_ball_again = input("Jae: Would you like to play again?")
            if "Yes" in eight_ball_again:
                while True:
                    time.sleep(2)
                    eight_ball_question = input("Jae: Okay! Ask me a yes or no question. ")
                    time.sleep(3)
                    print(random.choice(eight_ball_responses)) 
                    time.sleep(2)
                    eight_ball_again = input("Jae: Would you like to play again?")
            if "No" in eight_ball_again:
                time.sleep(2)
                print("Jae: Okay!")
#FIXME: HEADS OR TAILS
        elif "heads or tails" in games.lower():
            heads_or_tails_question = input("Jae: Okay! Pick heads or tails, and I'll flip a virtual coin! ")
            time.sleep(3)
            print(random.choice(heads_or_tails_responses))
            time.sleep(2)
            heads_or_tails_again = input("Jae: Would you like to play again?")
            if "Yes" in heads_or_tails_again.lower():
                time.sleep(2)
                heads_or_tails_question = input("Jae: Okay! Pick heads or tails, and I'll flip a virtual coin! ")
                time.sleep(3)
                print(random.choice(heads_or_tails_responses))
                time.sleep(2)
                heads_or_tails_again_again = input("Jae: Would you like to play again?")
                if "No" in heads_or_tails_again_again.lower():
                    time.sleep(2)
                    print("Jae: Okay!")
            elif "No" in heads_or_tails_again.lower():
                time.sleep(2)
                print("Jae: Okay!")
#TODO: MOOD TRACKER
    elif "mood tracker" in tasks.lower():
        time.sleep(2)
        tracker = input("Jae: Would you like to view your current tracker or input a value for today?")
        if "tracker" in tracker.lower():
            while True:
                time.sleep(2)
                print("Jae: Okay, here is your current mood status:")
                show_graph()
        if "input" : "value" in tracker.lower()
        while True:
                time.sleep(2)
           #run bargraphtest.py