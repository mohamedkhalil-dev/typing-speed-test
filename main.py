from tkinter import *
import random

random_words = ['retirement', 'dinner', 'board', 'flood', 'iron', 'ask', 'heavy', 'like', 'parallel', 'medicine'
    , 'helmet', 'mist', 'inject', 'frequency', 'glove', 'responsibility', 'elapse', 'stroke', 'background'
    , 'joy', 'romantic', 'spoil', 'cower', 'reflection', 'trustee', 'stand', 'sister', 'bench', 'symbol'
    , 'ring']


def next_word(*kwargs):
    global current_word
    if remaining_time != 0:
        current_word = random.choice(random_words)
        words_label.config(text=f"{current_word}")
        entry.delete(0, 'end')


def count_down(count):
    global remaining_time
    if count >= 0:
        window.after(1000, count_down, count - 1)
        timer_label.config(text=f"{count}")
    elif count < 0:
        remaining_time = 0
        result = Label(text=f"Test finished\nyour typing speed is: {score} words/min", font=('helvetica', 17), fg='red')
        result.pack()


def start_timer():
    next_word()
    count_down(60)


def check_word(*kwargs):
    global score, current_word, remaining_time

    user_input = (entry.get()).lstrip()
    print(f"current word: {current_word}, input:{user_input}")

    if (user_input.lower()) == current_word.lower() and remaining_time != 0:
        score += 1
        score_label.config(text=f'score: {score}')
    next_word()


def play_test():
    global remaining_time
    start_timer()
    if remaining_time != 0:
        entry.bind("<space>", check_word)
        entry.pack()


current_word = ""
score = 0
remaining_time = None

window = Tk()
window.title("Typing speed test")
window.geometry('800x600')
my_font = ('helvetica', 25, 'bold')
main_label = Label(text='welcome to Typing speed test', width=40, pady=2, font=my_font)
main_label.pack()

score_label = Label(text=f'score: {score}', width=50, font=my_font)
score_label.pack()
start_buttun = Button(text="start Test", command=play_test, font=my_font)
start_buttun.pack()

timer_label = Label(text='60', width=5, background='yellow', font=my_font)
timer_label.pack()
words_label = Label(text="press start to begin your test", width=30, height=5, font=my_font, fg="green")
words_label.pack()
note_label = Label(text='type space to show next word')
note_label.pack()
entry = Entry(width=20, font=my_font)
entry.pack()

window.mainloop()
