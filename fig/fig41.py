# coding: utf-8
import wx
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.figure import Figure
from matplotlib.numerix import arange, sin, cos, pi


class NoRepaintCanvas(FigureCanvasWxAgg):
    """
    サイズ変更時に、２回onPaint()が呼ばれて、画面がちらつくので、
    それを抑制したキャンバスクラス
    """
    def __init__(self, *args, **kwargs):
        """
        初期化
        """
        FigureCanvasWxAgg.__init__(self, *args, **kwargs)
        self.__drawn = 0


    def _onPaint(self, evt):
        """
        描画イベント発生時時
        """
        if not self._isRealized:
            self.realize()
        if self.__drawn < 2:
            self.draw(repaint = False)
            self.__drawn += 1
        self.gui_repaint(drawDC=wx.PaintDC(self))

class PlotPanel(wx.Panel):
    """
    グラフ描画クラス（派生させて利用すること）
    """
    def __init__(self, parent, id = -1, color = None,\
                 dpi = None, style = wx.NO_FULL_REPAINT_ON_RESIZE, **kwargs):
        """
        初期化
        """
        wx.Panel.__init__(self, parent, id = id, style = style, **kwargs)
        self._figure = Figure(None, dpi)
        self.__canvas = NoRepaintCanvas(self, -1, self._figure)
        self.SetColor(color)
        self.Bind(wx.EVT_IDLE, self._onIdle)
        self.Bind(wx.EVT_SIZE, self._onSize)
        self.__resizeflag = True
        self.setSize()


    def SetColor(self, rgbtuple):
        """
        図形とキャンバスの色を設定する
        """
        if not rgbtuple:
            rgbtuple = wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE).Get()
        col = [c/255.0 for c in rgbtuple]
        self._figure.set_facecolor(col)
        self._figure.set_edgecolor(col)
        self.__canvas.SetBackgroundColour(wx.Colour(*rgbtuple))


    def _onSize(self, event):
        """
        サイズイベント発生時の処理
        """
        self.__resizeflag = True


    def _onIdle(self, evt):
        """
        アイドルイベント発生時の処理
        """
        if self.__resizeflag:
            self.__resizeflag = False
            self.setSize()
            self.draw()


    def setSize(self, pixels = None):
        """
        サイズを変更したい場合に呼び出す。
        強制的に描画させたい場合にも有効
        """
        if not pixels:
            pixels = self.GetClientSize()
        self.__canvas.SetSize(pixels)
        self._figure.set_size_inches(pixels[0]/self._figure.get_dpi(),
        pixels[1]/self._figure.get_dpi())


    def draw(self):
        """
        グラフ描画を行う
        """
        pass


class DemoPlotPanel(PlotPanel):
    """
    テスト用グラブ描画クラス
    """

    def draw(self):
        if not hasattr(self, 'subplot'):
            self.subplot = self._figure.add_subplot(111)

        theta = arange(0, 45*2*pi, 0.02)
        rad = (0.8*theta/(2*pi)+1)
        r = rad*(8 + sin(theta*7+rad/1.8))
        x = r*cos(theta)
        y = r*sin(theta)
        #Now draw it
        self.subplot.plot(x,y, '-r')
        #Set some plot attributes
        self.subplot.set_title("A polar flower (%s points)"%len(x), fontsize = 12)
        self.subplot.set_xlabel("test plot", fontsize = 8)
        self.subplot.set_xlim([-400, 400])
        self.subplot.set_ylim([-400, 400])


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    frame = wx.Frame(None, -1, 'WxPython and Matplotlib')
    panel = DemoPlotPanel(frame)

    sizer = wx.BoxSizer(wx.HORIZONTAL)
    panel.SetSizer(sizer)
    sizer.SetItemMinSize(panel, 300, 300)
    panel.Fit()
    panel.setSize()
    frame.Show()
    app.MainLoop()
