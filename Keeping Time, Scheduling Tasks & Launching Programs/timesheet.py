#! python3
# timesheet.py - Keeps track of entry time of individuals

import time, os, sys
from datetime import datetime
import pandas as pd

print('Press ENTER to begin. Then type name to record entry time. Press CTRL-C to quit.')
df = pd.DataFrame(columns=['Name','Entry Time'])
try:
    input() # press ENTER to begin
    print('Started')
except KeyboardInterrupt:
    print('Timesheet not started')
    sys.exit()

# Tracking entry times
try:
    while True:
        empName = str(input())
        entryTime = time.ctime()
        # entering record to dataframe
        df = df.append({'Name':empName,'Entry Time':entryTime}, ignore_index = True)
except KeyboardInterrupt:
    # Handling CTRL-C input from the user
    print('\nDone.')

dt = datetime.now()
path = os.getcwd()
filename = 'Entry Log ' + '-'.join(list([str(dt.day),str(dt.month),str(dt.year)])) + '.csv'
print(f'Saving timesheet as {filename}')
df.to_csv(path+'/'+filename,header= True,index=False)