import tkinter as tk
import tkinter.messagebox as mbx
import pyperclip
#---------------------------------------------------------------------
#                       Constans
#---------------------------------------------------------------------
HEAD_LINE = "Courier"
LABEL_FONT = "Carbon"
LABEL_SIZE = 10
#---------------------------------------------------------------------
#                       Windows
#---------------------------------------------------------------------
                     #main window
window = tk.Tk()
window.title("    Password Manager")
window.config(padx = 10, pady = 10, bg = "white")
                     #Local window
#--------------------------------------------------------------------#
#                       Code starts from here                        #
#--------------------------------------------------------------------#
#---------------------------------------------------------------------
#                           Command button functions
#---------------------------------------------------------------------

def test(st1, st2):
    return any(list(i in st2 for i in st1))

def generated_password():
    import string, random
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    random.shuffle(characters)          #random.shuffle(lst) returns shuffle to lst itself
    password_length = 12
    while True:
        pasvrd = random.choices(characters, k = password_length)
        pasvrd = ''.join(pasvrd)
        if any(list(i in string.ascii_letters for i in pasvrd)) and any(list(i in string.digits for i in pasvrd)) and any(list(i in "!@#$%^&*()" for i in pasvrd)):
            break
    return "".join(pasvrd)


        #---------------------------------------------------------------------
        #             Save to file command of add_btn
        #---------------------------------------------------------------------
def save_to_file():
    if username_e.get() != "" and website_e.get() != "" and password_e.get() != "":
        txt_msg =f'''
Do you want to save
password: {password_e.get()}
username: {username_e.get()}
website: {website_e.get()}                        
                        '''
        state_of_message_bx = mbx.askokcancel(title = "Confirmation", message = txt_msg)
        #If you select of for the above message box then state_of_message_bx = True
        if state_of_message_bx:
            mbx.showinfo("Successful", "Credentials saved successfully and copied to clipboard.")
            with open("saved_passwords.txt", mode = "a") as file:
                file.write(f"{website_e.get()},{username_e.get()},{password_e.get()}\n")
            pyperclip.copy(password_e.get())
            website_e.delete(0, tk.END)
            username_e.delete(0, tk.END)
            password_e.delete(0, tk.END)
    else:
        mbx.showerror("Error", "Please fill all the fields.")
        #---------------------------------------------------------------------
        #             Password generation: command of g_password_btn
        #---------------------------------------------------------------------
def pass_generation():
    password_e.delete(0, tk.END) #basically it clears the entry to create put it's newly generated password
    if username_e.get() == "" or website_e.get() == "":
        mbx.showerror('Error', "Either website or username is empty.")
    else:
        final_password = generated_password()
        password_e.insert(tk.END, final_password)




#---------------------------------------------------------------------
#                      Creating a Headline Label
#---------------------------------------------------------------------
head_line = tk.Label(window, text = "Password Manager", fg = "black", bg = "white", font = (HEAD_LINE, 18, 'bold'))
head_line.grid(row = 0, column = 1)
#---------------------------------------------------------------------
#                      Creating a Headline Label
#---------------------------------------------------------------------
img_data = tk.PhotoImage(file = "logo.png")
#print(img_data) >>> pyimage1
cnvs = tk.Canvas(window, width = 215, height = 210, bg = "white", highlightthickness = 0)
cnvs.create_image(215/2, 210/2, image = img_data)
cnvs.grid(row = 1, column = 1)
#---------------------------------------------------------------------
#                      Creating a Headline Label
#---------------------------------------------------------------------
#Creating all Label just left to all of the entries
website_L = tk.Label(window, text = "Website:", fg = "black", bg = "white", font = (LABEL_FONT, LABEL_SIZE, 'bold'))
username_L = tk.Label(window, text = "Username:", fg = "black", bg = "white", font = (LABEL_FONT, LABEL_SIZE, 'bold'))
password_L = tk.Label(window, text = "Password:", fg = "black", bg = "white", font = (LABEL_FONT, LABEL_SIZE, 'bold'))
             #--------------------------------------------------
             #          .grid Labels
             #--------------------------------------------------
website_L.grid(row = 2, column = 0)
username_L.grid(row = 3, column = 0)
password_L.grid(row = 4, column = 0)
#---------------------------------------------------------------------
#                           All buttons
#---------------------------------------------------------------------
add_btn = tk.Button(window, text = "Save to file", command = save_to_file, width = 20, bg = 'blue', fg = 'white', font = ('Ariel', 10, 'bold'))
g_password_btn = tk.Button(window, text = "Generate Random Password", command = pass_generation, width = 22, font = ('Halyard', 10, 'bold'))
             #--------------------------------------------------
             #          .grid button
             #--------------------------------------------------
add_btn.grid(row = 5, column = 1)
g_password_btn.grid(row = 4, column = 2)
#---------------------------------------------------------------------
#                      All Entries
#---------------------------------------------------------------------
website_e = tk.Entry(window, width = 64, bd = 3)
website_e.focus()
username_e = tk.Entry(window, width = 64, bd = 3)
password_e = tk.Entry(window, width = 33, bd = 3)
             #--------------------------------------------------
             #          #.grid all of the entries
             #--------------------------------------------------
website_e.grid(row = 2, column = 1, columnspan = 2, pady = 5)
username_e.grid(row = 3, column = 1, columnspan = 2, pady = 5)
password_e.grid(row = 4, column = 1, pady = 5)
window.mainloop()
#(215, 210)
