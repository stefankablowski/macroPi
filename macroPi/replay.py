from keys import replay
from pynput.keyboard import Controller, Key
keyboard = Controller()

file = open("shortcuts.txt")
for line in file:
    line = str(line)
    line = line.strip()
    line = line.replace("'","")
    print(line)
    if len(line) < 2:
        keyboard.press(line)
        keyboard.release(line)
    else:
        keyboard.press(eval(line))
        keyboard.release(eval(line))