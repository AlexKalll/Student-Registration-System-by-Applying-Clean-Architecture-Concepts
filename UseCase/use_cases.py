from Entity.student import Student

class StudentUseCase:
    def __init__(self, repository):
        self.repository = repository  # Dependency Injection

    def register_student(self, name: str, phone: str, department: str):
        student = Student(None, name, phone, department)
        return self.repository.add_student(student)

    def get_students(self):
        return self.repository.get_all_students()

    def update_student(self, student_id: int, new_phone: str):
        return self.repository.update_student_phone(student_id, new_phone)

    def delete_student(self, student_id: int):
        return self.repository.delete_student(student_id)
