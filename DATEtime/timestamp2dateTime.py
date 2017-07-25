# encoding: utf-8

"""
@version: python3.5.2 
@author: kaenlee  @contact: lichaolfm@163.com
@software: PyCharm Community Edition
@time: 2017/7/20 15:21
purpose:
"""
import datetime as dt
import time

print("maxDateTime", dt.datetime.max)
print("minDateTime", dt.datetime.min)
print("最小单位：", dt.datetime.resolution)

# today()
print(dt.datetime.today())
print(dt.datetime.now())  # 添加时区参数
print(dt.datetime.utcnow())
print(time.time(), type(time.time()))  # 返回一个时间戳

# 时间戳 转 datetime
print("timestamp2time", dt.datetime.fromtimestamp(time.time()))
print("timestamp2time", dt.datetime.utcfromtimestamp(time.time()))  # 时间戳转datetime
print("------", "timestamp2time", dt.datetime.fromtimestamp(30680))

# print(dt.datetime.time())

# combine
d = dt.date(2017, 12, 12)
t = dt.time(12, 12, 12)
print(d, t)
print(dt.datetime.combine(d, t))

# strptime
x = dt.datetime.strptime("2007-03-04 21:08:12", "%Y-%m-%d %H:%M:%S")
print(x)

# attris
print(x.year, x.month, x.day, x.hour, x.minute, x.second, x.microsecond,
      x.tzinfo, x.date(), x.time())
print(x.replace(year=2013))
print(x.timetuple())
print(x.utctimetuple())
print(x.toordinal(), x.weekday(), x.isocalendar())
print(x.strftime("%a"))

# timedelta
y = dt.datetime.now()
print(y -x, type(y-x))
print("yesterday", y - dt.timedelta(days=1))
print((x-y).days)

# date to str
print(str(y))

# local time : timestruct
print("localtime", time.localtime())
# dt.datetime.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# datetime 转 timestamp
a = "Sat Mar 28 22:24:24 2009"
b = time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))
print("b", b)

