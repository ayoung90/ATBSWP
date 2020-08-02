#create an exception
def div42by(divideBy):
  try:
    return 42 / divideBy
  except ZeroDivisionError:
    print('ERROR: Cannot divide by 0')

print(div42by(2))
print(div42by(12))
print(div42by(0))  # :)
print(div42by(2))

def catCounter():
  print('How many cats do you have? Please enter:')
  numCats = input()
  try:
    if int(numCats) >= 4:
      print('Thats too many cats!')
    else:
      print('That is an acceptable number of cats')
  except ValueError:
    print('ERROR: input was not a valid number')

catCounter()