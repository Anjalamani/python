class student():
    def __init__(self):
        self.name="name"
        self.grade="grade"
    def display(self):
        print("NAME",self.name)
        print("GRADE",self.grade)
s1=student()
s2=student()
s3=student()
s1.name="abi"
s2.name="anu"
s3.name="anju"
s1.grade="A"
s2.grade="A+"
s3.grade="B"
s1.display()
s2.display()
s3.display()
