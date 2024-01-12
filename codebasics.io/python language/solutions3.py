
#18

class Teacher:
    def __init__(self, id):
        self.id = id
    
    def teacher_action(self):
        print("I teach")
    
    def common(self):
        print("I am a common teacher.")
        print("My id is", self.id)

    def tchr_id(self):
        print("I am a teacher, and my student id is", self.id)

class Student:
    def __init__(self, id):
        self.id = id

    def student_action(self):
        print("I learn.")
    
    def common(self):
        print("I am a common student.")
        print("My id is", self.id)

    def stdnt_id(self):
        print("I am a student, and my student id is", self.id)

class Person(Teacher, Student):
    def __init__(self, name, id):
        self.name = name
        super().__init__(id)


person1 = Person("Aftab", 1234)
print(person1.id, person1.name)     

person1.common()
person1.stdnt_id()
person1.tchr_id()