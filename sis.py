from ast import ImportFrom
import json
import matplotlib.pyplot as plt
import csv

students_grades = {}

courses_information = {}

students_information = {}

def Writecsv(students_grades):
    
    file = open("course-code.csv","w")
    file.write("ID,Course Code,Grade\n")
    
    for i in students_grades.keys():
        
        for c,g in students_grades[i].items():
            
            file.write("{},{},{}\n".format(i,c,g))    
    
    file.close()

def ReadCsv():
    
    file = open('course-code.csv', 'r+')
    
    try:
       
        reader = csv.reader(file)
        next(reader)
    
    except:
        
        file.write("ID,Course Code,Grade\n")
    
    for row in reader:
        
        id, course_code, grade = row
        
        if id not in students_grades:
            
            students_grades[id] = {}
        
        students_grades[id][course_code] = grade

def PrintHtml(a,b,f):
    
    file = open("student-code.html","w")
    head = "<title> students result</title>"
    body = f"\n<h1>{a}</h1>\n<h2>{f}</h2>\n<h3>{b}</h3>\n"
    image = "\n<img src='https://sis.sut.edu.eg/images/logo_Pages.png' alt='' style='position: relative;left: -810;width: 400;top: 10;'>"
    html = "<html><head>{}</head>\n<body style='text-align: center;background-color: rgb(234, 234, 234);'><header style='background-color: rgb(255, 255, 255);width: 110%;height: 150px;margin-top: -8;position: relative;left: -10;'>{}</header>{}</body></html>".format(head,image, body)
    file.write(html)
    file.close()

def ReadStudentsJson():
    
    global students_information
    file=open("students.json","r")
    content=file.read()
    
    try:
        
        students_information=json.loads(content)
    
    except:
        
        students_information = {}
    
    file.close

def WriteStudentsJson():
    
    file = open("students.json","w")
    json.dump(students_information,file)
    file.close()

def ReadCoursesJson():
    
    global courses_information
    file=open("courses.json","r")
    content=file.read()
    
    try:
        
        courses_information=json.loads(content)
    
    except:
        
        courses_information = {}
    
    file.close

def WriteCoursesJson():
    
    file = open("courses.json","w")
    json.dump(courses_information,file)
    file.close()

def ShowMainPage():
        
        welcome_text = "Welcome to Students Informaion System"
        print(f"\n{welcome_text.center(150)}\n")
        print(("-----------------------\n").center(150))
        print(("students information [Student]\t[Course] courses information\n").center(145).expandtabs(20))
        print(("Show final result [Final]  for a student\n ").center(152).expandtabs(20))
        print(("[Exit]\n").center(155))            
    
def ShowStudents_dict():
        
        print()
        print(("Show Students Information [1]\t[2] Add Student Information\n").center(147).expandtabs(20))
        print(("Edit Student Information [3]\t[4] Remove Student Information\n").center(152).expandtabs(16))
        print(("Supply grades for a student [5]\t[6] Supply Courses for a Student\n").center(152).expandtabs(20))
        
        print(("Prev[7]ious\n").center(154))

def ShowStudentCourses():
    
    print("")
    print(("Add Course to a Student [1]\t[2] Remove course of Student\n").center(145).expandtabs(20))
    print(("Show pie chart for [3] course registration\n").center(153).expandtabs(20))

def coursesShow_dict():
            
            print()
            print(("Show Courses Information [1]\t[2] Add Course Information\n").center(145).expandtabs(20))
            print(("Edit Course Information [3]\t[4] Remove Course Information\n").center(150).expandtabs(16))
            print(("Prev[5]ious\n").center(154))

def MainPage():
    
    ShowMainPage()
    
    while True: 
        
        user_choose = (input("\nEnter Your Choose , Enter Exit many times to exit : ").title().strip())
        
        
        if user_choose == "Student": 
            
            students_dict()
        
        elif user_choose == "Course":
            
            courses_dict()

        elif user_choose == "Exit":
            
            break
        
        elif len(user_choose) == 0 :
  
            ShowMainPage()
            print("invalid choose")
        
        elif user_choose == "Final":
            
            show_student_final_result()
        
        else:
            
            ShowMainPage()
            print("invalid choose")

def students_dict():         
    
    ShowStudents_dict()
    
    while True:
        
        user_input =(input("\nOpration Number , Enter Exit many times to exit : ").title())
        
        if user_input == "1":
            
            ReadStudentsJson()
            ShowStudents_dict()
            print(students_information)
        
        elif user_input == "2":
            
            name = input("Enter Student Name :").strip()
            print("Enter Student birth date")
            day = (input("Enter Day : ")).strip()
            month = (input("Enter Month : ")).strip()
            year = (input("Enter Year : ")).strip()
            Id = (input("Enter Student ID : ")).strip()
            
            if Id in students_information:
               
                ShowStudents_dict()
                print("This Id is already exists ")
            
            else:
                
                if len(name) == 0 or len(day) == 0 or len(month) == 0 or len(year) == 0 or len(str(Id)) == 0 :
                    
                    ShowStudents_dict()
                    print("There is missing information")
                
                elif Id.isdigit() == False:
                    
                    ShowStudents_dict()
                    print("The ID Must Be Numbers Only")
                    
                
                elif name.isdigit() == True or name.isalpha()== False:
                    
                    ShowStudents_dict()
                    print("The Name Must Be Characters Only")

                elif day.isdigit() == False or  (int(day) >31 or int(day) <1):
                    
                    ShowStudents_dict()
                    print("The Day Must Be Numbers Only or Your Day Is Above 31 or Your Day Is below 1")                                   
                
                elif month.isdigit() == False or ( int(month) >12 or int(month) <1) :
                    
                    ShowStudents_dict()
                    print("The Month Must Be Numbers Only or Your Month Is Above 12 or Your Month Is below 1")                                   
                
                elif year.isdigit() == False or ( int(year) >2024 or int(year)<1) :
                    
                    ShowStudents_dict()
                    print("The Year Must Be Numbers Only or Your Day Is Above 2024 or Your Month Is below 1")                                   
                
                else:
                   
                    ReadStudentsJson()
                    students_information[Id]={"Name" :name, "Birthdate" : f"{day}/{month}/{year}"}
                    WriteStudentsJson()     
                    ShowStudents_dict()
                    print("The student was added successfully")
            
        elif user_input == "3":
            ReadStudentsJson()
            print(students_information)
            Edit_choose = (input("Enter the the student ID that you want to edit his inform : ")).strip()
            
            if str(Edit_choose) in students_information.keys() :
                name = input("Enter Student Name :").strip()                                                           
                print("Enter Student birth date")
                day = (input("Enter Day : ")).strip()
                month = (input("Enter Month : ")).strip()
                year = (input("Enter Year : ")).strip()                       
                
                if  len(day) == 0 or len(month) == 0 or len(year) == 0 or len(name) == 0 :
                    ShowStudents_dict()
                    print("There is missing information")
                
                elif day.isdigit() == False and  (int(day) <=31 or int(day) >=1):
                    ShowStudents_dict()
                    print("The Day Must Be Numbers Only or Your Day Is Above 31 or Your Day Is below 1")                                   
                
                elif month.isdigit() == False and ( int(month) <=12 or int(month) >=1) :
                    ShowStudents_dict()
                    print("The Month Must Be Numbers Only or Your Month Is Above 12 or Your Month Is below 1")                                   
                
                elif year.isdigit() == False and ( int(year) <=2024 or int(year)>=1) :
                    ShowStudents_dict()
                    print("The Year Must Be Numbers Only or Your Day Is Above 2024 or Your Month Is below 1")
                
                elif name.isdigit() == True or name.isalpha()== False:
                    
                    ShowStudents_dict()
                    print("The Name Must Be Characters Only")
                
                else:
                    students_information[str(Edit_choose)]={"Name" : name,"Birthdate" : f"{day}/{month}/{year}"} 
                    WriteStudentsJson()
                    ShowStudents_dict()
                    print("The student was successfully modified.")
                
            elif len(str(Edit_choose)) == 0 : 
                ShowStudents_dict()   
                print("this ID didn't found")  
            
            else: 
               ShowStudents_dict()
               print("this ID didn't found")              

        elif user_input =="6":
            
            ShowStudentCourses()
            ReadCoursesJson()
            ReadStudentsJson()
            user_choose = input("Enter Your Choose : ").title().strip()
            
            if len(user_choose) == 0:
                ReadCoursesJson()
                ReadStudentsJson()
                ReadCsv()
                ShowStudents_dict()
                print("invalid choose")
            
            elif user_choose == "1":
              
                ReadCoursesJson()
                ReadStudentsJson()
                ReadCsv()
                student_id = (input("Enter Student ID : ")).strip()
                
                if len(student_id) == 0 :
                    ShowStudents_dict()
                    print("There is missing information")
                
                elif student_id.isdigit() == False :
                    ShowStudents_dict()
                    print('ID must be numbers only')
                
                elif student_id not in students_information:
                    ShowStudents_dict()
                    print("Student not found.")
                
                else:
                    ReadCoursesJson()
                    ReadStudentsJson()
                    ReadCsv()
                    course_code = (input("Enter Course Code : ")).strip().upper()
                    
                    if len(course_code) == 0 :
                        ShowStudents_dict()
                        print("There is missing information")

                    elif course_code not in courses_information.keys():
                        
                        ShowStudents_dict()
                        print("Course not found.")

                    elif course_code.isdigit() ==True or course_code.isalnum() ==  True or course_code.isalpha() == True :
                        ReadCoursesJson()
                        ReadStudentsJson()
                        ReadCsv()
                        if "Courses" not in students_information[student_id].keys():
                            students_information[student_id]["Courses"]= []
                            students_information[student_id]["Courses"].append(course_code)  
                            WriteCoursesJson()
                            WriteStudentsJson()
                            ShowStudents_dict()
                            
                            print(f"Course {course_code} has been added to student {student_id}")
                        
                        elif course_code in students_information[student_id]["Courses"]:
                            
                            ShowStudents_dict()
                            print("This Course Already Added")
                        
                        else:
                            
                            students_information[student_id]["Courses"].append(course_code)  
                            WriteCoursesJson()
                            WriteStudentsJson()
                            ShowStudents_dict()
                            
                            print(f"Course {course_code} has been added to student {student_id}")

                    else:
                        ShowStudents_dict()
                        print("This ID and Course code could be already exist, please try again")

            elif user_choose == "2":

                ReadCoursesJson()
                ReadStudentsJson()
                ReadCsv()
                student_id = (input("Enter Student ID : ")).strip()
                
                if len(student_id) == 0 :
                    
                    ShowStudents_dict()
                    print("There is missing information")
                
                elif student_id.isdigit() == False :
                    
                    ShowStudents_dict()
                    print('ID must be numbers only')
                
                elif student_id not in students_information:
                    
                    ShowStudents_dict()
                    print("Student not found.")
                
                else:
                    ReadCoursesJson()
                    ReadStudentsJson()
                    ReadCsv()
                    course_code = (input("Enter Course Code : ")).strip().upper()
                    
                    if len(course_code) == 0 :
                        
                        ShowStudents_dict()
                        print("Missing Information")
                        
                    
                    elif "Courses" not in students_information[student_id].keys():
                            
                            ShowStudents_dict()
                            print("This student does not have any course.")
                    
                    
                    else:
                        ReadCoursesJson()
                        ReadStudentsJson()
                        ReadCsv()
                        if course_code not in students_information[student_id]["Courses"]:
                            
                            ShowStudents_dict()
                            print("Course not found.")     
                        
                        elif course_code.isdigit() ==True or course_code.isalnum() ==  True or course_code.isalpha() == True :
                            
                            students_information[student_id]["Courses"].remove(course_code)  
                            WriteCoursesJson()
                            WriteStudentsJson()
                            ShowStudents_dict()
                            
                            print(f"Course {course_code} has been removed to student {student_id}")
               
                        else:
                            ShowStudents_dict()
                            print("The course is already removed from the list.")

            elif user_choose == "3":
                WriteCoursesJson()
                WriteStudentsJson()
                ShowStudents_dict()
                course_counts = {}

                for student_id, info in students_information.items():
                    
                    courses = info.get("Courses", [])
                    
                    for course in courses:
    
                        course_counts[course] = course_counts.get(course, 0)+1
                        

                plt.pie(course_counts.values(), labels=course_counts.keys(),autopct='%1.1f%%', startangle=140)
                plt.title('Course Registration Distribution')
                plt.show()
                ShowStudents_dict()
                
            
            
            else:
                ShowStudents_dict()
                print("Please enter a valid option.")

        elif user_input == "4":
            
            ReadStudentsJson()
            print(students_information)  
            remove_choose = (input("Enter the the student ID that you want to remove his inform : ")).strip()
            
            if remove_choose.isdigit()== False:
                ShowStudents_dict()
                print("Write Numbers Only ")
            elif len(remove_choose) == 0:
                ShowStudents_dict()
                print("There is missing information")
            elif remove_choose not in students_information.keys():
                ShowStudents_dict()
                print("this ID didn't found") 

            else:
                ShowStudents_dict()
                del students_information[str(remove_choose)]
                print("The student was removed successfully")
                WriteStudentsJson()
        
        elif user_input == "7":
            ShowMainPage()
            break
        
        elif len(user_input) == 0 :
            
            ShowStudents_dict()
            print("invalid choose")
        
        elif user_input == "5":
           
            supply_grades()
        
        else:
            
            ShowStudents_dict()
            print("invalid choose")

def courses_dict():
    
    coursesShow_dict()
    
    while True:
        
        user_input =(input("\nOperation Number , Enter Exit many times to exit : ")).title().strip()
        
        if user_input == "1":
            ReadCoursesJson()
            coursesShow_dict()
            print("")
            print(courses_information)
        
        elif user_input == "2":
            
            ReadCoursesJson()
            code = input("Enter Course Code :").strip().upper()
            name = input("Enter Course Name :").strip().lower()
            max_degree = (input("Enter Course Max Degree : ")).strip()
            Credit_hours = (input("Enter Course Credit Hours : ")).strip()
            
            if code in courses_information:
                coursesShow_dict()
                print("This course already exists.")
            
            else:
               
                if max_degree.isdigit() == False:
                    
                    coursesShow_dict()
                    print("The Max Degree Must Be Numbers Only ") 
            
                elif Credit_hours.isdigit() == False:
                    
                    coursesShow_dict()
                    print("The Credit Hours Must Be Numbers Only ") 
            
                elif len(code)== 0 or len(name)== 0 or len(max_degree)== 0 or len(Credit_hours)== 0:
                    
                    coursesShow_dict()
                    print("There is missing information")
           
                else:
                    coursesShow_dict()
                    courses_information[code]={"Name" : name , "Max Degree" : max_degree, "Credit Hours": Credit_hours}
                    print("The Course was added successfully")
                WriteCoursesJson()
                
            
        elif user_input == "3":
            ReadCoursesJson()
            print(courses_information)                                                             
            Edit_choose = input("Enter the the course Code that you want to edit its information : ").strip().upper()
            
            if Edit_choose in courses_information.keys():
                name = input("Enter Course Name :").strip()                                         
                max_degree = (input("Enter Course Max Degree : ")).strip()
                Credit_hours = (input("Enter Course Max Degree : ")).strip()
               
                if len(Edit_choose)== 0 or len(name)== 0 or len(str(max_degree))== 0 or len(Credit_hours)== 0 :
                   
                    coursesShow_dict()
                    print("There is missing information")
                
                elif max_degree.isdigit() == False:
                   
                    coursesShow_dict()
                    print("The Max Degree Must Be Numbers Only ") 
               
                elif Credit_hours.isdigit() == False:
                   
                    coursesShow_dict()
                    print("The Credit Hours Must Be Numbers Only ")
                
                else:
                    coursesShow_dict()
                    courses_information[Edit_choose]={"Name" : name , "Max Degree" : max_degree,"Credit Hours":Credit_hours}    
                    print("The student was successfully modified.")
                    WriteCoursesJson()             
            else:
                coursesShow_dict()
                print('No such course exist')

        elif user_input == "4":
            
            ReadCoursesJson()
            print(courses_information)  
            remove_choose = input("Enter the the course Num that you want to remove its information : ").strip().upper()
            
            if len(remove_choose)== 0:
               
                coursesShow_dict()
                print('Please enter the number of the Course you want to remove ')
            
            elif remove_choose not in courses_information:
               
                coursesShow_dict()
                print('That Course Does Not Exist')
            
            else:
                coursesShow_dict()
                del courses_information[remove_choose]
                print("The Course was removed successfully")
                WriteCoursesJson()
        
        elif user_input == "5":
           
            ShowMainPage()
            break
        
        elif len(user_input) == 0 :
            
            coursesShow_dict()
            print("invalid choose")
        
        else:
            
            coursesShow_dict()
            print("invalid choose")

def supply_grades():
    ReadStudentsJson()
    ReadCoursesJson()

    student_id = (input("Enter the student's ID: ")).strip()
    course_code = input("Enter the course code: ").strip().upper()
    grade = (input("Enter the student's grade for the course: ")).strip()
    
    if len(student_id)==0 or len(grade)==0 or len(course_code)==0 :
        
        ShowStudents_dict()
        print("There is missing information")
    
    elif student_id.isdigit()==False:
        
        ShowStudents_dict()
        print("The ID Must Be Numbers Only")
    
    elif grade.isalpha()==True:
        
        ShowStudents_dict()
        print("Grade must be numbers only.")
    
    else:

        if student_id  in students_information.keys():
            
            if course_code  in courses_information.keys() and course_code in students_information[student_id]["Courses"]:
                
                if student_id not in students_grades:
                    
                    students_grades[student_id]={}
                
                if student_id  in students_grades :
                        ReadCsv()
                        students_grades[student_id][course_code] = grade
                        Writecsv(students_grades)
                        ShowStudents_dict()
                        print(f"Grade {grade} for course {course_code} has been added for student {student_id}.")
                        
            else:
                ShowStudents_dict()
                print('No such course exist or This course already exists or Course didnt append to the Student ')
        
        else:
            ShowStudents_dict()
            print("this ID didn't found")  
         
def show_student_final_result():
    sum = 0
    total_credit = 0 
    total_corses =[]
    total_grades =[]  
      
    student_id = (input("Enter the student's ID to view grades: ")).strip()
    
    if student_id.isdigit()==False:

        ShowMainPage()
        print("The ID Must Be Numbers Only")
        
    elif len(student_id)==0:
            
        ShowMainPage()
        print("There is missing information")
            
    else:
        
        ReadCoursesJson()
        ReadStudentsJson()
        ReadCsv()
        
        if student_id in students_grades.keys():
          
            for course_code , grade in students_grades[student_id].items():
                
                if int(grade) == 0:
                    return("gpa : There is no courses")
                else:
                    
                    if int(grade) >= 97: 
                        gpa = 4.00
                        
                    elif int(grade) >= 93: 
                        gpa = 4.00
                        
                    elif int(grade) >= 90: 
                        gpa = 3.70
                        
                    elif int(grade) >= 87: 
                        gpa = 3.30
                        
                    elif int(grade) >= 83: 
                        gpa = 3.00
                        
                    elif int(grade) >= 80: 
                        gpa = 2.70
                        
                    elif int(grade) >= 77: 
                        gpa = (2.30)
                        
                    elif int(grade) >= 73: 
                        gpa = (2.00)
                        
                    elif int(grade) >= 70: 
                        gpa = (1.70)
                        
                    elif int(grade) >= 67: 
                        gpa = (1.33)
                        
                    elif int(grade) >= 65: 
                        gpa = (1.00)
                        
                        
                    elif int(grade) >= 0: 
                        gpa = (0.00)
                        
                    else:
                        print("Invalid Grade Entered")
                        
                prodect = float(gpa * int(courses_information[course_code]["Credit Hours"]))

                total_credit += int(courses_information[course_code]["Credit Hours"])
                
                sum += prodect
                
                    

            Gpa = sum / total_credit
            

        else:

            ShowMainPage()
            print(f"No grades found for student {student_id}.")      
            
        if student_id in students_grades and student_id in students_information:
                
                print(f"\nFinal results for student ID {student_id}: {students_information[student_id]}\n")
            
                for course_code, grade in students_grades[student_id].items():
                    print(f"Course Code: {course_code}, Grade: {grade}")
                
                print("-" * 40)

                print(f"Gpa : {Gpa}")
                

                PrintHtml(f"Final results for student ID {student_id}: {students_information[student_id]}",f"Gpa : {Gpa}",students_grades[student_id])
                
                
                def bar_chart():
                    
                    for course in students_grades[student_id].keys():
                        
                        if course not in total_corses:
                            
                            total_corses.append(course)    
                    
                    for grade in students_grades[student_id].values():
                        
                        if grade not in total_grades:
                            
                            total_grades.append(int(grade))
                    
                    plt.bar(total_corses,total_grades)
                    plt.show()
                bar_chart()

MainPage()