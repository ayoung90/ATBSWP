import openpyxl
import os
import datetime

filePath = 'C://files'
file = 'test.xlsx'

try:
  os.chdir(filePath)
except FileNotFoundError as err:
  print('ERROR: Directory (' + filePath + ') Does not exist. Exiting')
  exit()

wb = openpyxl.Workbook()

print(wb)

#first sheet is always 'active'
sheet = wb.active

sheet['A1'] = 'Hello world2'

try:
  if os.path.exists(file):
    for i in range(0,100):
      file = file[0:4] + str(i) + '.xlsx'
      if not os.path.exists(file):
        break
  wb.save(file)
except:
  print('ERROR: Could not save (' + file + '). Exiting')