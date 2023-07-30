# online & offline translation using machine learning with gui
from pydub.playback import play
import os
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import translator


# gui
# Function to handle user input and display responses
def send_message(user_message):
    display_text("|", user_message, "user")
    entry.delete(0, tk.END)


def input_type(input_text):
    if input_text == "1":
        online()
    elif input_text == "2":
        offline()


def online():
    display_text("bot: ", "Enter texts to translate.", "bot")
    user_input_text = entry.get()
    display_text("|", user_input_text, "user")
    display_text("bot: ", "Enter the language to convert", "bot")
    lang = entry.get()
    translation = translator.Translator(user_input_text, lang)
    translation = translation.translate_online(user_input_text, lang)
    audio = translation.text_to_speech(translation, lang)
    play(audio)
    print(translation)


def offline():
    display_text("bot: ", "Enter texts to translate.", "bot")
    user_input_text = entry.get()
    display_text("|", user_input_text, "user")
    display_text("bot: ", "Enter the language to convert", "bot")
    lang = entry.get()
    translation = translator.Translator(user_input_text, lang)
    translation = translation.translate_offline(user_input_text, lang)
    audio = translation.text_to_speech(translation, lang)
    play(audio)
    print(translation)


# Function to display messages in the chat box
def display_text(sender, text, tag):
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, sender, tag)
    chat_box.insert(tk.END, text + "\n")
    chat_box.config(state=tk.DISABLED)


# Create the main Tkinter window
root = tk.Tk()
root.title("Translation Bot")

# Create a card-like frame for the chat box
chat_frame = ttk.Frame(root, padding=10, relief=tk.RAISED, borderwidth=2)
chat_frame.pack(fill=tk.BOTH, expand=True)

# Create a chat box to display messages
chat_box = tk.Text(chat_frame, width=50, height=15, wrap=tk.WORD, state=tk.DISABLED)
chat_box.pack(fill=tk.BOTH, expand=True)

# Configure tags for user and bot messages
chat_box.tag_config("user", justify='right', foreground='blue')
chat_box.tag_config("bot", justify='left', foreground='green')

# Create a separator to separate the chat box area from the user input area
separator = ttk.Separator(root, orient=tk.HORIZONTAL)
separator.pack(fill=tk.X, padx=10, pady=5)

# Create an entry widget for user input
entry = ttk.Entry(root, width=40)
entry.pack(padx=10, pady=5, side=tk.LEFT, fill=tk.X, expand=True)

# Bind the Enter key press to the send_message function

# Create a "Send" button with an arrow label
send_button_style = ttk.Style()
send_button_style.configure("Custom.TButton", font=("Helvetica", 14), padding=10)
display_text("bot: ", "Welcome", "bot")
display_text("bot: ", "select translation mode", "bot")
display_text("bot: ", "1. online translation", "bot")
display_text("bot: ", "2. offline translation", "bot")
user_input_text = entry.get()
input_type(user_input_text)

if type == "1":
    online()
elif type == "2":
    offline()
entry.bind("<Return>", send_message(user_input_text))
send_button = ttk.Button(root, text="➡", command=send_message(user_message=user_input_text), style="Custom.TButton")
send_button.pack(padx=10, pady=5, side=tk.LEFT)



# Start the Tkinter event loop
root.mainloop()

