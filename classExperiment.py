#https://www.geeksforgeeks.org/how-to-get-column-names-in-pandas-dataframe/

# Import pandas package 
import pandas as pd 
    
# making data frame 
data = pd.read_csv("CTASample.csv") 


#list of courses e.g. top column of spreadsheet
list_of_courses = []

#iterating the columns
for col in data.columns:

    #https://www.journaldev.com/33182/python-add-to-list
    list_of_courses.append(col)


#https://stackoverflow.com/questions/4426663/how-to-remove-the-first-item-from-a-list
list_of_courses.pop(0)

#list of students e.g. each index column of spreadsheet
list_of_students = []


#https://stackoverflow.com/questions/39662891/read-in-the-first-column-of-a-csv-in-python
with open("CTASample.csv") as f:
    for row in f:
        list_of_students.append(row.split()[0])


list_of_students.pop(0)


# https://pythonspot.com/inner-classes/
#creating outer class to contain Course, as potentially university may want to add more courses




class Student:
    def __init__(self,StudentName,StudentCourse):
        self.StudentName = StudentName
        self.StudentCourse = StudentCourse



class Course:
    def __init__(self,NameOfCourse,Subjects,Students):
        self.NameOfCourse = NameOfCourse
        self.Subjects = Subjects
        self.Students = Students
        self.head = self.Head()
    
    class Head:
        def talk(self):
            return 'talking...'
            

if __name__ == '__main__':
    coursename = "ComputerScience"
    z1 = Course(coursename,list_of_courses,list_of_students)
    print (z1.NameOfCourse)
    print (z1.Subjects)
    print(z1.Students)
    print (z1.head.talk())


for item in list_of_students:
    #use code here to create a class for each student, which contains student name and course
    print(item)
    Student(str(item),str(z1.NameOfCourse))


print(Peter.StudentName)
print(Peter.StudentCourse)


