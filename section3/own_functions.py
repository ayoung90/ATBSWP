def hello(name):
    print('Howdy ! ' + name)
    print('Howdy!!! ' + name)
    print('Hello there. ' + name + '\n')


def plusOne(number):
    return number + 1


hello('Adam')
hello('Steven')
hello('Sarah')

newNumber = plusOne(1)
print(newNumber)

# amend print to remove newline
print('Hello', end=' ')
print('World')
print('cat', 'dog', 'mouse')
print('cat', 'dog', 'mouse', sep=' - ')
