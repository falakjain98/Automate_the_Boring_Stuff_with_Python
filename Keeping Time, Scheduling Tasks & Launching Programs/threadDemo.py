import threading, time
print('Start of Program.')

def TakeANap():
    time.sleep(5)
    print('Wake Up!')

threadObj = threading.Thread(target=TakeANap)
threadObj.start()

print('End of Program.')
