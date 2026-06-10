class Student():
    def __init__(self,name,age,city,grade):
        self.name = name
        self.age = age
        self.city = city
        self.grade = grade
    def print_details(self):
        print(self.name)
        print(self.age)
        print(self.city)
        print(self.grade)
    def change_details(self):
        UserInput = input ("which data you want to change?")
        if UserInput == "name" :
            self.name = input("pls add the updated name.")
        elif UserInput == "age" :
            self.age = input("pls add the updated age.")
        elif UserInput == "city" :
            self.city = input("pls add the updated city.")    
        elif UserInput == "grade" :
            self.grade = input("pls add the updated grade.")
s1 = Student("ian","12","Netherlands","A")
s1.print_details()
s1.change_details()

s1.print_details()

