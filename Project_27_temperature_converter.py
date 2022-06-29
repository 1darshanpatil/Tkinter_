import tkinter as tk

def act1(C):
    print(9*C/5 + 32)

window = tk.Tk()
window.title('Temperature Converted')
window.minsize(width = 300, height = 80)
window.config(padx = 100, pady = 20)

def converter():
    if ent_0.get() == "" and ent_1.get() != "":
        F = float(ent_1.get())
        C = round((F - 32)*5/9, 2)
        ent_0.insert(tk.END, string = f"{C}")
    elif ent_1.get() == "" and ent_0.get() != "":
        C = float(ent_0.get())
        F = round(9*C/5 + 32, 2)
        ent_1.insert(tk.END, string = f"{F}")
    elif ent_1.get() != "" and ent_0.get() != "":
        ent_0.delete(0, tk.END)
        ent_1.delete(0, tk.END)

    
#Entry
ent_0 = tk.Entry(width =  10,
               bd = 5)
ent_0.grid(row = 0, column = 0)

#Creating a label
lbl = tk.Label(text = 'celsius: ', font = 'bold')
lbl.grid(row = 1, column = 0)


#button
btn = tk.Button(text = "=",
                width = 5,
                command = converter)
btn.grid(row = 0, column = 1)

#Entry
ent_1 = tk.Entry(width =  10,
               bd = 5)
ent_1.grid(row = 0, column = 2)


#Creating a label
lbl_1 = tk.Label(text = 'Fahrenheit', font = 'bold')
lbl_1.grid(row = 1, column = 2)

window.mainloop()
