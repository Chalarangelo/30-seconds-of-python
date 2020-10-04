#!/usr/bin/env python
# coding: utf-8

# # CALCULATOR
# 
# SIMPLE CALCULATOR THAT CAN PERFORM FOLLOWING OPERATIONS
#  BASIC OPERATIONS
# 1. ADDITION
# 2. SUBTRACTION
# 3. MULTIPLICATION
# 4. DIVISION
# 5. MODULUS
# 
#  ADVANCED OPERATIONS
# 1. NATURAL LOG
# 2. TRIGNOMETRIC CALCULATIONS
# 3. EXPONENTIAL CALCULATIONS

# In[ ]:



from tkinter import *
import math as m
root =Tk()
# GIVING TITLE TO THE APPLICATION AS simple calculator
root.title("Simple Calculator")
e = Entry(root, width=50, borderwidth=5, relief=RIDGE, fg="White", bg="Black")
e.grid(row=0, column=0, columnspan=5, padx=10, pady=15)

# Creating some userdefined functions for the operations involved in the application.
def click(to_print):
	old=e.get()
	e.delete(0, END)
	e.insert(0, old+to_print)
	return

def sc(event):
	key=event.widget
	text=key['text']
	no=e.get()
	result=''
	if text=='deg':
		result=str(m.degrees(float(no)))
	if text=='sin':
		result=str(m.sin(float(no)))
	if text=='cos':
		result=str(m.cos(float(no)))
	if text=='tan':
		result=str(m.tan(float(no)))
	if text=='lg':
		result=str(m.log10(float(no)))
	if text=='ln':
		result=str(m.log(float(no)))
	if text=='Sqrt':
		result=str(m.sqrt(float(no)))
	if text=='x!':
		result=str(m.factorial(float(no)))
	if text=='1/x':
		result=str(1/(float(no)))
	if text=='pi':
		if no=="":
			result=str(m.pi)
		else:
			result=str(float(no) * m.pi)
	if text=='e':
		if no=="":
			result=str(m.e)
		else:
			result=str(m.e**float(no))

	e.delete(0, END)
	e.insert(0, result)

# This function clears all the contents displayed on the computation window.
def clear():
	e.delete(0, END)
	return 

# This function clears one character from rare end of the string.
def bksps():
	current=e.get()
	length=len(current)-1
	e.delete(length, END)

# This function is defined to evaluate the results and to prompt on the console.
def evaluate():
	ans=e.get()
	ans=eval(ans)
	e.delete(0, END)
	e.insert(0, ans)
    
# Arrangement of buttons for better visualition and computation.
lg = Button(root, text="log", padx=24, pady=10, relief=RAISED, bg="Black", fg="White")
lg.bind("<Button-1>", sc)
ln = Button(root, text="ln", padx=28, pady=10, relief=RAISED, bg="Black", fg="White")
ln.bind("<Button-1>", sc)
par1st = Button(root, text="(", padx=29, pady=10, relief=RAISED, bg="Black", fg="White",command=lambda: click("("))
par2nd = Button(root, text=")", padx=30, pady=10, relief=RAISED, bg="Black", fg="White",command=lambda: click(")"))
dot = Button(root, text=".", padx=29, pady=10, relief=RAISED, bg="Green", fg="Black",command=lambda: click("."))

exp = Button(root, text="^", padx=29, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("**"))

degb = Button(root, text="deg", padx=23, pady=10, relief=RAISED, bg="Black", fg="White")
degb.bind("<Button-1>", sc)
sinb= Button(root, text="sin", padx=24, pady=10, relief=RAISED, bg="Black", fg="White",)
sinb.bind("<Button-1>", sc)
cosb= Button(root, text="cos", padx=23, pady=10, relief=RAISED, bg="Black", fg="White")
cosb.bind("<Button-1>", sc)
tanb = Button(root, text="tan", padx=23, pady=10, relief=RAISED, bg="Black", fg="White")
tanb.bind("<Button-1>", sc)


sqrtm = Button(root, text="Sqrt", padx=23, pady=10, relief=RAISED, bg="Black", fg="White")
sqrtm.bind("<Button-1>", sc)
ac = Button(root, text="C", padx=29, pady=10, relief=RAISED, bg="Dark Red", fg="White",command=lambda:clear())
bksp = Button(root, text="DEL", padx=24, pady=10, relief=RAISED, bg="Dark Red", fg="White",command=lambda: bksps())
mod = Button(root, text=" % ", padx=24, pady=10, relief=RAISED, bg="Black", fg="White",command=lambda: click("%"))
div = Button(root, text="/", padx=29, pady=10, relief=RAISED, bg="yellow", fg="Black",command=lambda: click("/"))

fact = Button(root, text="x!", padx=29, pady=10, relief=RAISED, bg="Black", fg="White")
fact.bind("<Button-1>", sc)
seven = Button(root, text="7", padx=30, pady=10, relief=RAISED, bg="Grey", fg="White",command=lambda: click("7"))
eight = Button(root, text="8", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White",command=lambda: click("8"))
nine = Button(root, text="9", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White",command=lambda: click("9"))
mult = Button(root, text="X", padx=29, pady=10, relief=RAISED, bg="Yellow", fg="Black",command=lambda: click("*"))

frac = Button(root, text="1/x", padx=25, pady=10, relief=RAISED, bg="Black", fg="White")
frac.bind("<Button-1>", sc)
four = Button(root, text="4", padx=30, pady=10, relief=RAISED, bg="Grey", fg="White",command=lambda: click("4"))
five = Button(root, text="5", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White",command=lambda: click("5"))
six = Button(root, text="6", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White",command=lambda: click("6"))
minus = Button(root, text="-", padx=29, pady=10, relief=RAISED, bg="Yellow", fg="Black",command=lambda: click("-"))

pib = Button(root, text="pi", padx=28, pady=10, relief=RAISED, bg="Black", fg="White")
pib.bind("<Button-1>", sc)
one = Button(root, text="1", padx=30, pady=10, relief=RAISED, bg="Grey", fg="White",command=lambda: click("1"))
two = Button(root, text="2", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White",command=lambda: click("2"))
three = Button(root, text="3", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White",command=lambda: click("3"))
plus = Button(root, text="+", padx=29, pady=10, relief=RAISED, bg="Yellow", fg="Black",command=lambda: click("+"))

e_b = Button(root, text="e", padx=29, pady=10, relief=RAISED, bg="Black", fg="White")
e_b.bind("<Button-1>", sc)
zero = Button(root, text="0", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White",command=lambda: click("0"))
equal = Button(root, text="=", padx=29, pady=10, relief=RAISED, bg="Dark Orange", fg="Black",command=lambda: evaluate())


bksp.grid(row=1, column=0)
ln.grid(row=1, column=1)
par1st.grid(row=1, column=2)
par2nd.grid(row=1, column=3)
ac.grid(row=1, column=4)

lg.grid(row=2, column=0)
degb.grid(row=2, column=1)
sinb.grid(row=2, column=2)
cosb.grid(row=2, column=3)
tanb.grid(row=2, column=4)

sqrtm.grid(row=3, column=0)
e_b.grid(row=3, column=1)
exp.grid(row=3, column=2)
mod.grid(row=3, column=3)
div.grid(row=3, column=4)

fact.grid(row=4, column=0)
seven.grid(row=4, column=1)
eight.grid(row=4, column=2)
nine.grid(row=4, column=3)
mult.grid(row=4, column=4)

frac.grid(row=5, column=0)
four.grid(row=5, column=1)
five.grid(row=5, column=2)
six.grid(row=5, column=3)
minus.grid(row=5, column=4)

pib.grid(row=6, column=0)
one.grid(row=6, column=1)
two.grid(row=6, column=2)
three.grid(row=6, column=3)
plus.grid(row=6, column=4)

dot.grid(row=7, column=1)
zero.grid(row=7, column=2)
equal.grid(row=7, column=3)

root.mainloop()






