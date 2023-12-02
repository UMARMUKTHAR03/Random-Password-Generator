import random
import string
import tkinter as tk


def generate_password():
    length = length_entry.get()
    if not length:
        length = 12
    else:
        length = int(length)

    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        password_entry.delete(0, tk.END)
        password_entry.insert(tk.END, "Please select at least one character set.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)


window = tk.Tk()
window.title("Random Password Generator")

window.configure(bg="#f2f2f2")

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(4, weight=1)

length_label = tk.Label(window, text="Password Length :", bg="#f2f2f2")
length_label.grid(row=0, column=0, padx=50, pady=10, sticky="w")
length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1, padx=35, pady=0, sticky="ew")
length_entry.insert(0, "12")
lowercase_var = tk.BooleanVar()
lowercase_checkbox = tk.Checkbutton(window, text="Lowercase", variable=lowercase_var, bg="#f2f2f2")
lowercase_checkbox.grid(row=1, column=0, padx=25, pady=10, sticky="w")

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(window, text="Uppercase", variable=uppercase_var, bg="#f2f2f2")
uppercase_checkbox.grid(row=1, column=1, padx=25, pady=10, sticky="w")

numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(window, text="Numbers", variable=numbers_var, bg="#f2f2f2")
numbers_checkbox.grid(row=2, column=0, padx=25, pady=10, sticky="w")

symbols_var = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(window, text="Symbols", variable=symbols_var, bg="#f2f2f2")
symbols_checkbox.grid(row=2, column=1, padx=25, pady=10, sticky="w")

generate_button = tk.Button(window, text="Generate Password", command=generate_password, bg="#4caf50", fg="white",
                            width=20)
generate_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

password_entry = tk.Entry(window, width=30)
password_entry.grid(row=3, column=1, columnspan=2, padx=20, pady=0, sticky="w")

window.mainloop()
