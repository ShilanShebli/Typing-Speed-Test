import random
from tkinter import *
import datetime as dt

words = ["apple", "beach", "chair", "dance", "eagle",
         "fairy", "grape", "horse", "igloo", "jumps",
         "kite", "lemon", "mouse", "nurse", "olive",
         "umbra", "water", "xerox", "yacht", "zebra",
         "bacon", "cloud", "diver", "ember", "fungi",
         "ghost", "hotel", "insect", "jelly", "koala"]

start_time = None
first_enter_pressed = False

def start_typing(event):
    global start_time
    if start_time is None:
        start_time = dt.datetime.now()


def check_entry(event):
    global start_time, first_enter_pressed

    user_input = typing_place.get().strip()
    user_words = user_input.split()
    text_model_words = text_model.get("1.0", "end-1c").split()
    correct_user_words = sum(1 for user_word, model_word in zip(user_words, text_model_words) if user_word == model_word)

    elapsed_time = (dt.datetime.now() - start_time).total_seconds()
    words_per_minute = int(correct_user_words / (elapsed_time/60))
    print(f"Elapsed time: {elapsed_time:.2f} seconds, WPM: {words_per_minute} You typed: {correct_user_words} correct words")

    typing_place.delete(0, END)
    start_time = None
    if not first_enter_pressed:  # Check if it's the first Enter key press
        try_again_button.config(state=NORMAL)  # Enable "Try again" button
        first_enter_pressed = True

def try_again():
    # Clear the text entry field and disable the "Try again" button
    typing_place.delete(0, END)
    try_again_button.config(state=NORMAL)



window = Tk()
window.title("Test Your Typing Speed")
window.minsize(width=700, height=400)
window.config(padx=30, pady=30)

word_label = Label(text="Type the words you see as fast as you can!\nPress Enter when you're done!", font=("Arial", 16, "bold"))
word_label.grid(column=0, row=0, columnspan=3)



text_model = Text(height=5, width=50)
text_model.grid(column=0, row=1, columnspan=3, sticky="nsew")
text_model.config(padx=20, pady=20, font=("Arial", 14))
text_model.insert("1.0", words)

typing_place = Entry()
typing_place.focus()
typing_place.grid(column=0, row=2, columnspan=3)

typing_place.bind("<KeyPress>", start_typing)
typing_place.bind("<Return>", check_entry)


#create try again button
try_again_button = Button(text="Try again", command=try_again)
try_again_button.grid(column=0, row=3, columnspan=3)
try_again_button.config(state=DISABLED)



window.grid_rowconfigure(1)
window.grid_columnconfigure(0, weight=1)


window.mainloop()