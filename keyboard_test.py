import keyboard

while True:

    x = keyboard.read_key()

    if keyboard.read_key() == "w":
        print("going forward")
    elif keyboard.read_key() == "s":
        print('going back')
    else:
        print('Quitting')
        break
