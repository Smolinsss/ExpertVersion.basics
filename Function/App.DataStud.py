import random
import os
from faker import Faker

fake = Faker()

stud_names = []   #str
stud_grades = []  #float
stud_years = []   #int

def genStudents(amount = 10):
    for i in range(amount):
        stud_names.append(fake.name())
        stud_years.append(random.randint(1, 5))
        stud_grades.append(round(random.uniform(5.0, 10.0),2))
        

def printStudents():
    for i in range(len(stud_names)):
        print("-" * 45)
        print(i+1, f"{stud_names[i]:30} | {stud_years[i]:2} | {stud_grades[i]}")
    print("-" * 45)    

def addStudent():
    s_name = input("Enter new student name: ")
    s_year = int(input("Enter new student year: "))
    s_grade = float(input("Enter new student grade: "))

    stud_names.append(s_name)
    stud_years.append(s_year)
    stud_grades.append(s_grade)


def removeStudent():
    s_name = input("Enter the name of the student to delete: ")
    s_index = -1
    for i in range(len(stud_names)):
        if stud_names[i] == s_name:
            s_index = i
            break
    if s_index >= 0:
        stud_names.pop(s_index)
        stud_years.pop(s_index)
        stud_grades.pop(s_index) 

def editStudents():
    name_s = input("Enter the name of the student to remove:")
    for i in range(len(stud_names)):
        if stud_names[i] == name_s:
            y = int(input("Enter year: "))
            g = float(input("Enter grade: "))
            stud_years[i] = y
            stud_grades[i] = g

def topStudent():
    max_g = stud_grades.index(max(stud_grades))
    print(f"{stud_names[max_g]:30} | {stud_years[max_g]:2} | {stud_grades[max_g]}")

        
    
def gradeStudent():
    a = int(input("Enter from: "))
    b = int(input("Enter befor: "))
    for i in range(len(stud_grades)):
        if a <= stud_grades[i] <= b:
            print(f"{stud_names[i]:30} | {stud_years[i]:2} | {stud_grades[i]}")
        

def printMenu():
    print("##### STUDENTS DATABASE #####")
    print("1. Show students list")
    print("2. Add a student")
    print("3. Edit a student")
    print("4. Remove a student")
    print("5. Show TOP student")
    print("6. Show a list of students in a grade range")
    print("0. Exit")
    print("#############################")
    option = int(input(">>> "))
    return option

genStudents(5)
while True:
    os.system("cls")
    option = printMenu()

    if option == 1:
        printStudents()
        input("Hit ENTER to continue")
    elif option == 2:
        addStudent()
    elif option == 3:
        editStudents()
    elif option == 4:
        removeStudent()
    elif option == 5:
        topStudent()
        input("Hit ENTER to continue")
    elif option == 6:
        gradeStudent()
        input("Hit ENTER to continue")
    elif option == 0:
        break  

    
    printStudents()
