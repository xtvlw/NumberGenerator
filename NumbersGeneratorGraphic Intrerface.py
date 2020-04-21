#_[N_F]_
from tkinter import *
from random import randrange

root = Tk()

class Mold:
	def button(Height, Width, Text, X, Y, click, Font):
		button = Button(root, width=Width, height=Height, text=Text, font=Font, command=click)
		button.place(x=X, y=Y)

	def label(Height, Width, Text, X, Y, Font, re, color):
		label = Label(root, width=Width, height=Height, text=Text, font=Font, relief=re, justify=LEFT, anchor=W, background=color)
		label.place(x=X, y=Y)
		return label

	def box(Width, X, Y, Font):
		box = Entry(root, width=Width, font=Font)
		box.place(x=X, y=Y)
		return box


def function():
	xLabel, yLabel, n, n1 = 10, 150, 39, 0
	try:
		From = int(bx1.get())
		To = int(bx2.get()) + 1
		elements = int(bx3.get())
	except:
		return 0
	for i in range(200):
		i = Mold.label(1, 15, "", xLabel, yLabel, "arial 12", re="flat", color=None)
		yLabel += 20
		if n1 == n:
			yLabel = 150
			xLabel += 140
			n +=40
		n1 += 1
	xLabel, yLabel, n, n1 = 10, 150, 39, 0
	if elements > 200:
		AlertLabel = Mold.label(1, 25, "the max is 200", 250, 70, Font="arial 12", re="solid", color="white")
	else:
		AlertLabel = Mold.label(1, 25, "", 250, 70, Font="arial 12", re="flat", color=None)
		for i1 in range(elements):
			x = randrange(From, To)
			i = Mold.label(1, 15, "number {} : {}".format(i1 + 1, x), xLabel, yLabel, "arial 12", re="solid", color="white")
			yLabel += 20
			if n1 == n:
				yLabel = 150
				xLabel += 140
				n +=40
			n1 += 1


b1 = Mold.button(Height=1, Width=15, Text="Generate", X=50, Y=100, click=function, Font="arial 12")

bx1Label = Mold.label(Height=1, Width=15, Text="From", X=10, Y=10, Font="arial 12", re="flat", color="white")
bx1 = Mold.box(Width=10, X=150, Y=10, Font="arial 12")

bx2Label = Mold.label(Height=1, Width=15, Text="To", X=10, Y=40, Font="arial 12", re="flat", color="white")
bx2 = Mold.box(Width=10, X=150, Y=40, Font="arial 12")

bx3Label = Mold.label(Height=1, Width=15, Text="Nº of elements", X=10, Y=70, Font="arial 12", re="flat", color="white")
bx3 = Mold.box(Width=10, X=150, Y=70, Font="arial 12")


root.geometry("900x1000")
root.mainloop()