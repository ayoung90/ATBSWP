# This programs says hello and asks for my name

print('Hello world!')
print('What is your name?')
myName = input() #request name
print('It is good to meet you, ' + myName)
print('What is your age?') 
myAge = input() #request age
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

print('What would you like to do? (Bye)')
myInput = input()

if myInput == 'Bye':
  print('Ok. Bye ' + myName + ' (' + myAge + ')')
else:
  print('Sorry I dont understand: ' + myInput)