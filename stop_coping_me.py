# str = input('Hey how are you?\n')
# while str != "stop copying me":
#     print(str.upper())
#     str = input()

# with break
str = input('Hey how are you?\n')
while str != "stop copying me":
    print(str.upper())
    str = input()
    if str == "SHUT UP!":
        break
