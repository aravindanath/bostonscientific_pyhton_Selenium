import openpyxl

path = "/Users/aravindanathdm/PycharmProjects/PythonSelenium/testData.xlsx"


wb_obj = openpyxl.load_workbook(path)

sheet_obj = wb_obj.active

cell_obj = sheet_obj.cell(1,1)
print(cell_obj.value)
