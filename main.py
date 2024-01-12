from data import indian_personalities
from art import logo, vs
from tkinter import *
import random


score = 0
flag = True


def compare(a, b):
    if a > b:
        return True
    else:
        return False


def gameover():
    global flag
    print("You Losed!!!")
   # print(f"Your Final Score Is : {score}")
    flag = False

flag2=True

print(logo)
while flag2:
    userplay=input("DO YOU WANNA PLAY 'YES' or 'NO' :     \n\n").lower()
    if userplay=="yes":
        flag==True
        while flag:
            char1 = random.choice(indian_personalities)
            char2 = random.choice(indian_personalities)
            text="""---------------------------------------------------
            -----------------------------------------------------------"""
            print(text)
            print("Guess Which Have More Followers On Insta\n\n")
            print(f"********-------{char1['name']}-------*********")
            print(vs)
            print(f"********-------{char2['name']}-------*********")

            userchoice = int(
                input(f"Write '1' for {char1['name']} and '2' for {char2['name']} :   "))
            if userchoice == 1:
                if compare(a=char1["followers"], b=char2["followers"]):
                    print("Correct!!!")
                    score += 1
                else:
                    gameover()
            elif userchoice == 2:
                if compare(a=char2["followers"], b=char1["followers"]):
                    print("Correct!!!")
                    score += 1
                else:
                    gameover()

            print(f"Your Final Score Is : {score}")
    elif userplay=="no":
        flag2==False
