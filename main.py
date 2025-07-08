import tkinter as tk
from tkinter import messagebox
from db_config import get_connection

root = tk.Tk()
root.title("Student Management System")
root.geometry("400x600")

# --- Name Input ---
tk.Label(root, text="Enter Student Name:").pack(pady=10)
entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=5)

# --- Age Input ---
tk.Label(root, text="Enter Student Age:").pack(pady=10)
entry_age = tk.Entry(root, width=30)
entry_age.pack(pady=5)

# --- Marks Input ---
tk.Label(root, text="Enter Student Marks:").pack(pady=10)
entry_marks = tk.Entry(root, width=30)
entry_marks.pack(pady=5)

# --- Submit Function ---
def submit_data():
    name = entry_name.get()
    age = entry_age.get()
    marks = entry_marks.get()
    
    if name and age and marks:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "INSERT INTO studentsdata (name, age, marks) VALUES (%s, %s, %s)"
            values = (name, int(age), float(marks))
            cursor.execute(query, values)
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Data submitted successfully")
            
            # Clear fields
            entry_name.delete(0, tk.END)
            entry_age.delete(0, tk.END)
            entry_marks.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields")

# --- Submit Button ---
tk.Button(root, text="Submit", command=submit_data).pack(pady=20)
# --- Listbox to Display Students ---

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

def view_students():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM studentsdata")
        rows= cursor.fetchall()
        conn.close()
        listbox.delete(0, tk.END)  
        if rows:
            for row in rows:
                listbox.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Marks: {row[3]}")
        else:
            listbox.insert(tk.END, "No data found")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
# --- View Students Button ---

tk.Button(root, text="View Students", command=view_students).pack(pady=10)

# --- Delete by ID ---
tk.Label(root, text="Enter ID to Delete:").pack(pady=5)
entry_delete = tk.Entry(root, width=20)
entry_delete.pack(pady=5)

def delete_student():
    student_id = entry_delete.get()
    
    if student_id:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM studentsdata WHERE id = %s", (student_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Deleted", f"Student with ID {student_id} has been deleted.")
            entry_delete.delete(0, tk.END)
            view_students()  # Refresh the list after deletion
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Input Error", "Please enter a student ID.")
# --- Delete Button ---
tk.Button(root, text="Delete Student", command=delete_student).pack(pady=10)
# --- Clear All Students Button ---
def clear_all_students():
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete ALL students?")
    
    if confirm:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM studentsdata")  # ⚠️ Be careful, this deletes ALL
            conn.commit()
            conn.close()
            messagebox.showinfo("Cleared", "All student records deleted.")
            view_students()  # Refresh listbox
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
# --- Clear All Students Button ---
tk.Button(root, text="Clear All Students",command=clear_all_students).pack(pady=10) 
root.mainloop()


