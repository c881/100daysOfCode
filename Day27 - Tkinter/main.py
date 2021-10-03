import tkinter as tk

window = tk.Tk()
window.title("Hello world!")
window.minsize(width=500, height=300)

# label
my_label = tk.Label(text="hello again")
my_label.pack()

window.mainloop()
