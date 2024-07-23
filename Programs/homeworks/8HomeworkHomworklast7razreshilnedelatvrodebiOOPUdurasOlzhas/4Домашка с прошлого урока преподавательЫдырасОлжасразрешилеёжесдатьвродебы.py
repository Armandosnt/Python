class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Имя: {self.name}\nВозраст: {self.age}"
    
class Professor(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.professor_id = id
        self.courses = []

    def __str__(self):
        courses = "Список курсов: " + " ".join(self.courses)
        return super().__str__() + f"\nНомер профессора: {self.professor_id}\n{courses}"
    
    def add_course(self, course):
        course.set_professor(self)
        self.courses.append(course)

class Student(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.student_id = id
        self.courses = []

    def __str__(self):
        courses = "Список курсов: " + " ".join(self.courses)
        return super().__str__() + f"\nНомер студента: {self.student_id}\n{courses}"
    
    def enroll(self, course):
        course.add_student(self)
        self.courses.append(course)

class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.students = []
        self.professor = None

    def add_student(self, student):
        self.students.append(student)

    def set_professor(self, professor):
        self.professor = professor

    def __str__(self):
        students = ""
        for stud in self.students:
            students += " " + stud.name
        return f"""
Название курса: {self.course_name}
Номер курса: {self.course_code}
Препод: {self.professor}
Список студентов: {students}
"""

student = Student("Алишер", 22, "D111")
student1 = Student("Бекжан", 33, "D234")
student2 = Student("Сания", 44, "D345")

professor = Professor("Джеки Чан", 99, "P666")
    
math = Course("Матемаика", "MAT(123)")

math.add_student(student)
math.add_student(student1)
math.add_student(student2)

math.set_professor(professor)

print(math)
