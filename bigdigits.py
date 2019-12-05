#!/usr/bin/env python

Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]

One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
	
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]

Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]

Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ",
        "   *  "]

Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]

Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]

Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]

Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]

	
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]


Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

import sys
p=sys.argv[1]
lenth = len (p)
print (type (lenth))

for i in p:
	a=int(i)
	if a == 0:
		a=Digits[0]
		print(a)
	elif a == 1:
		a=Digits[1]
		print(a)
	elif a == 2:
		a=Digits[2]
		print(a)
	elif a == 3:
		a=Digit[3]
		print(a)
	elif a == 4:
		a=Digits[4]
		print(a)
	elif a == 5:
		a=Digits[5]
		print(a)
	elif a == 6:
		a=Digits[6]
		print(a)
	elif a == 7:
		a=Digits[7]
		print(a)
	elif a == 8:
		a=Digits[8]
		print(a)
	elif a == 9:
		a=Digits[9]
		print(a)
	else:
		print('error')

