import random

computer_choice = random.randint(1,100)
counter = 0
user_input = 0

try:
    while user_input != computer_choice:
        
        user_input = int(input("Enter your guess (0-100): "))
        if user_input > computer_choice:
            print("Too high")
            counter+=1
        elif user_input < computer_choice:
            print("Too low!")
            counter+=1
        else:
            print("You chose right!")  
            counter+=1

    if counter >=1 and counter <= 5:
        print(f"Guesses: {counter}. Amazing!")
    elif counter >=6 and counter <= 10:
        print(f"Guesses: {counter}. Good!")
    else:
        print(f"Guesses: {counter}. Keep practicing!")
        
except ValueError:
    print("Only numbers!")
