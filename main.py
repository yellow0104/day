import datetime

inp_start = input('사귄일 예:2022/8/1>')
inp_end = input('지금/끝난일 예:2022/8/2>')

date1 = datetime.date(int(inp_start.split('/')[0]), int(inp_start.split('/')[1]), int(inp_start.split('/')[2]))
date2 = datetime.date(int(inp_end.split('/')[0]), int(inp_end.split('/')[1]), int(inp_end.split('/')[2]))
diff = date2 - date1

print(diff.days)
