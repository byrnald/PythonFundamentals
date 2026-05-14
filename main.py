import random

computer_choice = random.randint(1,100)
counter = 0
user_input = 0

while user_input != computer_choice:
    try:
        user_input = int(input("Enter your guess (0-100): "))
        counter+=1
    except ValueError:
        print("Only Ints!")
        continue

    if user_input > computer_choice:
        print("Too high")
    elif user_input < computer_choice:
        print("Too low!")
    else:
        print("You chose right!")  
        if  1 <= counter <= 5:
            print(f"Guesses: {counter}. Amazing!")
        elif 6 <=  counter <= 10:
            print(f"Guesses: {counter}. Good!")
        else:
            print(f"Guesses: {counter}. Keep practicing!")
        
