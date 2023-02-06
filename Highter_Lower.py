"""This program will help the user to find a random number"""
import random

random_number = random.randint(0,100)
i=1
print("Welcome to game!Try to guess the random number that the computer chose." +" \n" + "\
    You have 10 attempts! Good Luck! ")

while i <= 10:
    user_number = int(input("Please introduce your number: "))
    if user_number < random_number:
        print("The random number is bigger!")
        i += 1
        if i == 11:
            print("You lost!")
    elif user_number > random_number:
        print("The random number is smaller")
        i += 1
        if i ==11 :
            print("You lost!")
    else :
        print("Congratulation, you guess the number!")
        break
