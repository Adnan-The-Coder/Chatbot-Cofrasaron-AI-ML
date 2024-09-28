import tkinter as tk

window = tk.Tk()
window.title("Sci-fi GUI")
window.geometry("500x500")
window.configure(bg="black")

# Create menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Create file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Paste")
menu_bar.add_cascade(label="Edit", menu=edit_menu)

label = tk.Label(window, text="Welcome to the Sci-fi GUI!", font=("Arial", 24), fg="white", bg="black")
label.pack(pady=50)

button = tk.Button(window, text="Click me!", font=("Arial", 18), fg="white", bg="blue")
button.pack(pady=20)

window.mainloop()
