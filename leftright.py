#!/usr/bin/env python2

lkeybmap = [
	[ '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='  ],
	[  'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']' ],
	[   'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';'          ],
	[    'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'         ]
]


ukeybmap = [
	[ '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+'  ],
	[  'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}' ],
	[   'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':'          ],
	[    'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?'         ]
]

patterns = []

def genlrpatterns(map):
	for x in range(0,10):
		for x2 in range(x+1,10):
			s = ""
			for y in range(0,4):
				s+="{}{}".format(map[y][x], map[y][x2])
			patterns.append(s)

genlrpatterns(lkeybmap)
genlrpatterns(ukeybmap)

for a in patterns:
	for b in patterns:
		print "{}{}".format(a, b)
