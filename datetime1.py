# Filename : test.py
# author by : www.runoob.com

# 引入 datetime 模块
import datetime

def getYesterday():
	today = datetime.date.today()
	oneday = datetime.timedelta
	yesterday = today - oneday(days=1)
	return yesterday


# 输出
print(getYesterday())