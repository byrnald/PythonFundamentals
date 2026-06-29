#Weekly Milestone

#TODO: Manage a class of students and their grades, demonstrating every list
#TODO: operation fromt his week. 
#* Specifications: 
#? Student list of dicts: [ {'name':'Alice','grades':[88,92,79] } ]
#? Calculate average grade for each student
#? Sort students by average descending
#? Find: top 3 students, students below 70 average (use comprehensions)
#? Generate a formatted class report with aligned columns
#? Add and remove students dynamically

#! We stopped using list comprehension to print because it was a waste of 
#! memory, it keeps making empty lists just print, it was unecessary.

student_list = [
    {"name":"Byron",
     "grades":[88, 92, 79]},
    {"name":"Cris",
     "grades": [92,52,17]},
    {"name":"Kevin",
     "grades":[82,88,42]},
    {"name": "Erick",
     "grades": [53, 23, 76]}
]

print("Average Grades: ")
average_grade = [(info['name'], sum(info['grades'])/len(info["grades"])) for info in student_list]
#* we used list comphrension to location the name and the lsit of grades in the list of dicts
#* then we took the sum of list of grades in the student_list all in one line


#[print(f"Name: {name:<8} | Grade Average: {grade:.2f}") for name, grade in average_grade]
for name, grade in average_grade: 
    print(f"Name: {name:<8} | Grade: {grade:.2f}")
#* printed only what we needed to output using parenthesis
#* for every name and grade in the list comprehension above

print()
sorted_grades = sorted(average_grade, key= lambda student: student[1], reverse=True)
#* we used sorted() to sort the average grades, using a lambda function
#* then since average_grade is a tuple (name, grade) we had to specify in the 
#* lambda function which index in the tuple do we want to sort by 
#* i picked the grade and then reversed it to have descending order.

print(f"Sorted Students Descending Order: ")
#[print(f"Name: {name:<8} | Grade Avg: {grade:.2f}") for name, grade in sorted_grades]
for name, grade in sorted_grades:
    print(f"Name: {name:<8} | Grade avg: {grade:.2f}")
#*then used list comprehension to print out the name and grade using parenthesis
#* for name and grade in the sorted_grades variable.

#! we are in the step FIND: 
print(f"\nTop 3 Students:")
#[print(f"Name: {name:<8} | Grade: {grade:.2f}") for name, grade in sorted_grades[:3]]
for name, grade in sorted_grades[:3]:
    print(f"Name: {name:<8} | Grade: {grade:.2f}")
#* All i did was access the list of tuples in sorted grades, in a for loop 
#* in this case a list comprehension we already access it, and we give a 
#* variable name to whatever values are with the tuples, in this case it was 
#* just 2 values, so name and grade. and then we specified those name and grade
#* from where we were trying to access them, in this case sorted_grades


print("\nBelow Average Students: ")
#below_average = [(info["name"], sum(info["grades"])/len(info["grades"])) for info in student_list if sum(info["grades"])/len(info["grades"]) < 70]
below_average = [(name, grade) for name, grade in average_grade if grade < 70]
for name, grade in below_average:
    print(f"Name: {name:<8} | Average: {grade:.2f}")
#* in order to get the below average students we accessed the tuple used ()
#* and name and grade to assign variables to whats inside the list of tuples in 
#* average_grade. adding an if statement to filter out and only print who's
#* average grade is less than 70


#* Adding and Deleting 
print("\nAdding and Removing: ")
student_list.append({"name": "Sarah", "grades": [90, 82, 85]})

removing_with_list = [info for info in student_list if info["name"] != "Cris"]
#* here we just filtered out the list of dicts to include everything but the 
#* the section with "Cris" in it
print(removing_with_list)

student_list = removing_with_list
#* since it was the same format of the original list and we wanted to 
#*change the original list, we made the student_list equal to the removing list

for info in student_list:
    print(f"Name: {info['name']} | Grades: {info['grades']}")
#* then we accessed the list of dicts using a for loop and formatted the 
#* how we wanted the output to be based on the keys/values in the dicts