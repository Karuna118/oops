class student:
    college_name = "ABC College"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    @classmethod
    def change_college(cls,new_name):
        cls.college_name=new_name

    def is_pass(marks):
        if marks>=35:
            print("Pass")
        else:
            print("fail")
    def display(self):
        print("The name of the student is",self.name)
        print("The roll number of the student is",self.roll_no)
    
s1=student("Abhi","123")
s2=student("Karuna","099")

s1.display()
s2.display()

print(student.college_name)
student.change_college("XYZ College")
print(s1.college_name)

student.is_pass(40)
student.is_pass(30)