print('How long did you sleep yesterday?')
hours = int(input())
minutes = hours * 60
seconds = minutes * 60
part = 24 / hours
if hours:
    if hours > 9:
        print(f"You slept {hours} hours that is {minutes} minutes or {seconds} seconds. It's {part}th of the day. Maybe you overslept.")
    elif hours < 6:
        print(f"You slept {hours} hours that is {minutes} minutes or {seconds} seconds. It's {part}th of the day. Recommended to sleep more.")
    else:
        print(f"You slept {hours} hours that is {minutes} minutes or {seconds} seconds. It's {part}th of the day. Have a nice day)")
else:
    print('Enter whole number')
