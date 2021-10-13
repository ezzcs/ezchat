import pyexcel
book = pyexcel.get_book(file_name="./test.ods")
sheet = book.sheet_by_index(0)
for row in sheet:
   print(row)
