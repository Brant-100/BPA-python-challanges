class student:
    def __init__(self, student_name, student_grade): 
        self.student_name = student_name
        self.student_grade = student_grade
    def is_passing(self):
        if self.student_grade <= 60:
            print("true")
        else:
            print("false")
    

p1 = student("mathew", 90)
p2 = student("john", 60)
print(p1.student_name), p1.is_passing()
#mathew
print(p2.student_name), p2.is_passing()
#john