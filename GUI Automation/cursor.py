#! python3
# cursor.py - moves the cursor in at frequent intervals to prevent screen from becoming inactive

import pyautogui, time

try:
    while True:
        time.sleep(5)
        pyautogui.move(100,0,duration = 0.25)
        pyautogui.move(0,100,duration = 0.25)
        pyautogui.move(-100,0,duration = 0.25)
        pyautogui.move(0,-100,duration = 0.25)
except KeyboardInterrupt:
    # Handling CTRL-C input from the user
    print('\nDone.')
