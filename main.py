from weighins_manager import storage
from weighins_manager import query

try:
    file_name = input("Enter file name: ")
except ValueError as e:
    print(f"Error!")

# file_name = "weighins_week2.json"
data = storage.load_data(file_name)
program_running = True

average_file_name = "average_weight.json"
weight_average_data = storage.load_data(average_file_name)

while program_running:
    print(f'''
            1. Load Data
            2. Save Data
            3. Average of Weight
            4. Delete Entry
            5. Week Average Menu
            6. Exit 
        ''')

    try:
        user_choice = int(input("Enter Choice: "))
    except ValueError as e:
        print(f"Only Numbers!")
    else:
        if user_choice == 1:
            print(data)
        elif user_choice == 2:
            data_to_save = {}
            day = input("What Day is it: ")
            weight = float(input("Weight: "))

            data_to_save[day] = weight
            data.append(data_to_save)

            save_data_result = storage.save_data(file_name, data)
            print(save_data_result)

        elif user_choice == 3: 
            average_weight_result = query.average_weight(data)
            print(average_weight_result)

        elif user_choice == 4:
            user_key_deletion = input("Key to delete: ")
            delete_entry_result = query.delete_entry(data, user_key_deletion)
            print(delete_entry_result)
            storage.save_data(file_name, data) 
            # after running testing, i noticed that after rerunning the file
            # the test day was still appearing. meaning; 
            # we had to save the new data onto the file

        # TODO this is where going implement the average saving file section
        elif user_choice == 5:
            average_menu = True
#TODO instead of asking for actual input, i might change this to a number choice
#TODO like above, so then we can view (load) that average data after as well.
#TODO but for now it works as intended, saves the weeks average and saves it onto the avg file

            while average_menu:
                print(f'''
                1. Load Data
                2. Save Average to File
                3. Exit to Main Menu
                ''')

                try: 
                    user_choice = int(input("Enter Number: "))
                except ValueError as e:
                    print(f"Only Numbers! (average menu)")

                if user_choice == 1:
                    print(weight_average_data)

                elif user_choice == 2:
                    user_input = input("Week #: ")
                    average_weight_to_save = query.average_weight(data)

                    weight_average_dict = {}
                    weight_average_dict[user_input] = average_weight_to_save
                    # same as before, we created an empty dictionary then
                    # formatted that dictionary with the user's input

                    weight_average_data.append(weight_average_dict)
                    # then we append the new dictionary onto the old list 
                    # which the variable weight_average_data is holding

                    saved_weight_average_data_result = storage.save_data("average_weight.json", weight_average_data)
                    print(saved_weight_average_data_result)
                    # then we have to save that new list (with the appended dict) onto
                    # the file and then we just print it
                
                elif user_choice == 3:
                    average_menu = False
                    print("Going back to main menu")
                    continue
                else:
                    print(f"Try Again!")
        
        elif user_choice == 6:
            program_running = False
            print(f"Exiting!")
        else:
            print(f"Try Again!")