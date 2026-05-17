
while True:
    print("1. Star Triangle\n2. Number Pyramid\n3. FizzBuzz\n4. Primes\n5. Rerverser\n6. Quit\n")
    try:
        user_input = int(input("Enter #: "))
        match user_input:
            case 1:
                print("Right Triangle: \n")
                try: 
                    user_number = int(input("Row/Column: "))
                except ValueError:
                    print("Wrong # for row/column! (Try/Except 2)")
                    continue

                for i in range(1, user_number+1):
                        print("*" * i)
            case 2: 
                print("Number Pyramid:\n")

                try:
                    user_pyramid = int(input("Enter Number: "))
                    for i in range(1, user_pyramid+1):
                        for j in range(1, i+1):
                            print(j, end=" ")
                        print()
                    print()

                except ValueError:
                    print("Enter Number! (Try/Except 3)")
                    continue
            case 3: 
                try:
                    user_fb = int(input("Enter Number: "))
                    for num in range(1, user_fb+1):
                        if num % 3 == 0 and num % 5 == 0:
                            print("FizzBuzz!")
                        elif num % 3 == 0:
                            print("Fizz")
                        elif num % 5 == 0:
                            print("Buzz")
                        else:
                            print(f"Nothing! {num} ")
                except ValueError: 
                    print("Number! (Try/Except 4)")
                    continue
            case 4:
                primes = []
                for i in range(2, 101):
                    for j in range(2, i):
                        if i % j == 0:
                            break
                    else:
                        primes.append(i)
                print(primes)
            case 5: 
                while True:
                    print("Choose what to Reverse: ")
                    try:
                        sub_choice = int(input("1. Right Triangle\n2. Number Pyramid\n3. Quit\ninput: "))
                        match sub_choice:
                            case 1: 
                                print("Reversing Triangle: ")
                                try:
                                    r_triangle_num = int(input("Enter Number: "))
                                    for i in range(r_triangle_num, 0, -1):
                                        print("*"*i)
                                except ValueError:
                                    print("Value Error! (Try/Except 6)")
                            case 2: 
                                try:
                                    r_number_pyramid = int(input("Enter Number: "))
                                    for i in range(1, r_number_pyramid+1):
                                        for j in range(r_number_pyramid, i-1, -1):
                                            print(j, end=" ")
                                        print()
                                except ValueError:
                                    print("Wrong! (Try/Except 7)")
                            case 3:
                                print("Quitting . . .\n")
                                break
                    except ValueError: 
                        print("Wrong Input! (Try/Except 5)")
            case 6:
                print("Quitting program . . .")
                break
    except ValueError:
        print("Value Error! (Try/Except 1)")
