#All files should be in the same folder
#Copy this link to download the objects used in this project: https://drive.google.com/file/d/10bGXO8AnMVzECTuLt-Ads7stdj-pyiAv/view?usp=drivesdk

import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import pickle

stock = {}

def savedetails():
	identity = accountnamevalue.get()
	stock[identity] = passwordvalue.get()
	with open("pwd.vishal", "wb") as passwords:
		pickle.dump(stock, passwords)
		messagebox.showinfo("Success", "Account saved successfully!")

def getdetails():
	entry = maspassvalue.get()
	account= account_name_value.get()
	if entry == "09876":
		
		#try:
		with open("pwd.vishal", "br") as passwordfile:
			pwd = pickle.load(passwordfile)
			if account in pwd:
				messagebox.showinfo("Success", f"Password of {account} is:\n{pwd[account]}")
					
			else:
				messagebox.showerror("Failed","Your account name not found!")
		#except Exception as e:
			#messagebox.showwarning("Fatal Error","Password database missing!")
	else:
		messagebox.showerror("Error", "Incorrect Password!")
		

screen = tkinter.Tk()
screen.configure(bg="white")

appname = Image.open("title.png").resize((750, 400), Image.ANTIALIAS)
conappname = ImageTk.PhotoImage(appname)
conappnamelabel = tkinter.Label(screen, image=conappname, bg="white")
conappnamelabel.pack()

tkinter.Label(screen, text="Save Password", bg="white", fg="black", font="comicsansms 8 bold").pack()
tkinter.Label(screen, text="Account Name", bg="white", fg="black").pack()

accountnamevalue = tkinter.StringVar()
passwordvalue = tkinter.StringVar()

accountnameentry = tkinter.Entry(screen, textvariable=accountnamevalue)
accountnameentry.pack()

tkinter.Label(screen, text="Password", bg="white", fg="black").pack()

passentry = tkinter.Entry(screen, textvariable=passwordvalue)
passentry.pack()


btnimageopen = Image.open("btn.png").resize((270, 80), Image.ANTIALIAS)
btnimage = ImageTk.PhotoImage(btnimageopen)
tkinter.Button(screen, image=btnimage, bd=0, command=savedetails, bg="white", activebackground="white").pack(pady=5)

tkinter.Label(screen, text="", bg="white", fg="black", font="comicsansms 8 bold").pack(pady=20)

tkinter.Label(screen, text="Get Password", bg="white", fg="black", font="comicsansms 8 bold").pack()
tkinter.Label(screen, text="Account Name", bg="white", fg="black").pack()

account_name_value = tkinter.StringVar()
account_name_entry = tkinter.Entry(screen, textvariable=account_name_value)
account_name_entry.pack()

tkinter.Label(screen, text="Enter Master Password", bg="white", fg="black").pack()
maspassvalue = tkinter.StringVar()
maspassentry = tkinter.Entry(screen, textvariable=maspassvalue)
maspassentry.pack()

btngetimageopen = Image.open("btnget.png").resize((270, 80), Image.ANTIALIAS)
btngetimage = ImageTk.PhotoImage(btngetimageopen)
tkinter.Button(screen, image=btngetimage, bd=0, command=getdetails, bg="white", activebackground="white").pack(pady=5)

#tkinter.Label(screen, text="", bg="white").pack()

bottom = Image.open("btm.png").resize((750, 200), Image.ANTIALIAS)
conbottom = ImageTk.PhotoImage(bottom)
conbottomlabel = tkinter.Label(screen, image=conbottom, bg="white")
conbottomlabel.pack(side="bottom")

screen.mainloop()