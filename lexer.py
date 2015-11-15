#!/usr/bin/env python
import sys

def tokenize(str):
	tokens = []
	iscomment = str.count('/')-str.lstrip('/').count('/')==2
	if(iscomment):
		return (0,0,['//',str.lstrip('/')])
				
	if(str.lstrip('\t').count('\t')>0):
		return (0,0,[])
	tabs = str.count('\t')
	str = str.lstrip('\t')

	endcomma = str.rstrip(',').endswith(',')
	str = str.rstrip(', ')
	
	tokens = str.split(' ')
	return (tabs,endcomma,tokens)
		
def clean(tokens):
	reserved = ["a","an","the","to"]
	newtokens = []
	for token in tokens:
		if(token in reserved):
			continue
		newtokens.append(token)
	return newtokens
	
def lexify(statement):
	tabs,endcomma,tokens = tokenize(statement)
	lexicaltokens = clean(tokens)
	return (tabs,endcomma,lexicaltokens)
