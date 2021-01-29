#1 python3
# backupToZip.py - Copies an entire folder and its contents
# into a ZIP file whose filename increments
# enter input as 'backup folder_path'

import zipfile, os, sys, shutil

def backupToZip(folder):
    # backup the entire contents of the "folder" into ZIP

    folder = os.path.abspath(folder)

    # Figure out the filename this code should use based on
    # what files already exist

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    # TODO: Create the ZIP File
    print(f'Creating {zipFilename}')
    backupZip = zipfile.ZipFile(zipFilename,'w')

    # TODO: Walk the entire folder tree and compress files in each folder.
    for foldername, subfolder, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # Add the current folder to ZIP file.
        backupZip.write(foldername)

        # Add all files in this folder to ZIP file
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # preventing backup of backup files
            backupZip.write(os.path.join(foldername,filename))
    backupZip.close()
    shutil.move(str(zipFilename), 'D:\Backups')
    print('Done.')

if len(sys.argv) == 2 and os.path.isdir(sys.argv[1]):
    backupToZip(sys.argv[1])
else:
    print('Path does not exist')