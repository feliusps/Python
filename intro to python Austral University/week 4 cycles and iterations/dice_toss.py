#For this project, we will create a program that simulates the roll of the dice.
#Every time we run the program, it will choose two random numbers between 1 and 6.
#The program will have to print them on the screen, print their sum
#and ask the user if they want to roll the dice again.

from random import randint

#greeting the user if he want to play
print("Welcome to play dice")

# while loop for keep going with the game
while True: 
    first_roll = (randint(1, 6))
    second_roll = (randint(1, 6))
    add_the_numbers = first_roll + second_roll
    print("the first roll is = ", first_roll)
    print("the second roll is = ", second_roll)
    print('the sum of the two numbers is :',add_the_numbers)
    
    #ask for the user input
    user_choice = input("do you want to keep playing Y/N ")
    if user_choice.lower()== 'y': # if yes keep playing
        continue
    else: #if not break
        print("see you later") 
        break 
    
