import xlrd
from xlutils.copy import copy
rb = xlrd.open_workbook("report.xls",formatting_info=True)

rs = rb.sheet_by_index(0) 

wb = copy(rb)

ws = wb.get_sheet(0)
ws.write(5,2,"差旅费")
wb.save("updated.xls")

