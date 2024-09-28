import tkinter as tk
from tkinter import scrolledtext

window = tk.Tk()
window.title("Chatbot GUI")
window.geometry("500x500")
window.configure(bg="#222222")

# Create chat box
chat_box = scrolledtext.ScrolledText(window, width=60, height=20, font=("Arial", 12), bg="#111111", fg="white")
chat_box.configure(state='disabled')
chat_box.pack(padx=10, pady=10)

# Create input box
input_box = tk.Entry(window, width=50, font=("Arial", 12))
input_box.pack(padx=10, pady=10)

# Define chatbot response function
def respond(sender):
    message = input_box.get()
    input_box.delete(0, 'end')
    chat_box.configure(state='normal')
    chat_box.insert('end', f"{sender}: {message}\n")
    if sender == "You":
        chat_box.insert('end', "Chatbot: Hello! How can I help you?\n")
    else:
        chat_box.insert('end', "You: Thank you for your response.\n")
    chat_box.see('end')
    chat_box.configure(state='disabled')

# Create send button for user input
user_send_button = tk.Button(window, text="Send", font=("Arial", 12), bg="blue", fg="white", command=lambda: respond("You"))
user_send_button.pack(pady=10, side=tk.RIGHT)

# Create send button for chatbot response
chatbot_send_button = tk.Button(window, text="Send", font=("Arial", 12), bg="green", fg="white", state='disabled', command=lambda: respond("Chatbot"))
chatbot_send_button.pack(pady=10, side=tk.LEFT)

# Enable chatbot send button after a delay
def enable_chatbot_send_button():
    chatbot_send_button.configure(state='normal')
enable_chatbot_send_button_id = window.after(3000, enable_chatbot_send_button)

# Cancel chatbot send button enablement if user sends message manually
def cancel_enable_chatbot_send_button():
    window.after_cancel(enable_chatbot_send_button_id)
    chatbot_send_button.configure(state='disabled')
input_box.bind("<Key>", lambda event: cancel_enable_chatbot_send_button())

window.mainloop()
