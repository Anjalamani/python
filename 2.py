# * construction
# -> A construction is a unique function that gets called automatically when an object is created of a class
# self ->  denote the object
class laptop():
    def __init__(self):
        self.ram=""
        self.process=""
    def display(self):
        print( "ram",self.ram)
        print("process" ,self.process)
hp=laptop()
dell=laptop()
hp.ram=8
dell.ram=7
hp.process=5
dell.process=9
hp.display()
dell.display()
 # The main purpose of a constructor is to initialize or assign values to the data members of that class
