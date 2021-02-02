#! python3
# stopwatch.py - a stopwatch program

import time, sys

# Display the program's instructions
print('Press ENTER to begin. Thenm press ENTER again to "click" the stopwatch. Press CTRL-C to quit.')
try:
    input() # press ENTER to begin
    print('Started')
    start = time.time()
    last = start
    lapNum = 1
except KeyboardInterrupt:
    print('Stopwatch not started')
    sys.exit()

# Tracking lap times
try:
    while True:
        input()
        lapTime = round(time.time() - last,2)
        totalTime = round(time.time() - start,2)
        print(f' Lap {lapNum}: {lapTime} ({totalTime})',end = '')
        lapNum += 1
        last = time.time() # resetting last lap time
except KeyboardInterrupt:
    # Handling CTRL-C input from the user
    print('\nDone.')