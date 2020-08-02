spam = ['cat', 'bat', 'rat', 'elephant']

print(spam[2])

spam2 = [['fish', 'shark'], 'bat', 'rat', 'elephant']

print(spam2[0])
print(spam2[0][1])

spam[2:4] = ['CAT', 'MOOSE', 'BEAR']
print(spam)

del spam[2]

print(spam)

print('MOOSE' in spam)

# Iterate over lists by item or index
for item in spam:
    print(item)

for i in range(0, len(spam)):
    print(spam[i])

print(len(spam))

cat = ['fat', 'orange', 'loud']

size, color, disposition = cat

print(size)
print(color)
print(disposition)

# swap variables
a = 'AAA'
b = 'BBB'

a, b = b, a

print(a)
print(b)