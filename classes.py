class students:
    name=""
    age=""

    def display(self,x,y):
        students.name=x
        students.age=y
        print(students.name)
        print(students.age)

s=students()        
s.display("Adarsh Rajesh",18)