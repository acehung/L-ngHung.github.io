class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age} tuổi)"
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        return f"{super().__str__()} - Mã sinh viên: {self.student_id}"
Student = Student("Lương Minh Hùng", 21, "23110171")
print(Student)
    