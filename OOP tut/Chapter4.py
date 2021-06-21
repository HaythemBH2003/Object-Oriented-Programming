######## INTERACTION BETWEEN CLASSES ########

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade

    def get_name(self):
        return self.name

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = [] 
                # students -------> ATTRIBUTE
                # NOT MENTIONED IN __init__()

    def get_name(self):
        return self.name 

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            print(f"Student {student.get_name()} successfully added to the {self.get_name()} course.")
            return True
        else:
            print(f"Maximum number of students reached. Unable to add {student.get_name()} to the {self.get_name()} course.")
            return False
    
    def get_average_grade(self):
        sum = 0 
        for student in self.students:
            sum += student.get_grade()
        average = sum / len(self.students)
        return average

s1 = Student("Tim", 16, 18)
s2 = Student("Bill", 18, 15)
s3 = Student("Joe", 19, 14)

course = Course("Computer Science", 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
print(course.get_average_grade())