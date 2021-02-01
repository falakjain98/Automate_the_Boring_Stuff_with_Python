#! python3
# convertToCsv.py - converts all xlsx files in directory to csv
# author: Falak Jain

import csv,openpyxl,os

for excelFile in os.listdir('./excelSpreadsheets'):
    # skip non-xlsx files
    if not excelFile.endswith('.xlsx'):
        continue
    print('Converting file ' + excelFile + ' from xlsx to csv...')

    wb = openpyxl.load_workbook('./excelSpreadsheets/'+excelFile)

    for sheetName in wb.get_sheet_names():
        sheet = wb.get_sheet_by_name(sheetName)

        # Create csv filename from the Excel filename and sheet title
        currentDir = os.getcwd()
        filename = currentDir + '//' + 'excelSpreadsheets' + '//' + 'convertedCsvs' + '//' + excelFile.rstrip('.xlsx') + '_' + sheetName + '.csv'

        # Create the csv.writer object for this Csv file
        csvFile = open(filename,'w',newline = '')
        csvWriter = csv.writer(csvFile)

        # Loop though every row in the sheet
        for rowNum in range(1,sheet.max_row+1):
            rowData = [] # apped each cell to this list
            # loop through each cell in the row
            for colNum in range(1,sheet.max_column+1):
                # Append each cell's data to rowData
                rowData.append(sheet.cell(row = rowNum,column = colNum).value)
            # Write the rowData list to the CSV file
            csvWriter.writerow(rowData)
        csvFile.close()