import xlwings as xw
wb = xw.Book('testFiles/data1.xlsx')
wks = xw.sheets
print("Available sheets :", wks)
ws = wks[0]
val = ws.range("A1").value
print("A value in sheet1 :", val)

