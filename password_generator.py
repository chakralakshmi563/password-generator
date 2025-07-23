import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12, use_special=True):
    if length < 4:
        return "Length must be at least 4!"

    # Base characters
    characters = string.ascii_letters + string.digits
    if use_special:
        characters += string.punctuation

    # Ensure at least one lowercase, uppercase, and digit
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation) if use_special else random.choice(string.ascii_lowercase)

    remaining = ''.join(random.choice(characters) for _ in range(length - 4))

    password_list = list(lowercase + uppercase + digit + special + remaining)
    random.shuffle(password_list)
    return ''.join(password_list)

def on_generate():
    try:
        length = int(entry_length.get())
        use_special = special_var.get()
        password = generate_password(length, use_special)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(entry_password.get())
    messagebox.showinfo("✅ Copied!", "Password copied to clipboard!")

def save_to_file():
    with open("passwords.txt", "a") as f:
        f.write(entry_password.get() + "\n")
    messagebox.showinfo("✅ Saved!", "Password saved to passwords.txt")

# GUI Setup
root = tk.Tk()
root.title("🔒 Stylish Password Generator")
root.geometry("420x300")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

title_label = tk.Label(root, text="🔐 Stylish Password Generator", font=("Arial", 16, "bold"), fg="white", bg="#1e1e2e")
title_label.pack(pady=10)

frame_top = tk.Frame(root, bg="#1e1e2e")
frame_top.pack(pady=5)

label_length = tk.Label(frame_top, text="Password Length:", font=("Arial", 12), fg="white", bg="#1e1e2e")
label_length.grid(row=0, column=0, padx=5)

entry_length = tk.Entry(frame_top, font=("Arial", 12), width=5)
entry_length.insert(0, "12")
entry_length.grid(row=0, column=1, padx=5)

special_var = tk.BooleanVar(value=True)
chk_special = tk.Checkbutton(frame_top, text="Include Special Characters", var=special_var,
                             font=("Arial", 10), fg="white", bg="#1e1e2e", selectcolor="#333")
chk_special.grid(row=0, column=2, padx=10)

btn_generate = tk.Button(root, text="🎲 Generate Password", command=on_generate, font=("Arial", 12, "bold"),
                         bg="#4caf50", fg="white", relief="flat", padx=10, pady=5)
btn_generate.pack(pady=10)

entry_password = tk.Entry(root, font=("Courier", 14), width=30, justify="center")
entry_password.pack(pady=5)

frame_buttons = tk.Frame(root, bg="#1e1e2e")
frame_buttons.pack(pady=10)

btn_copy = tk.Button(frame_buttons, text="📋 Copy", command=copy_to_clipboard, font=("Arial", 11), bg="#2196f3", fg="white", width=10)
btn_copy.grid(row=0, column=0, padx=5)

btn_save = tk.Button(frame_buttons, text="💾 Save", command=save_to_file, font=("Arial", 11), bg="#ff9800", fg="white", width=10)
btn_save.grid(row=0, column=1, padx=5)


# Auto-generate a password at startup
on_generate()

root.mainloop()
