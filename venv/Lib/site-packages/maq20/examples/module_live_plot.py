"""
This example uses pyqtgraph library.

Live plots all channels in a module.

Improvements:
    - Make this a class so it can be used as a widget for PyQT.
    - Give a choice of what channels we want to plot.

Notes:
    - Change the string passed to maq20.find() to use another module.
    - Add more pens if a module with more than 16 channels is to be used.
"""
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from maq20 import MAQ20

win = pg.GraphicsWindow()
win.setWindowTitle('Live graph MAQ20 Module')
pg.setConfigOptions(antialias=True)

maq20 = MAQ20(ip_address="192.168.128.100", port=502)
a_module = maq20.find('VDN')
if a_module is None:
    raise AttributeError("Module not found")
plots = []
curves = []
data = []

pens = [
    (255, 255, 255),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (0, 255, 255),
    (255, 0, 255),
    (100, 255, 50),
    (255, 255, 255),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (0, 255, 255),
    (255, 0, 255),
    (100, 255, 50),
]  # Used to draw the graphs in color.

for i in range(a_module.get_number_of_channels()):
    plots.append(win.addPlot(title="Channel " + str(i)))
    plots[i].showGrid(x=True, y=True)
    curves.append(plots[i].plot(pen=pens[i]))
    data.append([])
    if i % 2 == 1:
        win.nextRow()


def update():
    global a_module, curves, data
    for i in range(len(curves)):
        if len(data[0]) > 100:
            for d in data:
                del d[0]
        data[i].append(a_module[i])
        curves[i].setData(data[i])


timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)

"""Start Qt event loop unless running in interactive mode or using pyside."""
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
