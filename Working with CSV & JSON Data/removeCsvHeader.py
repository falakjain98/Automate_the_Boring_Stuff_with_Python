#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current working directory

import csv, os

os.makedirs('removeCsvHeader/headerRemoved',exist_ok=True)

# Loop through every file in the current working directory
for csvFilename in os.listdir('./removeCsvHeader'):
    if not csvFilename.endswith('.csv'):
        continue #skipping non-csv files
    print('Removing header from ' + csvFilename + '...')

    # Read the CSV file in while skipping the first row
    csvRows = []
    csvFileObj = open('./removeCsvHeader/'+csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue #skipping the first row
        csvRows.append(row)
    csvFileObj.close()

    # Write out the csv file
    currentDir = os.getcwd()
    currentFileCSV = currentDir +"//" + 'removeCsvHeader' + '//' + 'headerRemoved' + '//' + csvFilename
    csvFileObj = open(currentFileCSV,'w',newline = '')
    csvWriter = csv.writer(csvFileObj)
    for rows in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()