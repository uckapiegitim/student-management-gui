# 🧑‍🎓 Student Management System (Python GUI + MySQL)

This is a full stack desktop application built using **Python (Tkinter GUI)** and **MySQL**, allowing users to manage student records with a simple and clean interface.

> Built by **Mohan Sarma** as part of a full stack learning journey 💻🔥

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
- **Tooling:** VS Code 

---

## 📁 Folder Structure

```
Student-Management-System/
├── main.py          # Main GUI + CRUD logic
├── db_config.py     # MySQL database connection
├── README.md        # Project guide
└── studentdb        # MySQL DB with table: studentsdata (id, name, age, marks)
```

---

## ⚙️ How to Run the App

### ✅ 1. Install MySQL Connector

```bash
pip install mysql-connector-python
```

---

### ✅ 2. Create the Database & Table

Log in to your MySQL terminal or MySQL Workbench and run:

```sql
CREATE DATABASE studentdb;

USE studentdb;

CREATE TABLE studentsdata (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    age INT,
    marks FLOAT
);
```

---

### ✅ 3. Update DB Credentials in `db_config.py`

```python
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_mysql_password",
        database="studentdb"
    )
```

🧠 Replace `your_mysql_password` with your actual password

---

### ✅ 4. Run the App

```bash
python main.py
```

✅ A desktop GUI will open — allowing you to manage student records easily.

---
## 📸 Screenshots

Here’s a preview of the app GUI:

![App Screenshot](sc11.png)


---

## 🙋‍♂️ Author

**Mohan Sarma**  
👨‍💻 [GitHub](https://github.com/smohansarma)  
🔗 [LinkedIn](https://www.linkedin.com/in/mohan-sarma-s-b36752252)

---

## ⭐ Like this project?

- Star the repo on GitHub 🌟
- Share with other learners
- Add it to your resume and job applications!
