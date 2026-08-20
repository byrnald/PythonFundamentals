def filter_by(data, key, value):
    return [info for info in data if info[key] == value]
# we use list comprehension to loop through the list of dictionaries in one line
# then based on the key we're given we check if its equal to the value we were given

# i was thinking this wasnt going to work as intended BUT
# info[key] is the location of WHERE were going to be looking at, so that itself
# will hold an item
# if that item is EQUAL to that value passing through
# we return that dictionary


def first_filtered(data, key, value):
    for info in data:
        if info[key] == value:
            return info
# we loop through list of dictionaries
# if the location at info[key] is equal to the value given, we return that dictionary

def sorted_info(data, key):
    sorted_information = sorted(data, key=lambda item: item[key])
    return sorted_information
# we created a new variable for the sorted list of dictionaries
# we used the built-in sorted function based on our data (list of dicts)
# and the key we will base the sort off of.

