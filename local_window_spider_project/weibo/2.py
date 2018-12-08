import xlwt

if __name__ == '__main__':
    with open('东方航空.csv','r') as f:
        data = f.readlines()
    for i in range(len(data)):
        data[i]= data[i].strip('\n').split(',')
    # for i in data:
        # print(i)
    # exit()
    book = xlwt.Workbook()
    sheet = book.add_sheet('春秋航空')
    # print(data[1])
    # exit()
    for i in range(len(data)):
        for j in range(len(data[i])):
            # print(data[i][j])
            sheet.write(i,j,data[i][j])
    book.save('东方航空.xls')