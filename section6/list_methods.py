spam = ['hey','howdy','hiya','hello']
print(spam)
print(spam.index('hiya'))

spam.append('hi')

spam.insert(0,'privet')
print(spam)

spam.remove('hello')

spam.sort()
print(spam)

spam2 = spam.copy()

spam.sort(reverse=True,key=str.lower)

print(spam)

spam2 = spam.copy()

spam2[2] = 'test'
print(spam)
print(spam2)