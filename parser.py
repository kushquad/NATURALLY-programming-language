import re
import sys
import lexer

def isinteger(str):
	try:
		int(str)
		return True
	except:
		return False
		
def commentmatch(tomatch):
	if(tomatch[0]=='//'):
		return (True, '#'+tomatch[1])
	return (False,"")
	
def variabledeclarationmatch(tomatch):
	if(tomatch[0].lower()=="let" and tomatch[2].lower() == "be"):
		return (True, tomatch[1]+" = "+tomatch[3]) 	
	elif(tomatch[0].lower()=="set" and tomatch[2].lower() == "to"):
		return (True, tomatch[1]+" = "+tomatch[3])
	elif(tomatch[0].lower()=="define" and tomatch[2].lower()=="as"):
		return (True, tomatch[1]+" = "+tomatch[3])
	elif(tomatch[0].lower()=="declare" and tomatch[2].lower()=="as"):
		return (True, tomatch[1]+" = "+tomatch[3])
	return (False, "")

def classdeclarationmatch(tomatch,comma):
	if((tomatch[0].lower()=="define" or tomatch[0].lower()=="declare") and tomatch[1].lower()=="class"):
		return (True, "class "+tomatch[2]+":")
	return (False, "")

def functiondeclarationmatch(tomatch,comma):
	if((tomatch[0].lower()=="define" or tomatch[0].lower()=="declare") and tomatch[1].lower()=="function"):
		return (True, "def "+tomatch[2]+":")
	return (False, "")
	
def ifdeclarationmatch(tomatch,comma):
	if(tomatch[0].lower()=="if"):
		return (True, "if "+tomatch[1]+":")
	if((tomatch[0].lower()=="else" and tomatch[1].lower()=="if")):
		return (True, "elif "+tomatch[2]+":")
	if(tomatch[0].lower()=="elif"):
		return (True, "elif "+tomatch[1]+":")
	if(tomatch[0].lower()=="else"):
		return (True, "else:")
	return (False, "")
	
def fordeclarationmatch(tomatch,comma):
	if(tomatch[0].lower()=="for" and isinteger(tomatch[1]) and("time" in tomatch[2].lower())):
		return (True, "for __count__ in xrange(0,"+tomatch[1]+"):")
	return (False, "")

def inputmatch(tomatch):
	#Have to add code to parse appropriately?
	if(tomatch[0].lower() in ["read","input"]):
		return (True, tomatch[1]+' = '+"raw_input()")
	return (False, "")
	
def outputmatch(tomatch):
	if(tomatch[0].lower()=="print"):
		return (True, "print "+tomatch[1])
	return (False, "")
	
def macromatch(tomatch):
	l = len(tomatch)
	for i in xrange(0,l-3):
		if(tomatch[i].lower()=="greater" and tomatch[i+1].lower()=="than" and "equal" in tomatch[i+2].lower()):
			tomatch[i] = ">="
			tomatch[i+1] = tomatch[i+2] = ""
			print tomatch
		elif(tomatch[i].lower()=="lesser" and tomatch[i+1].lower()=="than" and "equal" in tomatch[i+3].lower()):
			tomatch[i] = "<="
			tomatch[i+1] = tomatch[i+2] = ""
	print tomatch
	return lexer.clean(tomatch)
	
def parse(tabs,comma,str):
	rules = [
				commentmatch(str),variabledeclarationmatch(str),
			 	classdeclarationmatch(str,comma),functiondeclarationmatch(str,comma),
			 	ifdeclarationmatch(str,comma),fordeclarationmatch(str,comma),
			 	inputmatch(str), outputmatch(str), macromatch(str)
			]
	for rule in rules:
		res = rule
		if(res[0]):
			return tabs*"\t"+res[1]	
	return "Compilation Error."
		
while(1):
	string = raw_input()
	if(string == 'q'):
		break
	lexed = lexer.lexify(string)
	print parse(lexed[0],lexed[1],lexed[2])
