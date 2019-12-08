#!/usr/bin/env python3

Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  ", ]

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

#построчный перебор семи строк в каждом элементе в Digits
second=(0,1,2,3,4,5,6)
for i in second:
	for a in p:
		number=int(a)
		for elem in Digits[number][i]:

			#замена (*) на цифровое занчение
			if elem == '*':
				elem=a
			print(elem, end = "")

		print("  ", end = "")
	print()


