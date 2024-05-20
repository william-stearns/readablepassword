#!/usr/bin/env python3
"""
Converts raw ascii characters into readable words.
Feed characters on stdin or give filenames to convert on the command line.  Examples:
echo "Convert me" | ./readable-password.py
./readable-password.py file1 file2
Works fine under both python2 and python3

Sample command to generate a new password, show it, and show it in readable form:
apg -a 0 -m 20 -x 20 -M SNCL -E '015|' -n 1 | tee -a /dev/stderr | readable-password.py 
Sonir/Quotdoylvayss2
SIERRA oscar november india romeo forwardslash QUEBEC uniform oscar tango delta oscar yankee lima victor alfa yankee sierra sierra two lf 

Copyright 2019 William Stearns <william.l.stearns@gmail.com>
Released under the GPL version 3.

"""

from __future__ import print_function


__version__ = '0.5'

__author__ = 'William Stearns'
__copyright__ = 'Copyright 2019-2024, William Stearns'
__credits__ = ['William Stearns']
__email__ = 'william.l.stearns@gmail.com'
__license__ = 'GPL 3.0'
__maintainer__ = 'William Stearns'
__status__ = 'Production'                                #Prototype, Development or Production



#Dictionary of phonetic equivalents for most of the bottom half of the ascii table.
phonetic_alphabet_table = {
	chr(0): 'nul',
	chr(1): 'soh',
	chr(2): 'stx',
	chr(3): 'etx',
	chr(4): 'eot',
	chr(5): 'enq',
	chr(6): 'ack',
	chr(7): 'bel',
	chr(8): 'bs',
	chr(9): 'tab',
	chr(10): 'lf',
	chr(11): 'vt',
	chr(12): 'ff',
	chr(13): 'cr',
	chr(14): 'so',
	chr(15): 'si',
	chr(16): 'dle',
	chr(17): 'dc1',
	chr(18): 'dc2',
	chr(19): 'dc3',
	chr(20): 'dc4',
	chr(21): 'nak',
	chr(22): 'syn',
	chr(23): 'etb',
	chr(24): 'can',
	chr(25): 'em',
	chr(26): 'sub',
	chr(27): 'esc',
	chr(28): 'fs',
	chr(29): 'gs',
	chr(30): 'rs',
	chr(31): 'us',
	' ': 'space',
	'!': 'exclamationpoint',
	'"': 'doublequote',
	'#': 'hash',
	'$': 'dollarsign',
	'%': 'percent',
	'&': 'ampersand',
	"'": 'singlequote',
	'(': 'leftparentheses',
	')': 'rightparentheses',
	'*': 'asterisk',
	'+': 'plus',
	',': 'comma',
	'-': 'minus',
	'.': 'period',
	'/': 'forwardslash',
	'0': 'zero',
	'1': 'one',
	'2': 'two',
	'3': 'three',
	'4': 'four',
	'5': 'five',
	'6': 'six',
	'7': 'seven',
	'8': 'eight',
	'9': 'niner',
	':': 'colon',
	';': 'semicolon',
	'<': 'lessthan',
	'=': 'equals',
	'>': 'greaterthan',
	'?': 'questionmark',
	'@': 'at',
	'A': 'ALFA',
	'B': 'BRAVO',
	'C': 'CHARLIE',
	'D': 'DELTA',
	'E': 'ECHO',
	'F': 'FOXTROT',
	'G': 'GOLF',
	'H': 'HOTEL',
	'I': 'INDIA',
	'J': 'JULIETT',
	'K': 'KILO',
	'L': 'LIMA',
	'M': 'MIKE',
	'N': 'NOVEMBER',
	'O': 'OSCAR',
	'P': 'PAPA',
	'Q': 'QUEBEC',
	'R': 'ROMEO',
	'S': 'SIERRA',
	'T': 'TANGO',
	'U': 'UNIFORM',
	'V': 'VICTOR',
	'W': 'WHISKEY',
	'X': 'X-RAY',
	'Y': 'YANKEE',
	'Z': 'ZULU',
	'[': 'leftsquarebracket',
	'\\': 'backslash',
	']': 'rightsquarebracket',
	'^': 'caret',
	'_': 'underscore',
	'`': 'backquote',
	'a': 'alfa',
	'b': 'bravo',
	'c': 'charlie',
	'd': 'delta',
	'e': 'echo',
	'f': 'foxtrot',
	'g': 'golf',
	'h': 'hotel',
	'i': 'india',
	'j': 'juliett',
	'k': 'kilo',
	'l': 'lima',
	'm': 'mike',
	'n': 'november',
	'o': 'oscar',
	'p': 'papa',
	'q': 'quebec',
	'r': 'romeo',
	's': 'sierra',
	't': 'tango',
	'u': 'uniform',
	'v': 'victor',
	'w': 'whiskey',
	'x': 'x-ray',
	'y': 'yankee',
	'z': 'zulu',
	'{': 'leftcurlybracket',
	'|': 'verticalpipe',
	'}': 'rightcurlybracket',
	'~': 'tilde',
	chr(127): 'del'
}


def convert_ascii_to_phonetic(raw_string: str):
	"""Using the phonetic_alphabet_table , convert a provided ascii string to its phonetic equivalent."""

	phonetic_out: str = ''

	for one_char in raw_string:
		phonetic_out = phonetic_out + phonetic_alphabet_table.get(one_char, 'UNMATCHED') + ' '

	return phonetic_out


if __name__ == "__main__":
	import fileinput

	line: str

	for line in fileinput.input():
		print(convert_ascii_to_phonetic(line))
