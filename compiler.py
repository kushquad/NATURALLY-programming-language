#!/usr/bin/env python

import parser
import lexer
import os
import sys

try:
	filename = sys.argv[1]
except:
	print "No input files passed as argument. Compilation terminated."
	sys.exit()

if(filename.endswith(".nat")):
	
	file = ""
	try:
		file = open(filename)
	except:
		print "File does not exist at path. Compilation terminated."
		sys.exit()

	compiled = open(filename[:-4],"w")
	compiled.write("#!/usr/bin/env python\n")
	print "Compiling..."

	i = 1
	
	for line in file:
		
		try:		
			lexed = lexer.lexify(line)
			parsed = parser.parse(lexed[0],lexed[1],lexed[2])
			compiled.write(parsed)
		except:
			print "Compilation Error"+" at line "+str(i)+"."
			os.system("rm "+filename[:-4])
			sys.exit()
		i += 1

	print "Compilation complete."
	print "Creating executable."
	os.system("chmod +x "+filename[:-4])

else:
	print "Invalid filetype. (.nat expected)"
