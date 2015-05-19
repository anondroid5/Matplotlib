# coding:utf-8
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# X軸データ
x = [datetime.datetime(2010,1,1),datetime.datetime(2010,1,2),
     datetime.datetime(2010,1,3),datetime.datetime(2010,1,4),
     datetime.datetime(2010,1,5)]

# Y軸データ
y = [1, 100, 2, 4, 1]

# データをセット
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)

# グラフのフォーマットの設定
days = mdates.DayLocator() #every day
daysFmt = mdates.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_locator(days)
ax.xaxis.set_major_formatter(daysFmt)
fig.autofmt_xdate()

#グラフのラベルを指定
ax.set_xlabel("Time") #x軸のラベル名(時間)
ax.set_ylabel("Tweet Counts") #y軸のラベル名(Tweet回数)

ax.legend(loc="upper right") #凡例を表示


plt.show()
