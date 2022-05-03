from cProfile import label
from sqlite3 import Row
from textwrap import fill
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TIMER_TITLE = 'POMODORO'
timer = None
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
  window.after_cancel(timer)
  global reps
  reps = 0
  check_marks.config(text="")
  title_label.config(text='POMODORO', fg=GREEN)
  canvas.itemconfig(time_text, text='00:00')

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
  global reps

  reps += 1

  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN * 60

  if reps % 8 == 0:
    title_label.config(text='BREAK', fg=RED)
    countdown(long_break_sec)
  elif reps % 2 == 0:
    title_label.config(text='BREAK', fg=PINK)
    countdown(short_break_sec)
  else:
    title_label.config(text='WORK', fg=GREEN)
    countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
  global timer
  global reps
  min_count = math.floor(count / 60)
  sec_count = count % 60
  if sec_count < 10:
    sec_count = f'0{sec_count}'

  canvas.itemconfig(time_text, text=f'{min_count}:{sec_count}')
  if count > 0:
    timer = window.after(1000, countdown, count - 1)
  else:
    start_timer()
    marks = ""
    for _ in range(math.floor(reps/2)):
      marks += "✔"
      check_marks.config(text=marks);

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text=TIMER_TITLE, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tkinter_pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="START", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="RESET", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
