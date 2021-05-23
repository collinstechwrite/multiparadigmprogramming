"""
For this assessment you are asked to build a GPA calculator for students in a fictional university.
You will be supplied a CSV file with names and the grades they have achieved in various modules (CTASample.csv).
This will be used to calculate GPA. You should add additional data to this CSV for the purposes of testing.
You will need to convert the percentage grade (i.e. a grade out of 100%) given in the CSV to a letter grade and
it’s corresponding value on the GPA scale.
The GPA scale should run from 4.2 down with + and - grades. Each module has equal weighting for GPA calculation.
An A+ is worth 4.2, an A 4, and A- 3.8 and so on down to F. You can decide what corresponds to an A+ for example
you could choose greater than 90%. There should also be a live mode where the user can enter a set of marks and modules
from the command line and have the program calculate the GPA.
The final output of the program should show the GPA of each student, their highest scoring module, their lowest scoring module,
standard deviation, median value, how far from the next highest GPA they were (if not at 4.2), and the letter grade of each module
result.


# https://iadt.ie/for-students/exams-assessments/grade-point-average-gpa
To calculate your GPA: First take the grade you received in each module and multiply it by the number of credits assigned to that module.
This gives you the number of grade points earned for each module. Add up all the grade points you have earned for and divide that by the number of credits.



https://pages.collegeboard.org/how-to-convert-gpa-4.0-scale



Letter Grade

 

Percent Grade

 

4.0 Scale

 

A+

97-100

4.0

A

93-96

4.0

A-

90-92

3.7

B+

87-89

3.3

B

83-86

3.0

B-

80-82

2.7

C+

77-79

2.3

C

73-76

2.0

C-

70-72

1.7

D+

67-69

1.3

D

65-66

1.0

E/F

Below 65

0.0




"""


import csv
 
with open('CTASample.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(type(row))
        print(row)

