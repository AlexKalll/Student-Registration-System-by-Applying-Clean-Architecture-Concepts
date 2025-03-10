class Student:
    def __init__(self, student_id: int = None, name: str = "", phone: str = "", department: str = ""):
        self.student_id = student_id
        self.name = name
        self.phone = phone
        self.department = department

    def __str__(self):
        return f"{self.student_id}: {self.name} | {self.phone} | {self.department}"
