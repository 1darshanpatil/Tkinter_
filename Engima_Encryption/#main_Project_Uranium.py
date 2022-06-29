import rotors
import tkinter as tk
from tkinter import HORIZONTAL
import tkinter.messagebox as mbx
import pyperclip
class Rotor():
    def __init__(self):
        pass
    def rotating(self, x, dc):
        dc_rotated = {}
        KEYS, VALUES = zip(*dc.items())
        for cnt in range(len(dc)):
            dc_rotated[KEYS[cnt]] = VALUES[(cnt - x)%len(dc)]
        return dc_rotated
    def encrypting_package(self, PIN, ROTOR_LST):
        packageE = []
        for x in range(6):
            pn = PIN[x]
            packageE.append(self.rotating(pn, ROTOR_LST[x]))
        return packageE
    def passing(self, PEL, ch):
        for x in range(6):
            try:
                ch = PEL[x][ch]
            except KeyError or TypeError:
                raise 'Please find if there is any extra in the entry.'                
        return ch
    def gkfvod(self, dc, val):
        return list(dc.keys())[list(dc.values()).index(val)]
    def unpassing(self, PEL, ch):
        for x in range(1, 7):
            ch = self.gkfvod(PEL[-x], ch)
        return ch
    def updating(self, PEL, e_or_d = 1):
        if e_or_d == 1:
            PIN = [1 for _ in range(6)]
            return self.encrypting_package(PIN, PEL)
        else:
            PIN = [-1 for _ in range(6)]
            return self.encrypting_package(PIN, PEL)
    def processE(self, PEL, password):
        passwordE = ''
        for str_ in password:
            passwordE += self.passing(PEL, str_)
            PEL = self.updating(PEL)
        return passwordE
    def processD(self, PEL, passwordE):
        password = ''
        for str_ in passwordE:
            password += self.unpassing(PEL, str_)
            PEL = self.updating(PEL)
        return password
class UI():    
    def __init__(self, window, encryption):
        self.encryption = encryption
        self.window = window
        self.window.title('Security Window')
        self.window.minsize(width = 100, height = 50)
        self.bg = tk.PhotoImage(file = "lock_.png")
        self.back_ground = tk.Label(image=self.bg, highlightthickness = 0)
        self.back_ground.place(x=0, y=0)
        self.x = tk.StringVar()
    def entry(self):
        inp = tk.Entry(self.window,width = 70, textvariable = self.x, bd = 7)
        inp.focus()
        inp.insert(tk.END, 'Enter your password')
        inp.grid(row = 0, column = 0,padx = 100, pady=100)
    def label(self):
        lebl = tk.Label(self.window, text = 'Slide the horizontal scales and set your 6-digit PIN.', fg = 'red', font=('bold', 13), highlightthickness = 0, background='black')
        lebl.grid(row = 1, column = 0, padx = 50, pady= 50)
    def scaler(self):
        self.a, self.b, self.c, self.d, self.e, self.f = tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()
        scaler1 = tk.Scale(self.window, from_ = 0, to = 9, variable = self.a, length = 200, background='#2f3c71', fg = 'red', highlightthickness = 0, width = 12)
        scaler2 = tk.Scale(self.window, from_ = 0, to = 9, variable = self.b, length = 200, background='#2f3c71', fg = 'red', highlightthickness = 0, width = 12)
        scaler3 = tk.Scale(self.window, from_ = 0, to = 9, variable = self.c, length = 200, background='#2f3c71', fg = 'red', highlightthickness = 0, width = 12)
        scaler4 = tk.Scale(self.window, from_ = 0, to = 9, variable = self.d, length = 200, background='#2f3c71', fg = 'red', highlightthickness = 0, width = 12)
        scaler5 = tk.Scale(self.window, from_ = 0, to = 9, variable = self.e, length = 200, background='#2f3c71', fg = 'red', highlightthickness = 0, width = 12)
        scaler6 = tk.Scale(self.window, from_ = 0, to = 9, variable = self.f, length = 200, background='#2f3c71', fg = 'red', highlightthickness = 0, width = 12)#, length = 200,orient=HORIZONTAL)
        scaler1.grid(row = 1, column = 1)
        scaler2.grid(row = 1, column = 2)
        scaler3.grid(row = 1, column = 3)
        scaler4.grid(row = 1, column = 4)
        scaler5.grid(row = 1, column = 5)
        scaler6.grid(row = 1, column = 6)
    def get_pin(self):
        en = self.x
        a, b, c, d, e, f = self.a, self.b, self.c, self.d, self.e, self.f
        st = [a.get(), b.get(), c.get(), d.get(), e.get(), f.get()]
        st = ''.join(list(map(str, st)))
        return st    
    def executingE(self):
        PIN, password = self.get_pin(), self.x.get()
        PIN = [int(i) for i in PIN]
        obj = self.encryption
        Rotor_lst = rotors.Rotor_lst
        PEL = obj.encrypting_package(PIN, Rotor_lst)
        passwordE = obj.processE(PEL, password)
        txt_msg = f'Your encrypted password is {passwordE}\nClick OK to copy to clipboard else cancel'
        state_of_message_bx = mbx.askokcancel(title = "Encrypted Password", message = txt_msg)
        if state_of_message_bx:
            mbx.showinfo('Confirmation', 'Copied to clipboard')
            pyperclip.copy(passwordE)
    def executingD(self):
        PIN, password = self.get_pin(), self.x.get()
        PIN = [int(i) for i in PIN]
        obj = self.encryption
        Rotor_lst = rotors.Rotor_lst
        PEL = obj.encrypting_package(PIN, Rotor_lst)
        passwordE = obj.processD(PEL, password)
        txt_msg = f'Your decrypted password is {passwordE}\nClick OK to copy to clipboard else cancel'
        state_of_message_bx = mbx.askokcancel(title = "Decrypted Password", message = txt_msg)
        if state_of_message_bx:
            mbx.showinfo('Confirmation', 'Copied to clipboard')
            pyperclip.copy(passwordE)
    def get_encrypted(self):
        btn = tk.Button(self.window, text = 'Encrypt', command = self.executingE, bg = '#2d5289', fg = 'white', width = 25)
        btn.grid(row = 0, column = 7)
    def get_decrypted(self):
        btn = tk.Button(self.window, text = 'Decrypt', command = self.executingD, bg = '#2d5289', fg = 'white', width = 25)
        btn.grid(row = 2, column = 7, padx = 50, pady = 40)        
class Executer():
    def __init__(self, password, pin):
        self.pin, self.password = pin, password
    def application(self):
        PIN = [int(i) for i in self.pin]    
if __name__ == "__main__":
    root = tk.Tk()
    encryption = Rotor()
    ob = UI(root, encryption)
    ob.scaler()
    ob.entry()
    ob.get_encrypted()
    ob.get_decrypted()
    ob.label()
    root.mainloop()
