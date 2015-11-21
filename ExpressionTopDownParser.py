def isOperator(token):
    return token in ['**','/','*','%','+','-','>=','>','<=','<','==','=']

def isAlpha(ch):
    ch = ch.lower()
    if(ch>='a' and ch<='z'):
        return True
    return False

def isNum(ch):
    if(ch>='0' and ch<='9'):
        return True
    return False

def isAlphaNum(ch):
    return isAlpha(ch) or isNum(ch)

def isVariable(token):
    if(isAlpha(ch)):
        for ch in token[1:]:
            if(not isAlphaNum(ch)):
                return False
        return True
    return False

def convToPostfix(infixtokens):
    opstack = []
    outputlist = []
    i = 0
    l = len(infixtokens)
    for i in xrange(0,l):
        if(isVariable(infixtokens[i])):
            outputlist.append(infixtokens[i])
        elif(infixtokens[i]=='('):
            opstack.append(infixtokens[i])
        elif(infixtokens[i]==')'):
           while(popstack[-1]!='('):
               outputlist.append(opstack[-1])
               opstack.pop()
        
