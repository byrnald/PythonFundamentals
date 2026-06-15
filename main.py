#Weekly milestone week 5
import re as regex
import sys

#TODO read the text from a file passed as a command-line argument


if len(sys.argv) < 2:
    print("Please Enter Both Files!")
    print("Example: python workingfile.py test_file.txt")
    sys.exit()

file_name = sys.argv[1]

with open(file_name, "r", encoding="utf-8") as file:
    content = file.read()


formated_content = content.lower().split()

#TODO FORMAT everything with f strings, starting from top 
#1. Word count, character count (with / without spaces) , sentence count

word_count = {}
count = 0
for word in formated_content:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("Word Count:\nWord:           | Count:")

#! We're here for word count 
# * completed.
for key, value in word_count.items():
    print(f"{key:<15} | {value}")

#! Now here: 
#* Status: Complete
#Character count 
char_count = 0
char_count = {}

#paragraph_for_char = paragraph.lower().replace(" ", "")
content_char = content.strip().lower().replace(" ", "")
print("Testing: ")

#? Here we are just uniting all the characters/words into one whole

#* which then this comes in to play
for char in content_char:
    if char in char_count:
        char_count[char] +=1
    else:
        char_count[char] = 1
print("Character Count: \nChar  |  Count")
for key, value in char_count.items():
    print(f"{key:<5} | {value}")
#sentence count
#! Work on sentence count now
#* Status: Complete.

content_sentence = content.strip().rstrip(".").split(".")
len_content_sentence = len(content_sentence)
print(f"Sentence Count: {len_content_sentence}")

#! Problem
#! Here
#! Work from here and keep going down, most of other comments should be done.
#* Completed (content)

#TODO Testing the sentence count apperently it was wrong.
#testing_sentence = "Sentence one. Sentence two."
#test_sentence = testing_sentence.rstrip(".").split(".")
#print("TESTING: ")
#print(len(test_sentence))
#? End of test here.


#Top 10 most common words:

sorted_dict = sorted(word_count.items(), key=lambda kv: kv[1], reverse=True)

top_sorted_words = sorted_dict[:10]

top_dict_words = dict(top_sorted_words)
top_dict_keys = top_dict_words.keys()

#print("Top 10 Words: ")
#for word in top_dict_keys:
    #print(word, end= "\n" )
#* Status Complete.
#* Trying to format the top 10 words with their keys (words) and values (occurences)
print("Top 10 Words: ")
for key, value in top_dict_words.items():
    print(f"{key:<10} | {value}")


#! TODO instead of using min/max as numbers, use words: 
#longest and shortest word:

longest_word = formated_content[0]
shortest_word = formated_content[0]

#use paragraph_v2
for word in formated_content:
    if len(word) > len(longest_word):
        longest_word = word
    if len(word) < len(shortest_word):
        shortest_word = word
print(f"Longest Word: {longest_word}\nShortest Word: {shortest_word}")    

#! UNTIL HERE FIX RED TODO (up) 
#* Completed 

#check for emails using regex
pattern_email = r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-z]{,3}'
pattern_URLS = r'[a-zA-Z]+[://]+[a-zA-Z]+\.[a-zA-Z]{,3}'

#? Why another paragraph string?
#* just to have the text a blit cleaner and a bit more organized.

finding_emails = regex.findall(pattern_email, content)
print(f"Emails Found: \n{finding_emails}")

finding_URLS = regex.findall(pattern_URLS, content)
print(f"URLs Found: \n{finding_URLS}")


