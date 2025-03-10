import unittest
from Data.database import get_db_connection
from Data.student_repo import StudentRepository
from UseCase.use_cases import StudentUseCase

class TestStudentRegistration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # set up a temporary test database before running the tests. 
        cls.repo = StudentRepository()
        cls.use_case = StudentUseCase(cls.repo)
        cls.repo.conn = get_db_connection()

    def test_1_register_student(self):
        # test registration. 
        student_id = self.use_case.register_student("Alice Johnson", "1234567890", "Computer Science")
        self.assertIsInstance(student_id, int)
        students = self.use_case.get_students()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].name, "Alice Johnson")

    def test_2_get_students(self):
        #  Test fetching all registered students. 
        students = self.use_case.get_students()
        self.assertGreater(len(students), 0)  # at least one student should exist

    def test_3_update_student_phone(self):
        # Test updating a student's phone number. 
        students = self.use_case.get_students()
        student_id = students[0].student_id
        updated = self.use_case.update_student(student_id, "0987654321")
        self.assertTrue(updated)
        updated_students = self.use_case.get_students()
        self.assertEqual(updated_students[0].phone, "0987654321")

    def test_4_delete_student(self):
        # Test deleting a student. 
        students = self.use_case.get_students()
        student_id = students[0].student_id
        deleted = self.use_case.delete_student(student_id)
        self.assertTrue(deleted)
        remaining_students = self.use_case.get_students()
        self.assertLess(len(remaining_students), 20) # since I saved 20 students in the database

if __name__ == "__main__":
    unittest.main()
