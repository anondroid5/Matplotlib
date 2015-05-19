# coding:utf-8

from pylab import *

axes(axisbg="#777777") # 背景を灰色に.
x = arange(-20, 20, 0.3)
plot(x+1, x, "b") # 青.
plot(x+2, x, "g") # 緑.
plot(x+3, x, "r") # 赤.
plot(x+4, x, "c") # シアン.
plot(x+5, x, "m") # マゼンタ.
plot(x+6, x, "y") # 黄.
plot(x+7, x, "k") # 黒.
plot(x+8, x, "w") # 白.
plot(x+9, x, color="#77ff77") # エメラルドグリーン.

legend(["blue", "green", "red", "cyan", "magenta", "yellow", "black", "white", "#77ff77"], "lower right")

xlim(2, 12)
ylim(-5, 5)

show()
