from tkinter import *

def buttonClicked():
	global e1, e2
	text = e1.get()
	print(e1 + e2)
	add.config(text = f"+")
	
	



myFirstApp = Tk()
myFirstApp.geometry("800x800")
myFirstApp.title("Addition Calculator")
text1 = Label(myFirstApp, text = "Enter a number",
	font = ("Arial", 20))
text1.pack()

e1 = Entry(myFirstApp, width = 30)
e1.pack()


b1 = Button(myFirstApp, text = "OK", command = buttonClicked,
font = ("Calibri", 50))
b1.pack()


add = Label(myFirstApp,text = "",
	font = ("Arial", 100))
add.pack()


e2 = Entry(myFirstApp, width = 30)
e2.pack()

b2= Button(myFirstApp, text = "OK", command = buttonClicked,
font = ("Calibri", 50))
b2.pack()



myFirstApp.mainloop()

