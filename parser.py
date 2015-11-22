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
		return (True, tomatch[1]+" = "+" ".join(tomatch[3:])) 	
	elif(tomatch[0].lower()=="set" and tomatch[2].lower() == "to"):
		return (True, tomatch[1]+" = "+" ".join(tomatch[3:]))
	elif(tomatch[0].lower()=="define" and tomatch[2].lower()=="as"):
		return (True, tomatch[1]+" = "+" ".join(tomatch[3:]))
	elif(tomatch[0].lower()=="declare" and tomatch[2].lower()=="as"):
		return (True, tomatch[1]+" = "+" ".join(tomatch[3:]))
	return (False, "")

def classdeclarationmatch(tomatch,comma):
	if((tomatch[0].lower()=="define" or tomatch[0].lower()=="declare") and tomatch[1].lower()=="class"):
		return (True, "class "+tomatch[2]+":")
	return (False, "")

def functiondeclarationmatch(tomatch,comma):
	if((tomatch[0].lower()=="call" and tomatch[2].lower()=="with")):
		return (True, tomatch[1].lower()+"("+" ".join(tomatch[3:]).rstrip()+")\n")
	return (False, "")
	
def ifdeclarationmatch(tomatch,comma):
	if(tomatch[0].lower().rstrip()=="if" and len(tomatch)>1):
		return (True, "if "+" ".join(tomatch[1:]).rstrip('\n')+":\n")
	if((tomatch[0].lower().rstrip()=="else" and len(tomatch)>2 and tomatch[1].lower()=="if")):
		return (True, "elif "+" ".join(tomatch[2:]).rstrip('\n')+":\n")
	if(tomatch[0].lower().rstrip()=="elif" and len(tomatch)>1):
		return (True, "elif "+" ".join(tomatch[1:]).rstrip('\n')+":\n")
	if(tomatch[0].lower().rstrip()=="else"):
		return (True, "else:\n")
	return (False, "")
	
def whiledeclarationmatch(tomatch,comma):
	if(tomatch[0].lower().rstrip()=="while" and len(tomatch)>1):
		return (True, "while "+" ".join(tomatch[1:]).rstrip()+":\n")
	return (False, "")

def inputmatch(tomatch):
	#Have to add code to parse appropriately?
	if(tomatch[0].lower() in ["read","input"] and len(tomatch)==2):
		return (True, " ".join(tomatch[1:]).rstrip('\n')+' = '+"raw_input()\n")
	elif(tomatch[0].lower() in ["read","input"] and len(tomatch)==4 and tomatch[2].lower()=="as" and "int" in tomatch[3].lower()):
		return (True, tomatch[1].rstrip('\n')+' = '+"int(raw_input())\n")
	return (False, "")
	
def outputmatch(tomatch):
	if(tomatch[0].lower()=="print"):
		return (True, "print "+" ".join(tomatch[1:]))
	return (False, "")
	
def macromatch(tomatch):
	l = len(tomatch)
	for i in xrange(0,l):
		if(i<=l-3 and tomatch[i].lower()=="greater" and tomatch[i+1].lower()=="than" and "equal" in tomatch[i+2].lower()):
			tomatch[i] = ">="
			tomatch[i+1] = tomatch[i+2] = ""
		elif(i<=l-3 and tomatch[i].lower()=="lesser" and tomatch[i+1].lower()=="than" and "equal" in tomatch[i+2].lower()):
			tomatch[i] = "<="
			tomatch[i+1] = tomatch[i+2] = ""
		elif(i<=l-2 and tomatch[i].lower()=="lesser" and tomatch[i+1].lower()=="than"):
			tomatch[i] = "<"
			tomatch[i+1] = ""
		elif(i<=l-2 and tomatch[i].lower()=="greater" and tomatch[i+1].lower()=="than"):
			tomatch[i] = ">"
			tomatch[i+1] = ""
		elif(tomatch[i].lower()=="plus"):
			tomatch[i] = "+"
		elif(tomatch[i].lower()=="minus"):
			tomatch[i] = "-"
		elif(tomatch[i].lower()=="times" or tomatch[i].lower()=="into"):
			tomatch[i] = "*"
		elif(i<=l-2 and tomatch[i].lower()=="divided" and tomatch[i+1].lower()=="by"):
			tomatch[i] = "/"
			tomatch[i+1] = ""
		elif(tomatch[i].lower()=="modulo"):
			tomatch[i] = "%"
		elif(tomatch[i].lower()=="power"):
			tomatch[i] = "**"
	return lexer.clean(tomatch)
	
def expressionmatch(str):
	return (False,"")

def emptyline(str):
	if(str[0].rstrip()==""):
		return (True,"")
	return (False,"")
	
def parse(tabs,comma,str):
	str = macromatch(str)
	rules = [
				commentmatch(str),variabledeclarationmatch(str),
			 	classdeclarationmatch(str,comma),functiondeclarationmatch(str,comma),
			 	ifdeclarationmatch(str,comma),whiledeclarationmatch(str,comma),
			 	inputmatch(str), outputmatch(str), expressionmatch(str), emptyline(str)
			]
	l = len(rules)
	for i in xrange(0,l):
		res = rules[i]
		if(res[0]):
			return tabs*"\t"+res[1]	
	return None
