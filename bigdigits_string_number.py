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
i=0
while i < 7:
	for a in p:
		number=int(a)
		string=str(number)
		for elem in Digits[number][i]:

			#замена (*) на цифровое занчение
			if elem == '*':
				elem=string

			print(elem, end = "")
		print("  ", end = "")
	i+=1
	print()


