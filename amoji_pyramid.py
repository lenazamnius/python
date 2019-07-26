# print a pyramid
count = 1
while count < 8:
    print('\U0001f600' * count)
    count += 2
print('\n')

# print a pyramid up side down
for num in range(8, 0, -1):
    print('\U0001f600' * num)

# print a dimond

count = 1
indent = 12
while count < 11:
    print((' ' * int(indent / 2)) + ('*' * count))
    count += 2
    indent -= 2

indent = 2
for num in range(11, 0, -2):
    print((' ' * int(indent / 2)) + ('*' * num))
    indent += 2
