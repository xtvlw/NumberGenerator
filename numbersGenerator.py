#_[N_F]_
from random import randrange

From = int(input("from : "))
To = int(input("to : "))
Nelements = int(input("Nº of elements : ")) + 1

for i in range(Nelements):
	x = randrange(From, To)
	print("number {} : {} ". format(i+1, x))
