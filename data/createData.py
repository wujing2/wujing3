import xlwt

wb = xlwt.Workbook()
ws = wb.add_sheet('wujing')
title = ['username','passwd','status','asserText']

data = [
    ['xiaoming', '121231212', '失败', '用户名或密码错误'],
    ['helloworld', '123456', '成功', 'helloworld']
    ]
for i in range(len(title)):
    print(0,i,title[i])
    ws.write(0,i,title[i])

for x in range(len(data)):
    # print(x+1,data[x])
    for y in range(len(data[x])):
        print(x+1,y,data[x][y])
        ws.write(x+1,y,data[x][y])

wb.save('user.xls')
