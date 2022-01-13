from os import system

students_first_name = []
students_last_name = []
students_age = []
student_mark = []
   
while True:
     
    data = input("Enter the student's details: ")
    if data == "":
        break

    system("cls") 
    x = data.split()
    if int(x[2]) in range(18, 31) and int(x[3]) in range(1,11):
        students_first_name.append(x[0])
        students_last_name.append(x[1])    
        students_age.append(x[2])
        student_mark.append(x[3])
    else:
        print("This doesn't fit!")
system("cls")    
for i in range(len(students_first_name)):
    print(students_first_name[i],students_last_name[i],students_age[i],student_mark[i])
 
