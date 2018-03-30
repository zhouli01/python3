
import calendar


yy=int(input("输入年份："))
mm=int(input("输入月份："))


print(calendar.month(yy,mm))
monthrange=calendar.monthrange(yy,mm)
print ("天数:",monthrange)