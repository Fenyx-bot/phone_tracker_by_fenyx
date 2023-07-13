#Imports <33
from tkinter import *
from unicodedata import name
import phonenumbers as nb
from phonenumbers import geocoder, carrier
import os


root = Tk()
root.title("Phone Tracker")
root.maxsize(width= 600, height= 600)
root.minsize(width= 600, height= 600)
root.geometry("600x600+700+150")
root.config(bg= "#e3dac9")




def bk():
    root.deiconify()
    register.destroy()


def finish_register():
    #vars
    global f_nb
    
    f_name = name.get()
    f_fn = family_name.get()
    f_nb = rg_nb.get()
    all_users = os.listdir()


    if f_name == "" or f_fn == "" or f_nb == "":
        notif.config(fg= "red", text= "All Fields Are Required *")
        return


    for nb_check in all_users:
        if f_nb == nb_check:
            notif.config(fg= "red", text= "Phone Number Is Already Registered")
            return
        else:
            new_file = open(f_nb, "w")
            new_file.write(f_name + "\n")
            new_file.write(f_fn + "\n")
            new_file.write(f_nb)
            new_file.close()
            notif.config(fg= "blue", text= "Account Has Been Registered Successfully")
            return
    

def search():
    global login_number

    login_number = number.get()
    all_users = os.listdir()
    ename = "Unknown"
    efname = ""

    for f_nb in all_users:
        if login_number == f_nb:
            print("INFO:")
            file = open(f_nb, "r")
            file_data = file.read()
            user_details = file_data.split("\n")
            ename = user_details[0]
            efname = user_details[1]
            file.close()


    num = str(number.get())
    print(num)
    ch_number = nb.parse(num, "CH")
    print(geocoder.description_for_number(ch_number, "en"))

    service_nb = nb.parse(num, "RO")
    print(carrier.name_for_number(service_nb, "en"))

    #labels
    Label(root, text=ename+ " " + efname, font=("Calibri", 14), fg="#c0c0c0", bg= "#365577").place(x= 280, y= 325, anchor= "center")
    Label(root, text="From " + str(geocoder.description_for_number(ch_number, "en")), font=("Calibri", 14), fg="#c0c0c0", bg= "#365577").place(x= 280, y= 350, anchor= "center")
    Label(root, text="Using The Phone Service Of " + str(carrier.name_for_number(service_nb, "en")), font=("Calibri", 14), fg="#c0c0c0", bg= "#365577").place(x= 280, y= 375, anchor= "center")



def register():

    root.withdraw()
    global register

    register = Toplevel(root)
    register.title("Register")
    register.maxsize(width= 600, height= 600)
    register.minsize(width= 600, height= 600)
    register.geometry("600x600+700+150")
    register.config(bg= "#c9aa88")

    #vars
    global name
    global family_name
    global rg_nb
    global notif

    name = StringVar()
    family_name = StringVar()
    rg_nb = StringVar()

    #labels
    L= Label (register, text= "Register A New Phone Number", font= ("Calibri", 20), bg= "#c9aa88").place(x= 300, y= 25, anchor= "center")
    Label (register, text= "Name ", font= ("Calibri", 16), bg= "#c9aa88").place(x= 50, y= 125)
    Label (register, text= "Family Name ", font= ("Calibri", 16), bg= "#c9aa88").place(x= 50, y= 225)
    Label (register, text= "Phone Number ", font= ("Calibri", 16), bg= "#c9aa88").place(x= 50, y= 325)
    notif = Label (register, font= ("Calibri", 16), bg= "#c9aa88")
    notif.place(x= 285, y= 425, anchor= "center")

    #Entries
    Entry (register,textvariable= name,  width= 20, font= "large_font").place(x= 250, y= 127)
    Entry (register,textvariable= family_name,  width= 20, font= "large_font").place(x= 250, y= 227)
    Entry (register,textvariable= rg_nb,  width= 20, font= "large_font").place(x= 250, y= 327)

    #Buttons
    Button (register, text= "Register",command= finish_register, font= ("Calibri", 12), width= 30, bg= "#c0c0c0").place(x= 285, y= 525, anchor= "center")
    Button (register, text= "Back",command= bk, font= ("Calibri", 12), width= 30, bg= "#c0c0c0").place(x= 285, y= 560, anchor= "center")



    

#vars
global number
number = StringVar()

#labels
Label (root,text= "Phone Tracker 1.0 By Fenyx", font=("helvetica", 20), bg= "#e3dac9").place(x= 300, y= 50, anchor= "center")
Label (root,text= "Enter The Phone Number ", font=("Calibri", 14), bg= "#e3dac9").place(x= 160, y= 135, anchor= "center")
Label (root, text= "Help Us Expand Our Database", font=("calibri", 14), bg= "#e3dac9").place(x= 285, y= 480, anchor= "center")

#entires
Entry (root,textvariable= number, font=("Calibri", 12)).place(x= 300, y= 125)


#buttons

Button (root,text= "Add A New Phone Number",command= register, font= ("Calibri", 12), bg= "#c0c0c0").place(x= 285, y= 525, anchor= "center")
Button (root, text= "Search Number",command= search, font= ("Calibri", 12), bg= "#c0c0c0").place(x= 235, y= 225)


root.mainloop()