from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    pass

def start_timer():
    count_down(5)
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- count_down MECHANISM ------------------------------- # 
def count_down(count):
    canvas.itemconfig(timer_text, text=f"{count}")
    if count > 0:
        window.after(1000, count_down(count - 1))
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=60, pady=50, bg=YELLOW)

# draw an image and text over it.
timer_label = Label(text="Timer",fg="dark green",font=(FONT_NAME,30, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112,image=tomato_img) # 100 & 112 are - x & y of the center of the image/ canvas
                                               # 101, because of padding
timer_text = canvas.create_text(100, 124, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# start_timer()
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=start_timer)
reset_button.grid(column=2, row=2)

checkmarks_label = Label(text="✔", fg=GREEN)
checkmarks_label.grid(column=1, row=3)


window.mainloop()