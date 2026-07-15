#Monday



import collections


point = (3,4)
rgb = (255, 128, 0)

x, y = point
print(x, y)


Point = collections.namedtuple("Point", ["x", "y"])
#* using this basically prepares a tuple for us, like a blueprint
#* where we use the first part of the namedtuple as a function 
#* and it'll hold 2 values,  (we can give how many values we  want)
#! the variable name and the name in namedtuple need to be the same 

p1 = Point(x=5, y=6)
print(p1.x)

Colors = collections.namedtuple("Colors", ["x","y"])
color1 = Colors(x="Red", y="Blue")

print(color1.x)
#* Normally for tuples we cannot access them using names. 
#* using collections.namedtuple we are capable of doing so
#* we just give the variable name and . the placeholder of the values
#* inside the tuple


Pokemon = collections.namedtuple("Pokemon", ["x", "y"])

zekrom = Pokemon("Zekrom", "5900")

print(zekrom.x, zekrom.y)
#* zekrom.x prints out the first part "Zekrom"
#* zekrom.y prints out the second part "5900"




#Tuesday :
 
phonebook = {
    "Byron": "201-999-999"
}

phonebook["Carl"] = "908-123-1234"
phonebook["Jit"] = "123-589-5900"

print(phonebook["Carl"]) #Looking it up to see if it was added. (it worked)
print(phonebook.get("Carl")) #similar way of looking things up based on key

del phonebook["Carl"] #* this directly deletes the key that's specified 
print(phonebook.get("Carl", "Not here anymore")) 
#* the .get() function works by giving it what key it needs to find
#* and if doesnt find it, it will print out the given message
  
print(phonebook.get("Byron", "testing "))
#* since Byron was not deleted, this message will not print 
#* the .get() will only activate to safely return a the message if the key is NOT there


for key, value in phonebook.items():
    print(f"Name: {key:<8} | #: {value}")







print("\nWednesday: ")

text = "this is just quick test for the practice question."

word_frequency = {word: text.count(word) for word in text.split()}
#print(word_frequency)
#* this is basically saying the key will be the words seperated at blank spaces
#* because of of text.split() and the value will be the count of the that word
#* that is in the string of text

for key, value in word_frequency.items():
    print(f"{key:<10} | {value}")

#Same thing just with a for loop
#for word in text.split():
    #print(word, text.count(word))

top_words = sorted(word_frequency.items(), key=lambda word: word[1], reverse=True)
#* we needed to sort the iterable, in this case a dictionary. we had to use 
#* .items() iterable because it was a dctionary, without it we would not have 
#* been able to access keys and values.
#*then we needed to specify how we were going to sort the list, i used a lambda 
#* function for our values (not keys) and reversed the order so then i can slice it


top_three = dict(top_words[:3])
#* because of sorted() the iterable becomes a tuple, so here i sliced it 
#* since we cant slice a dictionary, and then after i casted it back to a dict

print(f"\nTop 3 words: ")
for key, value in top_three.items():
    print(f"{key:<10} | {value}")

print(f"\nLetter Frequency:")
char_count = {letter: text.count(letter) for letter in text.replace(" ", "").strip()}
for key, value in char_count.items():
    print(f"{key:<10} | {value}")

word_frequency.setdefault("this", "testing")
print(word_frequency)
#* setdefault() becaus searches for the key that we ask it for 
#* similar to a dict, same layout, 2 items, but in this case the value is optional
#* it searches that key, if it doesnt find it, itll add the key and value onto
#* the dictionary.

#! Problem 2 

a = {"key": "value"}

b = {"testing": "stuff"}
c = a

a.update(b)

print(a)
print(b)

#updating a with another value will keep b or c untouched, 
# it will not update anything other than the iterable that is currently updating

merged_dict = a | b
print(merged_dict)
#* merges the two dicts using union, if keys overlap it basically only takes 
#* the values from the dictionary farthest to the right, so B

merged = {**a, **b}
print(merged)
#* unpacks both dictionaries and merges them onto the new iterable
#* but if keys overlap, it will only take the key that was unpacked last


#Thursday :
print(f"\nNew Problem: ")

active_users = ["Byron", "Cris", "Kevin", "Erick"]
premium_users = ["Byron", "Alvin"]

#TODO: Find both active AND premium users (intersection & )

intersect = set(active_users).intersection(premium_users) 
#this gets all of the items what are intersecting with each other 
#in every tuple, so since we have active/premium users, if one name is in 
#both lists it means they'd intersect
#we can use & instead of .intersection() as well for the same result
#although they both need to set() for &, and only the first one needs to be a 
#set for .intersect()

print(f"\nActive AND premium user(s): {intersect}")

#TODO: Active but NOT premium (difference - )
differ = set(active_users).difference(premium_users)
#? what does .difference() do and why;s it different from .intersection()
#* .difference() does the opposite of .intersection(), it gets almsot all of the 
#* items that are not the same between both lists, in our case
#* since Byron existed in both lists, it wont take that, but alvin
#* only exists on the second list, not in the first so that won;t be taken either
#* so simply .intersection gets the names that are in both lists, difference
#* gets the names thats dont show up in both lists, based on the first list 

print(f"\nDifference: {differ}")

#TODO: Either active OR preimum (union |)

either_or = set(active_users).union(premium_users)
print(f"\nActive OR Premium: {either_or}")

#? What does .union() do?
#* gets all the values inside the set/lists and merges them onto one 
#* iterable, if there are duplicates, it will only grab it from the second/
#* farthest right list.

#same answer: set(active_users) | set(premium_users)
#* each one can be written this way, but the other can way only the first 
#* list needs to be casted as a set() not the second one.
#* but this way both need to be casted as a set().

print("Testing: ")



def my_list():
    return [n for n in range(1,11)]

def my_set():
    return set(n for n in range(1,11))

print(f"My list function and my_set function: ")
print(my_list())
print(my_set())
print(f"End of functions. ")

#! Friday

#TODO:(1) 100 students records with name/grade/age 
#TODO:(2) track which users have seen which articles
#TODO:(3) order that events happened 
#TODO:(4) find duplicate emails in 1M addresses fast.

print(f"\nFirst Friday Questions: ")

dif_list = [n for n in  range(1,11)]

print(dif_list)

dif_list.pop(0)

print(dif_list)



seen_transactions = []
current_id = [1,2,3,3,1,2,3,4,5,6,7,8,9,10,1]

#for id  in current_id:
#    if id in seen_transactions:
#        print("seen!")
#    else:
#        print("new!")
#        seen_transactions.append(id)
#this is incredible unifficient, speically if the list were to be thousands
#of values

duplicates = set()
seen = set()
for n in current_id:
    if n in seen:
        print(f"ALREADY SEEN! {n}")
        duplicates.add(n)
    else:
        seen.add(n)
#so basically we have two different sets, duplicates and seen 
# we loop through all of our numbers and if that number is already in our
# seen set() print we've already seen it and add it to our duplicate set()
# if we have not seen it (else) yet, add it to our seen set()
print(f"Seen: {seen}")
print(f"Duplicates: {duplicates}")


print(f"\nFriday Last Problem: ")


information = {
    1: {"name": "Kevin", "age": 21, "email": "kev@gmail.com"}
}
#almost the same format we just talked about, we used used an int as an id for a key
#and as the value a dictionary for their information corresponding to that ID

def add_user(dictionary, new_id, name, age, email):
    dictionary[new_id] = {"name": name, "age": age, "email": email}
    
add_user(information, 2, "Byron", 22, "byrnald@gmail.com")
add_user(information, 3, "Alvin", 25, "alv@gmail.com")

print(f"add_user function:")
print(information)

def get_user(dictionary, id):
    return dictionary.get(id, "ID # Not Found!")

print(f"\nget_user function: ")
print(get_user(information, 2))
print(get_user(information, 5))

print("\ntesting: ")
def update_user(dictionary, id, **kwargs):
    
    if get_user(dictionary, id) == "ID # Not Found!":
        print(f"Could not find ID #: {id}")
    else: 
        dictionary[id].update(kwargs)
        print(f"Sucessfully updated!")


update_user(information, 1, name="Cris")
#can use **kwargs for functions that require more parameters when we dont want 
# change every little detail, just the ones we specify. 
#in our case we only changed the name of the first key, but we could have changed
#any of the parameters inside the sublist, like name, age, or email, or all


print(f"\nDeleting user: ")
def delete_user(dictionary, id):
    if get_user(dictionary, id) == "ID # Not Found!":
        print(f"ID #: {id} not valid!")
    else:
        del dictionary[id]
        print(f"Sucessfully deleted!")

delete_user(information, 1)



print("\nDisplay of info: ")

for key, value in information.items():
    print(f" {key:<2} | {value}")


print(f"\nfind by name: ")


def find_by_name(dictionary, name):
    for main_dict, sub_dict in dictionary.items():
        if sub_dict["name"] == name:
            id = main_dict
            return get_user(dictionary, id)
    return "Not Found!"

print(find_by_name(information, "Byron"))
print(find_by_name(information, "Jit"))

print(f"\n Practice Problems: ")

library = {
    1: {"title": "Harry Potter", "author": "Rowling", "year": 1997},
    2: {"title": "1984", "author": "Orwell", "year": 1949},
    3: {"title": "Dune", "author": "Herbert", "year": 1965},
}


print(f"get_book Function: ")
def get_book(dictionary, id):
    return dictionary.get(id, "get_book function, Error: Not Found!")

print(get_book(library, 5))



print(f"\nfind_by_author function:")
def find_by_author(dictionary, author):
    for key, value in dictionary.items():
        if value["author"] == author:
            return key, value
    return f"No Author: {author} Found!"

print(find_by_author(library, "Orwell"))
print(find_by_author(library, 'Byron'))

print(f"\nget_books_after function: ")
def get_books_after(dictionary, year):
    results = []
    for key, value in dictionary.items():
        if value["year"] > year:
            results.append([key, value])
    if not results:
        return f"No books found after {year}"
    else:
        return results

print(get_books_after(library, 2003))
print(get_books_after(library, 100))

print(f"\nupdate_book Function: ")

def update_book(dictionary, id, **kwargs):
    if get_book(dictionary, id) == "get_book function, Error: Not Found!":
        return "Not Valid (update_book function)"
    else:
        dictionary[id].update(kwargs)

update_book(library, 1, title="The Goat ")


print(f"\nTesting: ")
print(get_book(library, 1))
print(get_book(library, 10))

print()


for key, value in library.items():
    print(key, value)

print(library[1]["title"])



print(f"\nWeekly Milestone: ")

personal_information = {
    "Alice": {"phone": "201-281-XXXX", "email": "alice@gmail.com", "tags": {"friend", "work"}},
    "Kelvin": {"phone": "908-279-XXXX", "email": "k@gmak.com", "tags": {"ka" , "vi"}}
}

print("\nView Function: ")
def view(dictionary, name):
    return dictionary.get(name, "Name Not Found! (view function)")

print(view(personal_information, "Alice"))

print(f"\nAdd Function: ")
def add(dictionary, name, phone, email, tags):
    dictionary[name] = {"phone":phone, "email": email, "tags": {tags}}
    return f"Sucessfully added {name}"

print(add(personal_information, "Byron", "908-279-XXXX", "byrn@gmail.com", "testingTag"))


print(f"\nUpdate Function: ")
def update(dictionary, name, **kwargs):

    if name not in dictionary:
        return f"Error (Update function)"
    else:
        if "tags" not in kwargs:
            dictionary[name].update(kwargs)
            return f"sucessfully updated {name}"
# if used this for tags it would have just created a string of the old dictionary, 
# and new variable we'll have of tags and delete the existing tags
# so itd be something like "tags": update_variable
        else:
            dictionary[name]["tags"].add(kwargs["tags"])
            kwargs.pop("tags")
            dictionary[name].update(kwargs)
# if we are updating tags, we need to go inside the tag Set
# then add onto the existing Set already inside tags at location dict[name]["tags"]
# and then add the word we provided at kwargs["tags"] 
# so at the end its like add the word tag we provided at the Set
# kwargs["tags"]
            return f"Testing else logic"

# print(personal_information["Alice"]["tags"])
# this just print out their tags
# print(personal_information["Alice"])
# this just prints out everything within the Alice dictionary


print(update(personal_information, "Byron", email="5900", tags="vi"))

print(f"\nDelete Contant Function: ")
def delete_contact(dictionary, name):
    if view(dictionary, name) == "Name Not Found! (view function)":
        return f"Error (delete_contanct function)"
    else:
        del dictionary[name]
        return f"Sucessfully deleted {name}"

print(delete_contact(personal_information, "Alice"))
print(view(personal_information, "Byron"))

# practically identical to the view function, so we'll do intersection
# search_by_name = any(key.startswith("Byron") for key in personal_information.keys())
#* This just searches for any name that we give it, if it find it returns true, else false

search_by_name = [(key,value) for key, value in personal_information.items() if key.startswith("Byron")]


print(f"\nSearch By Name: {search_by_name}")

# def tag_viewer(dictionary, name):
#     if view(dictionary, name) == "Name Not Found! (view function)":
#         return "Error (tag_viewer)"
#     else: 
#         return dictionary[name]["tags"]

# intersection for filtering by tag

# filter_by_tag = tag_viewer(personal_information, "Byron").intersection(personal_information, "Kelvin")
# filter_by_tag = personal_information["Byron"]["tags"].intersection(personal_information["Kelvin"]["tags"])
# this filters all of the information and focuses on only the tags, 
# if any tags intersect, it will catch that and then we print it


print(f"\nFiltering By Tag: ")
target_tag = "vi"
filtering_by_tag = [key for key, value in personal_information.items() if target_tag in value["tags"]]
print(f"{filtering_by_tag}\n")

print(f"End of test")
# ! Find duplicate phone using a set:

new_phone = set()
dup = set()
for key, value in personal_information.items():
    if value["phone"] not in new_phone:
        new_phone.add(value["phone"])
        print(f"New Phone {key}")
    else:
        dup.add(value["phone"])
        print(f"Already Seen from {key}")
print(dup)


    # personal_information[key]["phone"]

# duplicate_phone = [value for key, value in personal_information.items() if personal_information[key]["phone"]]
# print(duplicate_phone)

# * Alphabetical order: 
alphabetical_order = dict(sorted(personal_information.items(), key=lambda contact: contact[0]))
print(alphabetical_order.keys())

# can also be done a bit different, like :
# other_version = sorted(personal_information)
# * since sorted automatically sorts things in alphabetical order by default

print("Import: ")

with open("WeeklyMilestone-7", "w") as file:
    for key, value in alphabetical_order.items():
        file.write(f"{key}, {value["phone"]}, {value["email"]}, {"-".join(value["tags"])}\n")

#* here we basically told python to create/open a file with the name given
#* now we set to what we want to do to that file, we want to write onto it
#* so we have "w". then we just put all of what we want to add it in there
#* we want to write the formated output so file.write( formated output )

print("\nImport (after done)")
#! this is just reading after the import was done in csv formart

with open("WeeklyMilestone-7", "r") as file:
    content = file.read()
    print(content)

print(f"\nExport: ")

with open("contacts.csv", "r") as file:
    # content = file.read().rstrip().split(",")
    # content[len(content)-1] = set(content[len(content)-1].split("-")) 

    for line in file:
        clean_line = line.strip().split(",")

        if len(clean_line) != 4:
            continue

        clean_line[-1] = set(clean_line[-1].split("-"))
        personal_information[clean_line[0]] = {'phone':clean_line[1], 'email':clean_line[2], 'tags':clean_line[3]}

for key_name, info in personal_information.items():
    print(f"{key_name:<8} | {info}") 
