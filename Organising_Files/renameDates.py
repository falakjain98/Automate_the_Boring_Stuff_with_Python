#1 python3
# ranameDates.py  - Renames filenames from American date
# format to European data format

import shutil, os, re

# Create regex that matches files with the American format
datePattern = re.compile(r"""^(.*?)  #all text before date
    ((0|1)?\d)-         # one or two digits for month
    ((0|1|2|3)?\d)-      # one or two digits for day
    ((19|20)\d\d)       # four digits for the year
    (.*?)$              #all text after the date
    """,re.VERBOSE)

# TODO: Loop over the files in the working directory
path = 'D:\Falak\Learning\Online Courses\Automate_the_Boring_Stuff_With_Python_Textbook\\automate_online-materials'
for amerFilename in os.listdir(path):
    mo = datePattern.search(amerFilename)
    # TODO: Skip files without a date
    if mo == None:
        continue

    # TODO: Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    
    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    # TODO: Get the full absolute paths
    absWorkingDir = os.path.abspath(path)
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    
    # TODO: Rename the files
    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    shutil.move(amerFilename,euroFilename) #uncomment after testing