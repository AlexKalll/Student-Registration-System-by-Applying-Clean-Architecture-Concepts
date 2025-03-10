

# Student Registration System 
### (Applying Clean Architecture Concepts)

A simple **Student Registration System** built using **Python** and **SQLite**, following the **Clean Architecture** principles.

---
## 🏛️ Clean Architecture Overview
| **Layer**                  | **Role** |
|----------------------------|---------|
| **Entity (Domain Layer)**   | Defines the `Student` entity. |
| **UseCase (Application Layer)** | Handles business logic (e.g., student registration, updates). |
| **Interface (Presentation Layer)** | CLI-based interface for user interaction. |
| **Data (Infrastructure Layer)** | Handles SQLite database operations using the Repository Pattern. |

- Generally, Clean Architecture is a software design philosophy that separates the structure of an application into distinct layers, promoting independence and making the system easier to maintain, test, and scale.
---

## 🚀Project Features
✅ Register new students  
✅ View all registered students  
✅ Update student details  
✅ Delete students  
✅ Command-line interface (CLI)  
✅ SQLite database integration  

---

## 📂 Project Structure  

```
/<Root Directory>
│── /Entity               # Domain Layer (Core Business Rules)
│    ├── student.py
│── /UseCase              # Application Layer (Business Logic)
│    ├── use_cases.py
│── /Interface            # Presentation Layer (User Interface)
│    ├── cli.py           # CLI Interaction
│── /Data                 # Infrastructure Layer (Database)
│    ├── database.py      # Database connection establishment
│    ├── student_repo.py  # Data Access
│── /Tests                # Unit Tests
│    ├── tests.py
│── main.py               # Entry Point
│── README.md             # project Documentation
│── .gitignore            # Hide some cache, secret files and keys
```

---

## 🔨 Technologies Used
- **Python 3**
- **SQLite (Relational Database)**
- **Clean Architecture Design Pattern**
- **unittest (For Testing)**

---

## 🎯 How to Run the Project

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/yourusername/student-registration.git
cd student-registration
```

### 2️⃣ Install Dependencies  
This project uses **only built-in Python libraries**, so no extra dependencies are required.

### 3️⃣ Run the Application  
```bash
python main.py
```

---

## 🧪 Running Tests  
To ensure everything is working correctly, run the unit tests:

```bash
python -m unittest Tests/test.py
```
---

## 📸 Demo
📍 **Registering a Student**
```
--- Student Registration System ---
1. Register Student
2. View Students
3. Update Student Phone
4. Delete Student
5. Exit
Enter your choice: 1
Enter student name: Eyob Deresse 
Enter student phone: 1234567890
Enter student department: Computer Science
Student registered with ID: 1
```

📍 **Viewing All Students**
```
Registered Students:
1: John Abebe | 1234567890 | Computer Science
```

📍 **Updating a Student's Phone**
```
Enter student ID: 1
Enter new phone number: 9876543210
Updated successfully!
```

📍 **Deleting a Student**
```
Enter student ID to delete: 1
Deleted successfully!
```
📍 **Testing**
```bash
python -m unittest Tests/test.py
```
Output
```bash
....
----------------------------------------------------------------------
Ran 4 tests in 1.496s

OK
```
---

## 📌 Contributing
Contributions are welcome! If you'd like to improve this project, feel free to fork the repository and submit a pull request.  

---
### Contact me
[LinkedIn](https://www.linkedin.com/in/kaletsidik-ayalew-mekonnen-34772226b/) | [Instagram](https://www.instagram.com/kaletsidik.24?igsh=YzljYTk1ODg3Zg==) | [X~Twitter](https://x.com/kaletsidike?t=VCe79O084EmE9bM2V5jOIA&s=09) | [Telegram](https://t.me/Adragon_de_mello) | [GitHub](https://github.com/AlexKalll) | [LeetCode](https://leetcode.com/Alexkal/)


Kaletsidik Ayalew
alexkalalw@gmail.com

