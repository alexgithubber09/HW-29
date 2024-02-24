class Student:

    def __init__(self, name, age, avg):
        self.name = name
        self.age = age
        self.avg = avg


    def averageGrade(listMarks, lengthList):
        return sum(listMarks)/lengthList

    def status(averageGrade):
        if averageGrade > 3 and averageGrade < 6:
            print("троечник")
        elif averageGrade >= 6 and averageGrade < 9:
            print("хорошист")
        elif averageGrade >= 9:
            print("отличник")

Student1 = Student(name="Mike", age=18, avg=6.4)
Student2 = Student(name="John", age=21, avg=9.2)
Student3 = Student(name="Steave", age=20, avg=5.9)

print(f"Average grade is {Student.averageGrade(listMarks=[5,9,7], lengthList=3)}")

Student.status(Student1.avg)
Student.status(Student2.avg)
Student.status(Student3.avg)


