import requests
import tkinter as tk
import time
from functools import partial


def generate_words():
    word_data = requests.get("https://random-word-api.herokuapp.com/word?number=10&length=5")
    words_list = word_data.json()
    words_str = ", ".join(words_list)
    return words_str


def start_typing(time_start):
    entry.bind('<Return>', partial(check_typing, time_start))


def check_typing(time_start, event=None):
    time_end = time.time()
    typed_text = entry.get()
    if typed_text == words_to_type["text"]:
        time_taken = time_end - time_start
        typing_speed = len(words_to_type["text"].split(", ")) / (time_taken / 60)
        result.config(text=f"Typing speed: {typing_speed:.2f} CPM")
    else:
        result.config(text="Incorrect typing, try again.")
    entry.delete(0, 'end')
    entry.unbind('<Return>')
    submit_b.focus_set()


def update_words():
    words_to_type.config(text=generate_words())


window = tk.Tk()
window.title('Typing speed test')
window.minsize(500, 200)
window.maxsize(500, 200)

hi_label = tk.Label(window, text="Enter these words:")
hi_label.pack()

words = generate_words()
words_to_type = tk.Label(window, text=words)
words_to_type.pack()

entry = tk.Entry(window, width=55)
entry.pack()

submit_b = tk.Button(window, text='Start', command=lambda: start_typing(time.time()))
submit_b.pack()

result = tk.Label(window, text="")
result.pack()

update_words_button = tk.Button(window, text="Generate New Words", command=update_words)
update_words_button.pack()

what_to_do = tk.Label(window, text='1) Press start button\n2) Enter text\n3) Press Enter')
what_to_do.pack()
window.mainloop()
