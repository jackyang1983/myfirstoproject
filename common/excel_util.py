import xlrd

class ExcelUtil:

    def __init__(self,excel_file,sheetname):
        self.excel_file = excel_file
        self.sheetname = sheetname

    def read_exceltolist(self):
        workbook = xlrd.open_workbook(self.excel_file)
        worksheet = workbook.sheet_by_name(self.sheetname)
        num_rows = worksheet.nrows
        num_cols = worksheet.ncols
        list = []
        for rown in range(1, num_rows):
                dict = {worksheet.cell_value(0, 0): worksheet.cell_value(rown, 0), worksheet.cell_value(0, 1): worksheet.cell_value(rown, 1)}
                list.append(dict)
        return list


if __name__ == '__main__':

    workbook1 = ExcelUtil('../data/test_case.xls','Sheet1').read_exceltolist()
    print(workbook1)
