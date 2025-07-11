import tkinter as tk
import re
import random
import string

def check_strength(event=None):
    password = entry.get()
    length_ok = len(password) >= 8
    upper_ok = re.search(r'[A-Z]', password) is not None
    lower_ok = re.search(r'[a-z]', password) is not None
    digit_ok = re.search(r'\d', password) is not None
    special_ok = re.search(r'[\W_]', password) is not None

    update_label(length_label, length_ok)
    update_label(upper_label, upper_ok)
    update_label(lower_label, lower_ok)
    update_label(digit_label, digit_ok)
    update_label(special_label, special_ok)

    score = sum([length_ok, upper_ok, lower_ok, digit_ok, special_ok])

    if score == 5:
        strength = "Very Strong"
        color = "#00cc66"
        crack_time = "Centuries"
        bar_width = 300
    elif score == 4:
        strength = "Strong"
        color = "#3399ff"
        crack_time = "Months to Years"
        bar_width = 240
    elif score == 3:
        strength = "Moderate"
        color = "#ff9933"
        crack_time = "Hours to Days"
        bar_width = 180
    else:
        strength = "Weak"
        color = "#ff3333"
        crack_time = "Instant to Minutes"
        bar_width = 100

    strength_label.config(text=f"Strength: {strength}", fg=color, bg=bg_color)
    crack_time_label.config(text=f"Estimated Time to Crack: {crack_time}", fg="white", bg=bg_color)
    strength_bar.config(width=bar_width, bg=color)

def update_label(label, is_ok):
    label.config(fg="#00cc66" if is_ok else "red")

def toggle_password():
    entry.config(show="" if show_var.get() else "*")

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    strong_pass = ''.join(random.choice(characters) for _ in range(14))
    entry.delete(0, tk.END)
    entry.insert(0, strong_pass)
    check_strength()

bg_color = "#1e1e1e"
fg_color = "#ffffff"

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("480x540")
root.configure(bg=bg_color)

tk.Label(root, text="Enter your password:", font=("Arial", 12), fg=fg_color, bg=bg_color).pack(pady=10)
entry = tk.Entry(root, show="*", font=("Arial", 14), width=30, bg="#2e2e2e", fg=fg_color, insertbackground=fg_color)
entry.pack()
entry.bind("<KeyRelease>", check_strength)

show_var = tk.BooleanVar()
show_check = tk.Checkbutton(root, text="Show Password", variable=show_var, command=toggle_password, fg=fg_color, bg=bg_color, selectcolor=bg_color, activebackground=bg_color)
show_check.pack(pady=5)

tk.Label(root, text="Criteria:", font=("Arial", 12, "bold"), fg=fg_color, bg=bg_color).pack(pady=10)

length_label = tk.Label(root, text="• At least 8 characters", fg="red", bg=bg_color)
upper_label = tk.Label(root, text="• Contains uppercase letter", fg="red", bg=bg_color)
lower_label = tk.Label(root, text="• Contains lowercase letter", fg="red", bg=bg_color)
digit_label = tk.Label(root, text="• Contains a digit", fg="red", bg=bg_color)
special_label = tk.Label(root, text="• Contains a special character", fg="red", bg=bg_color)

length_label.pack(anchor="w", padx=30)
upper_label.pack(anchor="w", padx=30)
lower_label.pack(anchor="w", padx=30)
digit_label.pack(anchor="w", padx=30)
special_label.pack(anchor="w", padx=30)

strength_label = tk.Label(root, text="Strength: ", font=("Arial", 14, "bold"), bg=bg_color)
strength_label.pack(pady=10)

crack_time_label = tk.Label(root, text="Estimated Time to Crack: ", font=("Arial", 12), bg=bg_color)
crack_time_label.pack()

strength_bar = tk.Frame(root, height=10, width=100, bg="red")
strength_bar.pack(pady=10)

tk.Button(root, text="Generate Strong Password", command=generate_password, bg="#00cc66", fg="white", font=("Arial", 12), activebackground="#00aa55").pack(pady=20)

root.mainloop()
