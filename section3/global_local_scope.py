spam = 42 # global variable

def printSpam():
  print('Spam = ' + str(spam))

def eggs():
  spam = 42 # local variable
  return spam

print('example xyz')

def Spam():
  eggs = 99
  bacon()
  print(eggs)

def bacon():
  ham = 101
  eggs = 0

def assignSpam(var):
  global spam 
  spam = var

Spam()

printSpam()
assignSpam(25)
printSpam()