from tkinter import *



def buttonClicked():
	global text, text2
	text = int(e1.get())
	text2 = int(e2.get())
	answer.config(text = f"{text}+{text2}={text+text2}")

	
	
	
myFirstApp = Tk()
myFirstApp.geometry("800x800")
myFirstApp.title("Addition Calculator")
text1 = Label(myFirstApp, text = "Enter a number",
	font = ("Arial", 20))
text1.pack()

e1 = Entry(myFirstApp, width = 30)
e1.pack()


#b1 = Button(myFirstApp, text = "OK", command = buttonClicked,
#font = ("Calibri", 50))
#b1.pack()


add = Label(myFirstApp,text = "+",
	font = ("Arial", 100))
add.pack()

test = Label(myFirstApp, text = "Enter another number",
	font = ("Arial", 17))
test.pack()

e2 = Entry(myFirstApp, width = 30)
e2.pack()

b2= Button(myFirstApp, text = "ANSWER", command = buttonClicked,
font = ("Calibri", 30))
b2.pack()


answer = Label(myFirstApp, text = "",
	font = ("Arial", 30))
answer.pack()



myFirstApp.mainloop()

