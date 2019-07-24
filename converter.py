print('How long did you sleep yesterday?')
hours = int(input())
minutes = hours * 60
seconds = minutes * 60
if hours > 9:
    print(f'You slept {hours} hours that is {minutes} minutes or {seconds} seconds. Maybe you overslept.')
elif hours < 6:
    print(f'You slept {hours} hours that is {minutes} minutes or {seconds} seconds. Recommended to sleep more.')
else:
    print(f'You slept {hours} hours that is {minutes} minutes or {seconds} seconds. Have a nice day)')
