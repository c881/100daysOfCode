from tkinter import *


#Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=130)
window.config(pady=50, padx=50)

label_isequal = Label(text="is equal to")
label_isequal.grid(column=0, row=2)
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=1)
label_km = Label(text="Km")
label_km.grid(column=2, row=2)
miles_entry = Entry()

miles_entry.grid(column=1, row=1)
miles_entry.config(width=10)
label_km_result = Label(width=10)
label_km_result.grid(column=1, row=2)

def calc_km():
    miles = miles_entry.get()
    label_km_result["text"] = round(float(miles) * 1.6, 2)

calculate = Button(text="Calculate",command=calc_km)
calculate.grid(column=1, row=3)





window.mainloop()
