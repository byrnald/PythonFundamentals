import json

def load_data(file_name):
    try:
        with open(f"{file_name}", "r") as file:
            content = json.load(file)
# here were just using json to load the file and giving it a variable.
    except FileNotFoundError as e:
        print(f"File Not Found! (load_data function) {e}")
        return []
# if the file is not found we create a new list so then we can add content to it.
    else:
        return content
# if there is is a list, we return whats in the content of that file


def save_data(file_name, data_to_save):
# with this function there will be a file and data to save to that file
    try:
        with open(f"{file_name}", "w") as file:
            content = json.dump(data_to_save, file, indent=4)
# we try to open the file so we can write it to it
# and we use json.dump to give it the data to save, onto the file
    except FileNotFoundError as e:
        return f"File Not Found (save_data function) {e}"
# if the file is not found, we get this error
    else:
        return f"Data Saved!"
# else if it everything worked,  the data was saved.
