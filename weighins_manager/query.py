
def average_weight(data):
    weights_list = [next(iter(items.values())) for items in data]

    result = 0
    for item in weights_list:
        result += item
    result = result / len(weights_list)
    print(f"diving by: {len(weights_list)}")

    return f"Average for the week: {result:.2f}"

def delete_entry(data, key):
    keys_list = [next(iter(items.keys())) for items in data]

    if key not in keys_list:
        return f"Key not found!"

    for item in data:
        for info in list(item.keys()): #just iterating through the keys info being
            # the keys to item (meaning days)
            if key == info:
                del item[key]
    data.pop() #to remove the empty dictionary after
    return f"{key} has been deleted"

            

# Were going to be deleting the entry based off the key that is passed through