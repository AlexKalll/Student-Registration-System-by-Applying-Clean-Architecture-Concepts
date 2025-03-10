from Data.student_repo import StudentRepository
from UseCase.use_cases import StudentUseCase

class StudentCLI:
    def __init__(self):
        self.repo = StudentRepository()
        self.use_case = StudentUseCase(self.repo)

    def run(self):
        while True:
            print("\n--- Student Registration System ---")
            print("1. Register Student")
            print("2. View Students")
            print("3. Update Student Phone")
            print("4. Delete Student")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter student name: ")
                phone = input("Enter student phone: ")
                department = input("Enter student department: ")
                student_id = self.use_case.register_student(name, phone, department)
                print(f"Student registered with ID: {student_id}")

            elif choice == "2":
                students = self.use_case.get_students()
                if students:
                    print("\nRegistered Students:")
                    for student in students:
                        print(student)
                else:
                    print("No students found!")

            elif choice == "3":
                student_id = int(input("Enter student ID: "))
                new_phone = input("Enter new phone number: ")
                success = self.use_case.update_student(student_id, new_phone)
                print("Updated successfully!" if success else "Student not found!")

            elif choice == "4":
                student_id = int(input("Enter student ID to delete: "))
                success = self.use_case.delete_student(student_id)
                print("Deleted successfully!" if success else "Student not found!")

            elif choice == "5":
                print("Exiting...")
                break

            else:
                print("Invalid choice! Please try again.")
