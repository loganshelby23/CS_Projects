import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import datetime
from xlrd import open_workbook
import matplotlib.dates as dates

folder = ("C:/Users/lgsh2/Desktop/Gaming Projects/OSRS_GE_Sheets")
loc = input('Input the name of the excel sheet to examine: ')

if not '/' in loc and not '.xlsx' in loc: 
    loc = '/' + loc + '.xlsx' 
elif not '/' in loc:
    loc = '/' + loc
elif not '.xlsx' in loc:
    loc = loc + '.xlsx'
else:
    pass

loc = folder + loc    
wb = open_workbook(loc)
sheet = wb.sheet_by_index(0)

columns = sheet.ncols
rows = sheet.nrows

xCoordinate = []
yCoordinate = []
x = np.linspace(0, rows, 1)
plt.xlabel('Date')
plt.ylabel('Price')
spotZero = 0
for i in range(columns):
    xCoordinate.append(sheet.cell_value(spotZero, i))
    j = 1
    for j in range(rows):
        yCoordinate.append(sheet.cell_value(j,i))
        print(sheet.cell_value(j,i))

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(xCoordinate, yCoordinate)
for xy in zip(xCoordinate,yCoordinate ):                                       
    ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
#plt.plot(xCoordinate, yCoordinate)
plt.show()


