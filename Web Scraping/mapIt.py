#! python3
# mapIt.py - Launches a map in the brower using an address 
# from the command line or clipboard

import webbrowser,sys
import pyperclip
if len(sys.argv) > 1:
    # get address from command line
    address = ' '.join(sys.argv[1:])

# Get address from clipboard
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address)
