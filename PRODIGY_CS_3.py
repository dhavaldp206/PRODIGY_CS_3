import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    length_error = len(password) < 8
    upper_error = not any(char.isupper() for char in password)
    lower_error = not any(char.islower() for char in password)
    digit_error = not any(char.isdigit() for char in password)
    special_error = not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?~' for char in password)

    errors = [length_error, upper_error, lower_error, digit_error, special_error]
    error_count = sum(errors)

    if error_count == 0:
        return "Strong password"
    elif error_count <= 2:
        return "Medium strength password"
    else:
        return "Weak password"

def check_strength():
    password = password_entry.get()
    strength = check_password_strength(password)
    messagebox.showinfo("Password Strength", strength)

# Create main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")
root.configure(bg="black")

# Create password label and entry
password_label = tk.Label(root, text="Enter Password:", fg="green", bg="black", font=("Courier", 12))
password_label.pack()
password_entry = tk.Entry(root, show="", font=("Courier", 12))
password_entry.pack()

# Create button to check strength
check_button = tk.Button(root, text="Check Strength", command=check_strength, fg="green", bg="black", font=("Courier", 12))
check_button.pack()

# Run the main loop
root.mainloop()
