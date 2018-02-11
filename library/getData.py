import xlrd

def getDatafromxls(xlspath):
    book = xlrd.open_workbook(xlspath)
    alldata = []
    sheet = book.sheet_by_index(0)
    filereader = sheet.nrows

    for row in range(1,filereader):

        alldata.append(sheet.row_values(row))

    return alldata
print(getDatafromxls('./data/user.xls'))





