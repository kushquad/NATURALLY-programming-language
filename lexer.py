#!/usr/bin/env python

import sys

def interpret(comp):
	print comp

try:
	code = open(sys.argv[1])
except:
	"No input files provided as argument. Compilation terminated."

print "Compiling...\n"
blocks = code.readlines()
for block in blocks:
	statements = block.split('.')
	for statement in statements:
		components = statement.split(',')
		interpret(components)

