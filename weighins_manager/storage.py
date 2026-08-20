
import json
# For the my weighins script, we're going to create a list of dictionaries, for example:
# [ {"Monday": "#"}, {"Tuesday": "#"} ]
# that will be the core function/view of this script, Then either take the average of the whole file 
# could be week 1-9 or etc, or i could create a new folder or new main to calculate the new average 
# use the same weighins_manager (folder) for those files/new week folder

def load_data(file_name):
    try:
        with open(f"{file_name}", "r") as file:
            content = json.load(file)
# Give the variable content the content of that file, basically all that info in that variable 
#* We 'try' to open the content and using the json.load(file) onto a variable 
    except FileNotFoundError as e:
        print(f"Creating File! (File Not Found Exception, load_data function)")
        return []
#* If the file is not found, we notify the user and return an empty list so we create that file with an empty
#* list to start inputting information onto that empty list
    else:
        return content
#* if we do find that file, return that content in that file.

def save_data(file_name, data_to_save):
    try:
        with open(f"{file_name}", "w") as file:
            content = json.dump(data_to_save, file, indent=4)
# Now we use try and except to open the file and write onto it, 'dump' with json.
    except FileNotFoundError as e:
        return f"File Not Found! (save_data function)"
# if file is not found, we'll throw an exception
    else:
        return F"Content Saved!"
# else, the data has been saved and onto the file thats passed through
    


