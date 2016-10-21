from math import sin, cos, tan, asin, acos, atan
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import Graph, MeshLinePlot, MeshStemPlot


class CustomGraph(Graph):
    def __init__(self, **kwargs):
        super(CustomGraph, self).__init__(**kwargs)

        self.xlabel='X'
        self.ylabel='Y'
        self.x_ticks_minor=5
        self.x_ticks_major=25
        self.y_ticks_major=1
        self.y_grid_label=True
        self.x_grid_label=True
        self.padding=5
        self.x_grid=True
        self.y_grid=True
        self.xmin=-0
        self.xmax=100
        self.ymin=-5
        self.ymax=5

        #graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
        #    x_ticks_major=25, y_ticks_major=1,
        #    y_grid_label=True, x_grid_label=True, padding=5,
        #    x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-5, ymax=5)
        plot1 = MeshLinePlot(color=[1, 0, 0, 1])
        plot1.points = [(x, sin(x)) for x in range(0, 101)]
        plot2 = MeshLinePlot(color=[0, 1, 0, 1])
        plot2.points = [(x, cos(x)) for x in range(0, 101)]
        plot3 = MeshLinePlot(color=[0, 0, 1, 1])
        plot3.points = [(x, tan(x)) for x in range(0, 101)]
        self.add_plot(plot1)
        self.add_plot(plot2)
        self.add_plot(plot3)