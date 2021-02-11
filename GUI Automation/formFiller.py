#! python3
# formFiller.py - Automatically fills in the form

import pyautogui, time

submitAnotherLink = [190,350]

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
    'robocop': 4, 'comments': 'Tell Bob I said hi.'},
    {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
    'comments': 'n/a'},
    {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
    'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
    {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
    'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
    ]

for person in formData:
    # Chance to kill script
    print('>>> 3 Second pause to let user press ctrl-c <<<')
    time.sleep(3)

    print('Entering %s info...' % (person['name']))
    pyautogui.write(['\t','\t'])

    # Fill out the Name field
    pyautogui.write(person['name'] + '\t')

    # Greatest Fear field
    pyautogui.write(person['fear'] + '\t')

    # Source of Wizard Powers field
    if person['source'] == 'wand':
        pyautogui.write(['down',' ','\t'],0.5)
    elif person['source'] == 'amulet':
        pyautogui.write(['down','down',' ','\t'],0.5)
    elif person['source'] == 'crystal ball':
        pyautogui.write(['down','down','down',' ','\t'],0.5)
    elif person['source'] == 'money':
        pyautogui.write(['down','down','down','down',' ','\t'],0.5)

    # RoboCop field
    if person['robocop'] == 1:
        pyautogui.write([' ','\t','\t'],0.5)
    elif person['robocop'] == 2:
        pyautogui.write(['right','right','\t','\t'],0.5)
    elif person['robocop'] == 3:
        pyautogui.write(['right','right','right','\t','\t'],0.5)
    elif person['robocop'] == 4:
        pyautogui.write(['right','right','right','right','\t','\t'],0.5)
    elif person['robocop'] == 5:
        pyautogui.write(['right','right','right','right','right','\t','\t'],0.5)

    # Additional Comments field
    pyautogui.write(person['comments'] + '\t')

    # Submit
    time.sleep(0.5) # Waiting for button to activate
    pyautogui.press('Enter')

    # Wait until form page has loaded
    print('Submitted form.')
    time.sleep(3)

    # Click the Submit another response link
    pyautogui.click(submitAnotherLink[0],submitAnotherLink[1])