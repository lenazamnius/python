#print a pyramid
count = 1
while count < 8:
    print('*' * count)
    count += 1
print('\n')

#print a pyramid up side down
for num in range(8, 0, -1):
    print('*' * num)

# print a dimond

count = 1
indent = 11
while count < 12:
    print((' ' * int(indent / 2)) + ('*' * count))
    count += 2
    indent -= 2

indent = 2
for num in range(9, 0, -2):
    print((' ' * int(indent / 2)) + ('*' * num))
    indent += 2
