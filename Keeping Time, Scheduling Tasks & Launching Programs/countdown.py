#! python3
# countdown.py - A simple countdown

import time,subprocess

timeLeft = int(input('Enter Countdown Duration: '))
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft -= 1

# Play sound file at end of countdown
subprocess.Popen(['start','alarm.wav'],shell = True)