#!/usr/bin/env python2

patterns = [
	'1qaz',
	'!QAZ',
	'2wsx',
	'@WSX',
	'3edc',
	'#EDC',
	'4rfv',
	'$RFV',
	'5tgb',
	'%TGB',
	'6yhn',
	'^YHN',
	'7ujm',
	'&UJM',
	'8ik,',
	'*IK<',
	'9ol.',
	'(OL>',
	'0p;/',
	')P:?',
	'=[;.',
	'+{:>',
	'-pl,',
	'_PL<',
	'0okm',
	')OKM',
	'9ijn',
	'(IJN',
	'8uhb',
	'*UHB',
	'7ygv',
	'&YGV',
	'6tfc',
	'^TFC',
	'5rdx',
	'%RDX',
	'4esz',
	'$ESZ',
	'1234',
	'qwer',
	'asdf',
	'zxcv',
	'2345',
	'wert',
	'sdfg',
	'xcvb',
	'3465',
	'erty',
	'dfgh',
	'cvbn',
	'457',
	'rtyu',
	'fghj',
	'vbmn',
	'5678',
	'tyui',
	'ghjk',
	'bnm,',
	'6789',
	'yuio',
	'hjkl',
	'nm,.',
	'7890',
	'uiop',
	'jkl;',
	'm,./',
	'!@#$',
	'QWER',
	'ASDF',
	'ZXCV',
	'@#$%',
	'WERT',
	'SDFG',
	'XCVB',
	'#$%^',
	'ERTY',
	'DFGH',
	'CVBN',
	'$%^&',
	'RTYU',
	'FGHJ',
	'VBNM',
	'%^&*',
	'TYUI',
	'GHJK',
	'BN<M',
	'^&*(',
	'YUIO',
	'HJKL',
	'NM<>',
	'&*()',
	'UIOP',
	'JKL:',
	'M<>?',
]

patternrev=[]
for x in patterns:
	patternrev.append(x[::-1])

patterns.extend(patternrev)

for a in patterns:
	for b in patterns:
		for c in patterns:
			for d in patterns:
				print "{}{}{}{}".format(a, b, c, d)
