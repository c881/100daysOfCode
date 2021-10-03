import tkinter as tk

window = tk.Tk()
window.title("Hello world!")
window.minsize(width=500, height=300)

# label
my_label = tk.Label(text="hello again")
my_label.pack()

my_label.config(text='New Label')

def button_clicked():
    my_label["text"] = user_input.get()

# Button
my_button = tk.Button(text="Click me!", command=button_clicked)
my_button.pack()

# Entry
user_input = tk.Entry(textvariable="hello there!")
user_input.pack()


window.mainloop()
