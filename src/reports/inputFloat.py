import xlrd
import xlwt
from xlutils.copy import copy
rb = xlrd.open_workbook("report.xls",formatting_info=True)

rs = rb.sheet_by_index(0) 

wb = copy(rb)

ws = wb.get_sheet(0)



def writeAccountValue(value,location):
    Style = xlwt.XFStyle()
#    Font = xlwt.Font()
#    Font.name = '微软雅黑'
#    Font.bold = False
#    Font.height = 18 * 20
#    Style.font = Font
    Borders = xlwt.Borders()
    Borders.top = xlwt.Borders.THIN
    Borders.bottom = xlwt.Borders.THIN
    Borders.left = xlwt.Borders.THIN
    Borders.right = xlwt.Borders.THIN
    Style.borders = Borders
    Alignment = xlwt.Alignment()
    Alignment.horz = xlwt.Alignment.HORZ_CENTER
    Alignment.Vert = xlwt.Alignment.VERT_CENTER
    Style.alignment = Alignment



    valueString = str(value)
    sheetRow = location[0]
    sheetColumn = location[1]
    valueCheck = valueString.split('.')
    if len(valueCheck)==1 :
        loopCount = len(valueCheck[0])
        for num in range(0,loopCount):
            valueChar = valueCheck[0][loopCount-num-1]
            ws.write(sheetRow,sheetColumn-num,int(valueChar),Style)
    if len(valueCheck)==2 :
        loopCount = len(valueCheck[0])
        for num in range(0,loopCount):
            valueChar = valueCheck[0][loopCount-num-1]
            ws.write(sheetRow,sheetColumn-num-2,int(valueChar),Style)
        loopCount = len(valueCheck[1])
        for num in range(0,loopCount):
            valueChar = valueCheck[1][loopCount-num-1]
            ws.write(sheetRow,sheetColumn-num,int(valueChar),Style)



account_value = 32344.55
account_value_location = [5,24]
writeAccountValue(account_value,account_value_location)
wb.save("./updated.xls")

