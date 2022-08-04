# pip install openpyxl   - install module

import openpyxl  # excel manipulation module
import os

os.chdir('/Users/dayspring/Downloads/')

# create a workbook object by opening the xlsx file

workbook = openpyxl.load_workbook('example.xlsx')

# choose the sheet
sheet = workbook.get_sheet_by_name('Sheet1')

# find all the sheets in the workbook
workbook.get_sheet_names('example.xlsx')