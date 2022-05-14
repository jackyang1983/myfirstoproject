import os.path

import xlrd


class ExcelUtil:
    # 构造函数传入excel文件路径，sheet名字
    def __init__(self, excel_file, sheet_name):
        self.excel_file = excel_file
        self.sheet_name = sheet_name

    def read_excel_to_list(self):
        workbook = xlrd.open_workbook(self.excel_file)
        worksheet = workbook.sheet_by_name(self.sheet_name)
        num_rows = worksheet.nrows
        data_list = []
        for rown in range(1, num_rows):
            xls_dict = {worksheet.cell_value(0, 0): worksheet.cell_value(rown, 0),
                        worksheet.cell_value(0, 1): worksheet.cell_value(rown, 1)}
            data_list.append(xls_dict)
        return data_list


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, 'data\\test_case.xls')
    XLS_List = ExcelUtil(DATA_DIR, 'Sheet1').read_excel_to_list()
    print(XLS_List)
