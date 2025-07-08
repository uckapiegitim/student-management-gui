# 🧑‍🎓 Student Management System (Python GUI + MySQL)

This is a full stack desktop application built using **Python (Tkinter GUI)** and **MySQL**, allowing users to manage student records with a simple and clean interface.

> Built by **Mohan Sarma (S)** as part of a full stack learning journey 💻🔥

---

## 🚀 Features

- ✅ Add Student (Name, Age, Marks)
- ✅ View All Students in List
- ✅ Delete Student by ID
- ✅ Clear All Student Records
- ✅ Auto-refresh list after any action
- ✅ Error & confirmation popups for smooth experience

---

## 🛠️ Tech Stack

- **Frontend (GUI):** Python Tkinter
- **Backend Logic:** Python Functions
- **Database:** MySQL (with `mysql-connector-python`)
- **Tooling:** VS Code + GitHub

---

## 📁 Folder Structure
Student-Management-System/
│
├── main.py # Main GUI + CRUD logic
├── db_config.py # MySQL database connection
├── README.md # Project guide
└── studentdb (MySQL DB) # Table: studentsdata (id, name, age, marks)


---

## ⚙️ How to Run the App

### 1. Install MySQL Connector (if not already):
```bash
pip install mysql-connector-python

### 2. Create the Database & Table:
Log in to your MySQL terminal and run:

sql
Copy code
CREATE DATABASE studentdb;
USE studentdb;

CREATE TABLE studentsdata (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    age INT,
    marks FLOAT
);
### 3. Update Database Credentials (in db_config.py):
python
Copy code:
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_mysql_password",
        database="studentdb"
    )

### 4. Run the App:
```bash

python main.py

