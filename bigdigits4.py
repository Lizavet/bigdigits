#!/usr/bin/env python

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

second=(0,1,2,3,4,5,6)

for i in p:
	a=int(i)
	for x in second:
		print(Digits[a][x])


