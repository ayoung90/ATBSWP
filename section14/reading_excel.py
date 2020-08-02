import openpyxl
import os

#download file from http://autbor.com/example.xlsx and place in 'C:\files'
filePath = 'C://files'
file = 'example.xlsx'
sheet = 'Sheet1'

#check the file & directory exists
try:
  os.chdir(filePath)
except FileNotFoundError:
  print('ERROR: Directory (' + filePath + ') Does not exist. Exiting')
  exit()


if not os.path.exists(file):
  print('ERROR: Directory (' + filePath + ') Does not exist. Exiting')
  exit()

workbook = openpyxl.load_workbook(file)
sheet = workbook[sheet]

print(sheet.values)

cellValue = sheet['A1'].value

print(cellValue)

colC = sheet['C']

print(colC)