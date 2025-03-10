from Data.database import get_db_connection
from Entity.student import Student

class StudentRepository:
    def __init__(self):
        self.conn = get_db_connection()
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS Student (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            department TEXT NOT NULL
        )"""
        self.conn.cursor().execute(query)
        self.conn.commit()

    def add_student(self, student: Student):
        # self.create_table()
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Student (name, phone, department) VALUES (?, ?, ?)",
                       (student.name, student.phone, student.department))
        self.conn.commit()
        return cursor.lastrowid

    def get_all_students(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Student")
        students = cursor.fetchall()
        return [Student(*student) for student in students]

    def update_student_phone(self, student_id: int, new_phone: str):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE Student SET phone = ? WHERE student_id = ?", (new_phone, student_id))
        self.conn.commit()
        return cursor.rowcount > 0

    def delete_student(self, student_id: int):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Student WHERE student_id = ?", (student_id,))
        self.conn.commit()
        return cursor.rowcount > 0
