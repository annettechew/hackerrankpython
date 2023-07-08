N = int(input()) #no of students
from collections import namedtuple 
columns = namedtuple('columns', input().split()) 
marks = 0
for i in range(N):
    stuinfo = input().split()
    stu = columns(*stuinfo)
    marks += int(stu.MARKS)
    
print(marks/N)
