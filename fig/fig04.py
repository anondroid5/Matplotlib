# coding:utf-8
import random
import dateutil.parser as parser
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot():
    #x軸のデータ格納
    x = ["00:00","00:30","01:00","01:30","02:00","02:30",
         "03:00","03:30","04:00","04:30","05:00","05:30",
         "06:00","06:30","07:00","07:30","08:00","08:30",
         "09:00","09:30","10:00","10:30","11:00","11:30",
         "12:00","12:30","13:00","13:30","14:00","14:30",
         "15:00","15:30","16:00","16:30","17:00","17:30",
         "18:00","18:30","19:00","19:30","20:00","20:30",
         "21:00","21:30","22:00","22:30","23:00","23:30"]

    #x軸のデータを取り出す
    xval = [parser.parse(xv) for xv in x]
    #y軸のデータを3~7までの乱数(48個)
    yval1 = [random.randint(3,7) for i in range(48)]
    #y軸のデータを4~9までの乱数(48個)
    yval2 = [random.randint(4,9) for i in range(48)]
    #y軸のデータを10~14までの乱数(48個)
    yval3 = [random.randint(5,11) for i in range(48)]


    #データをセット
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    #点を描画する際にマーカーの種類,線の種類,凡例の指定をする。
    ax.plot(xval,yval1,marker='o',linestyle="-",label="Japan vs Greece")
    ax.plot(xval,yval2,marker='s',linestyle="-",label="Japan vs Ivory Coast")
    ax.plot(xval,yval3,marker='^',linestyle="-",label="Japan vs Colombia")
    #y軸の表示範囲
    ax.set_ylim(0,12)
    # グラフのタイトルを設定
    ax.set_title("Bursty in Twitter Streams")
    #x軸のラベル
    ax.set_xlabel("Every 10 Seconds")
    #y軸のラベル
    ax.set_ylabel("Tweet Counts")
    #凡例表示
    ax.legend(loc="lower right")
    #グリッドを表示
    ax.grid()
    #グラフのフォーマットの設定
    days = mdates.AutoDateLocator()
    daysFmt = mdates.DateFormatter("%H:%M")
    ax.xaxis.set_major_locator(days)
    ax.xaxis.set_major_formatter(daysFmt)

    plt.show()
    plt.savefig("test.png")

    #plt.close()

if __name__=="__main__":
    plot()
    
