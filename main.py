
active_mods = {}

with open("mods_config.txt", "r") as file:
    for line in file:
        parts = line.strip().split()

        if line.startswith("#"):
            continue
        if len(parts) != 3:
            continue

        # active_mods[parts[0].strip()] = {"version": parts[1].strip(), "type": "-".join(parts[2])}

        

        parts[2] = parts[2].split("-")

        active_mods[parts[0].strip()] = {"version": parts[1].strip(), "type": set(parts[2])}
        
print(f"{active_mods}\n")



network_nodes = [
    ("Proxmox-Server", "192.168.1.10", "Online"),
    ("Raspberry-Pi", "192.168.1.15", "Offline"),
    ("Managed-Switch", "192.168.1.2", "Online"),
    ("Old-Laptop", "192.168.1.22", "Offline"),
    ("NAS-Storage", "192.168.1.50", "Online")
]



with open("testing_nodes.csv", "w") as file: 
    for item in network_nodes:
        if item[2].startswith("Offline"):
            continue
        file.write(f"{item[0]},{item[1]},{item[2]}\n")

with open("testing_nodes.csv", "r") as file:
    content = file.read()
    print(content)



# ! Tuesday:
print(f"Tuesday: ")
    
from pathlib import Path

current_directory = Path.cwd()

print(current_directory)

with open(f"{Path.cwd()}/week8_tuesday_logs.txt", "r") as file:
    content = file.read()
    print(content)


print(f"Testing")
#*  We basically just got the current working directory and used .glob()
#* to globally find all (*) of the files ending in .txt
txt_files = current_directory.rglob("*.txt")


list_files = []
for file in txt_files:
    size_kb= file.stat().st_size / 1000
    name_file = file.name

    name_size = (size_kb, name_file)
    list_files.append(name_size)

sorting_files = sorted(list_files, key=lambda x: x[0])

for file in sorting_files:
    print(f"{file[1]:<22} | {file[0]}")


#* now we loop through every file in the our variable txt files
#* which finds all files ending in .txt in our current directory

#* we find the info of that file using stat(), and to specify
#* what part of the information we want, in our case the file size
#* is the bytes, so we use .st_size
#* then we divide by 1000 so convert the current bytes into kb

#* Then we need the name of those files, because if we only print the files
#* we'll get the whole path of where that file is, so we use
#* file.name to get only the name of the files we looping through

print('\nOther Test\n')

directory = Path.cwd()
print(f"{directory}\n")
#* just gets the directory in the current working directory

directory_txt_files = directory.glob("*.txt")
#* now we get all the files ending in .txt in that directory

file_information = []
for file in directory_txt_files: 
    name = file.name
    size = file.stat().st_size
    info = (name, size)
    file_information.append(info)

print(file_information)   
#* nowe we loop through every file that ends with .txt
#* and we use .name to get the name of it not, and not extra info 
#* also use .stat().st_size to get the byte size of those files

sorted_information = sorted(file_information, key=lambda f: f[1])
print(f"{sorted_information}\n")



#TODO Wednesday:

import json

contacts = {
    "Alice": {
        "phone": "555-0198",
        "email": "alice@example.com",
        "tags": {"friend", "work"} # Pay close attention to this!
    },
    "Bob": {
        "phone": "555-6742",
        "email": "bob@example.com",
        "tags": {"gym"}
    }
}

# Utilize dump and load from json

print(f"Json\n")

for contact, information in contacts.items():
    information['tags'] = list(information['tags'])

with open ("json_contacts.txt", "w") as file:
    json.dump(contacts, file, indent=2)

with open ("json_contacts.txt", "r") as file:
    file_loader =  json.load(file)
    print(file_loader)


print(f"\nReminder: \n")

current_wd = Path.cwd()
print(current_wd)

all_txt_files = current_wd.glob("*.txt")

working_file = ""
for file in all_txt_files:
    if file.name == "mods_config.txt":
        working_file = file.name

result = {}
with open(f"{Path.cwd()}/{working_file}", "r") as file:
    for line in file: 
        parts = line.strip().split()
        if len(parts) != 3:
            continue
        parts[2] = parts[2].strip().split("-")
        result[parts[0].strip()] = {"version": parts[1].strip(), "type": set(parts[2])}
 
print(result)

info_files = []
txtfiles = Path.cwd().glob("*.txt")

for file in txtfiles:
    f_name = file.name
    f_size = file.stat().st_size
    set_files = (f_name, f_size)
    info_files.append(set_files)

print()
sorted_files = sorted(info_files, key=lambda f: f[1])

print(sorted_files)

print(f"\nThursday\n")

try: 

    with open(f"secret_file.txt", "r") as file: 
        content = file.read()

except FileNotFoundError as e: 
    print(f"File not Found: {e}")
except PermissionError as e:
    print(f"Does not have permission: {e}")

else: 
    print(content)

finally: 
    print("Finally Clause: Done!")

#* with using try, except, else and finally clause
# first we try to open the files that we are trying to read 
# so with open inside the try clause
# after we need the exceptions clause, if the file is not found
# or if we arent allowed, have an exception cause for those errors
# then an else clause, in case the file does open, we print the content
# and a finally clause, where itll print no matter what after everything

#! Practice problem 2: 

print("\nPractice Problem 2:\n")

class ValidationError(ValueError): pass
# First we create a new exception catcher 

def validate_age(age): 
    if age < 0:
        raise ValidationError("Age cannot be negative") 
    else:
        return age
# Then we create a function that validates the age
# if the age is less than 0 we'll raise our error
# else we'll return the age


try:
    function_use = validate_age(1)
except ValidationError as e:
    print(f"Wrong Value! {e}")
else:
    print(function_use)
finally:
    print("Done!")

# Then our try / except / else clause
# we try to enter our validate_age() 
# our except clause will guard our function for any validation erros
# else if no errors then we'll print the function


print(f"\nFriday: \n")

import math_tools as mt


# def main():
    # print(mt.add(5,5))
    

# if __name__ == "__main__":
    # main()

print("\nProblem 2: \n")

# from contacts.storage import save_contacts

# def main():
    # save_contacts()


# if __name__ == "__main__":
    # main()


print(f"\nWeekly Milestone 8:\n")


