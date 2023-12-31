# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interpolation_Task1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QSlider
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import pylab as pl
from pylab import cm
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
import numpy as np
from matplotlib.figure import Figure
from scipy import signal
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from pyqtgraph import PlotWidget
from numpy import reshape, linspace, around
from sympy import S, symbols, printing
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import math


class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None, dpi=100):
        fig = Figure(dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MatplotlibCanvas, self).__init__(fig)
        fig.tight_layout()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1241, 987)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_main_window = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_main_window.setObjectName("horizontalLayout_main_window")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_for_EqnsandError= QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_for_EqnsandError.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_for_EqnsandError.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_for_EqnsandError.setSpacing(5)
        self.horizontalLayout_for_EqnsandError.setObjectName("horizontalLayout_for_Equations")

        self.verticalLayout_fitting_equations = QtWidgets.QVBoxLayout()
        self.verticalLayout_fitting_equations.setObjectName("verticalLayout_fitting_equations")
        self.fitting_equation_label = QtWidgets.QLabel(self.layoutWidget)
        self.fitting_equation_label.setObjectName("fitting_equation_label")
        self.verticalLayout_fitting_equations.addWidget(self.fitting_equation_label)

        self.verticalLayoutWidget_main_window = QtWidgets.QWidget(self.layoutWidget)
        self.verticalLayoutWidget_main_window.setGeometry(QtCore.QRect(10, 50, 1500, 500))
        self.verticalLayoutWidget_main_window.setObjectName("verticalLayoutWidget_main_window")

        self.horizontalLayout_for_EqnsandError.addLayout(self.verticalLayout_fitting_equations)
        self.verticalLayout_error = QtWidgets.QVBoxLayout()
        self.verticalLayout_error.setObjectName("verticalLayout_error")
        self.percentage_error_label = QtWidgets.QLabel(self.layoutWidget)
        self.percentage_error_label.setObjectName("percentage_error_label")
        self.verticalLayout_error.addWidget(self.percentage_error_label)
        self.horizontalLayout_for_EqnsandError.addLayout(self.verticalLayout_error)
        self.main_widget = QtWidgets.QWidget(self.splitter)
        self.main_widget.setObjectName("main_widget")
        self.verticalLayout_for_maingraph = QtWidgets.QVBoxLayout(self.main_widget)
        self.verticalLayout_for_maingraph.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_for_maingraph.setObjectName("verticalLayout_for_maingraph")
        self.verticalLayout_for_main_graph = QtWidgets.QVBoxLayout()
        self.verticalLayout_for_main_graph.setObjectName("verticalLayout_for_main_graph")
        self.graph_label = QtWidgets.QLabel(self.main_widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setBold(True)
        font.setWeight(75)
        self.graph_label.setFont(font)
        self.graph_label.setObjectName("graph_label")
        self.verticalLayout_for_main_graph.addWidget(self.graph_label)
        self.horizontalLayout_maingraph = QtWidgets.QHBoxLayout()
        self.horizontalLayout_maingraph.setObjectName("horizontalLayout_maingraph")
        self.signal_fig = Figure()
        self.figure_canvas_genSig = FigureCanvas(self.signal_fig)
        self.horizontalLayout_maingraph.addWidget(self.figure_canvas_genSig)
        genAxis = self.signal_fig.gca()
        genAxis.cla()
        self.verticalLayout_mainsig_parameters = QtWidgets.QVBoxLayout()
        self.verticalLayout_mainsig_parameters.setObjectName("verticalLayout_mainsig_parameters")
        self.verticalLayout_for_numofchunks = QtWidgets.QVBoxLayout()
        self.verticalLayout_for_numofchunks.setObjectName("verticalLayout_for_numofchunks")
        self.No_of_chunks_label = QtWidgets.QLabel(self.main_widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setBold(True)
        font.setWeight(75)
        self.No_of_chunks_label.setFont(font)
        self.No_of_chunks_label.setObjectName("label")
        self.verticalLayout_for_numofchunks.addWidget(self.No_of_chunks_label)
        self.No_of_chunks_lineEdit = QtWidgets.QLineEdit(self.main_widget)
        self.No_of_chunks_lineEdit.setObjectName("No_of_chunks_lineEdit")
        self.verticalLayout_for_numofchunks.addWidget(self.No_of_chunks_lineEdit)
        self.verticalLayout_mainsig_parameters.addLayout(self.verticalLayout_for_numofchunks)
        self.verticalLayout_for_fitting_order = QtWidgets.QVBoxLayout()
        self.verticalLayout_for_fitting_order.setObjectName("verticalLayout_for_fitting_order")
        self.fitting_order_lable = QtWidgets.QLabel(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.fitting_order_lable.sizePolicy().hasHeightForWidth())
        self.fitting_order_lable.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setBold(True)
        font.setWeight(75)
        self.fitting_order_lable.setFont(font)
        self.fitting_order_lable.setObjectName("fitting_order_lable")
        self.verticalLayout_for_fitting_order.addWidget(self.fitting_order_lable)
        self.fitting_order_lineEdit = QtWidgets.QLineEdit(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fitting_order_lineEdit.sizePolicy().hasHeightForWidth())
        self.fitting_order_lineEdit.setSizePolicy(sizePolicy)
        self.fitting_order_lineEdit.setObjectName("fitting_order_lineEdit")
        self.verticalLayout_for_fitting_order.addWidget(self.fitting_order_lineEdit)
        self.verticalLayout_mainsig_parameters.addLayout(self.verticalLayout_for_fitting_order)
        self.verticalLayout_clipping_percentage = QtWidgets.QVBoxLayout()
        self.verticalLayout_clipping_percentage.setObjectName("verticalLayout_clipping_percentage")
        self.clipping_label = QtWidgets.QLabel(self.main_widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.clipping_label.setFont(font)
        self.clipping_label.setLineWidth(-1)
        self.clipping_label.setObjectName("clipping_label")
        self.verticalLayout_clipping_percentage.addWidget(self.clipping_label)
        self.clipping_percentage_spinBox = QtWidgets.QSpinBox(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clipping_percentage_spinBox.sizePolicy().hasHeightForWidth())
        self.clipping_percentage_spinBox.setSizePolicy(sizePolicy)
        self.clipping_percentage_spinBox.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.clipping_percentage_spinBox.setMinimum(1)
        self.clipping_percentage_spinBox.setMaximum(100)
        self.clipping_percentage_spinBox.setObjectName("clipping_percentage_spinBox")
        self.verticalLayout_clipping_percentage.addWidget(self.clipping_percentage_spinBox)
        self.verticalLayout_mainsig_parameters.addLayout(self.verticalLayout_clipping_percentage)
        self.horizontalLayout_maingraph.addLayout(self.verticalLayout_mainsig_parameters)
        self.verticalLayout_for_main_graph.addLayout(self.horizontalLayout_maingraph)
        self.verticalLayout_for_maingraph.addLayout(self.verticalLayout_for_main_graph)
        self.verticalLayout_ErrorMap = QtWidgets.QVBoxLayout()
        self.verticalLayout_ErrorMap.setObjectName("verticalLayout_ErrorMap")
        self.error_map_label = QtWidgets.QLabel(self.main_widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setBold(True)
        font.setWeight(75)
        self.error_map_label.setFont(font)
        self.error_map_label.setObjectName("error_map_label")
        self.verticalLayout_ErrorMap.addWidget(self.error_map_label)
        self.horizontalLayout_map = QtWidgets.QHBoxLayout()
        self.horizontalLayout_map.setObjectName("horizontalLayout_map")
        self.error_map_fig = Figure()
        self.error_map_canvas = FigureCanvas(self.error_map_fig)
        self.horizontalLayout_map.addWidget(self.error_map_canvas)
        self.verticalLayout_mapAxes = QtWidgets.QVBoxLayout()
        self.verticalLayout_mapAxes.setObjectName("verticalLayout_mapAxes")
        self.verticalLayout_for_map_xaxis = QtWidgets.QVBoxLayout()
        self.verticalLayout_for_map_xaxis.setObjectName("verticalLayout_for_map_xaxis")
        self.choose_x_axis_label = QtWidgets.QLabel(self.main_widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setBold(True)
        font.setWeight(75)
        self.choose_x_axis_label.setFont(font)
        self.choose_x_axis_label.setObjectName("choose_x_axis_label")
        self.verticalLayout_for_map_xaxis.addWidget(self.choose_x_axis_label)
        self.comboBox_Xaxis = QtWidgets.QComboBox(self.main_widget)
        self.comboBox_Xaxis.setObjectName("comboBox_Xaxis")
        self.comboBox_Xaxis.addItem("")
        self.comboBox_Xaxis.addItem("")
        self.comboBox_Xaxis.addItem("")
        self.comboBox_Xaxis.addItem("")
        self.verticalLayout_for_map_xaxis.addWidget(self.comboBox_Xaxis)
        self.verticalLayout_mapAxes.addLayout(self.verticalLayout_for_map_xaxis)
        self.verticalLayout_for_map_yaxis = QtWidgets.QVBoxLayout()
        self.verticalLayout_for_map_yaxis.setObjectName("verticalLayout_for_map_yaxis")
        self.choose_y_axis_label = QtWidgets.QLabel(self.main_widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setBold(True)
        font.setWeight(75)
        self.choose_y_axis_label.setFont(font)
        self.choose_y_axis_label.setObjectName("choose_y_axis_label")
        self.verticalLayout_for_map_yaxis.addWidget(self.choose_y_axis_label)
        self.comboBox_Yaxis = QtWidgets.QComboBox(self.main_widget)
        self.comboBox_Yaxis.setObjectName("comboBox_Yaxis")
        self.comboBox_Yaxis.addItem("")
        self.comboBox_Yaxis.addItem("")
        self.comboBox_Yaxis.addItem("")
        self.comboBox_Yaxis.addItem("")
        self.verticalLayout_for_map_yaxis.addWidget(self.comboBox_Yaxis)
        self.verticalLayout_mapAxes.addLayout(self.verticalLayout_for_map_yaxis)
        self.verticalLayout_for_map_progressbar = QtWidgets.QVBoxLayout()
        self.verticalLayout_for_map_progressbar.setObjectName("verticalLayout_for_map_progressbar")
        self.generate_error_map_button = QtWidgets.QPushButton(self.main_widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.generate_error_map_button.setFont(font)
        self.generate_error_map_button.setObjectName("generate_error_map_button")
        self.verticalLayout_for_map_progressbar.addWidget(self.generate_error_map_button)
        self.progressBar = QtWidgets.QProgressBar(self.main_widget)
        self.progressBar.move(40,80)
        self.progressBar.setMaximum(100)
        self.progressBar.hide()
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_for_map_progressbar.addWidget(self.progressBar)
        self.verticalLayout_mapAxes.addLayout(self.verticalLayout_for_map_progressbar)
        self.horizontalLayout_map.addLayout(self.verticalLayout_mapAxes)
        self.verticalLayout_ErrorMap.addLayout(self.horizontalLayout_map)
        self.verticalLayout_for_maingraph.addLayout(self.verticalLayout_ErrorMap)
        self.horizontalLayout_main_window.addWidget(self.splitter)
        self.timer=QtCore.QTimer()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1241, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.verticalLayout_for_fitting_eqns = QtWidgets.QVBoxLayout()
        self.verticalLayout_for_fitting_eqns.setObjectName("verticalLayout_for_fitting_eqns")
        self.overlap_percentage_lable = QtWidgets.QLabel(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.overlap_percentage_lable.sizePolicy().hasHeightForWidth())
        self.overlap_percentage_lable.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setBold(True)
        font.setWeight(75)
        self.overlap_percentage_lable.setFont(font)
        self.overlap_percentage_lable.setObjectName("overlap_percentage_lable")
        self.verticalLayout_for_fitting_eqns.addWidget(self.overlap_percentage_lable)
        self.overlap_percentage_lineEdit = QtWidgets.QLineEdit(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.overlap_percentage_lineEdit.sizePolicy().hasHeightForWidth())
        self.overlap_percentage_lineEdit.setSizePolicy(sizePolicy)
        self.overlap_percentage_lineEdit.setObjectName("overlap_percentage_lineEdit")
        self.verticalLayout_for_fitting_eqns.addWidget(self.overlap_percentage_lineEdit)
        self.verticalLayout_mainsig_parameters.addLayout(self.verticalLayout_for_fitting_eqns)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.fitted_equations = plt.Figure()
        self.figure_canvas_fit = FigureCanvas(self.fitted_equations)
        self.verticalLayout_fitting_equations.addWidget(self.figure_canvas_fit)

        self.error_equations = Figure()
        self.figure_canvas_error = FigureCanvas(self.error_equations)
        self.verticalLayout_error.addWidget(self.figure_canvas_error)


        self.actionOpen.triggered.connect(lambda: self.get_file())
        self.No_of_chunks_lineEdit.textChanged.connect(lambda: self.Interpolate())
        self.fitting_order_lineEdit.textChanged.connect(lambda: self.Interpolate())
        self.clipping_percentage_spinBox.valueChanged.connect(lambda: self.extrapolate())
        self.generate_error_map_button.clicked.connect(self.toggle_button)
        self.movement=0
        self.time_col = []
        self.amp_col = []
        self.comboBox_Xaxis.activated.connect(self.updateText)
        self.comboBox_Yaxis.activated.connect(self.updateText)

    def updateText(self):
        self.currentIndex(self.comboBox_Xaxis.currentIndex(), self.comboBox_Yaxis.currentIndex())

    def currentIndex(self, x, y):
        sum = x + y
        dic_labels = {bool(sum == 3): "overlapping between chunks", bool(sum == 4): "The order of the fitting polynomial", bool(sum == 5): "Number of chunks"}
        return self.overlap_percentage_lable.setText(dic_labels.get(True))


    def get_file(self):
        self.fileName = QFileDialog.getOpenFileName(filter="CSV (*.csv)")[0]
        data_frame = pd.read_csv(self.fileName)
        self.time_col = data_frame.values[:, 0]
        self.amp_col = data_frame.values[:, 1]
        self.plot()

    def plot(self):
        genAxis = self.signal_fig.gca()
        genAxis.cla()
        genAxis.grid(True)
        genAxis.plot(self.time_col, self.amp_col,color ="red")
        self.figure_canvas_genSig.draw()
        self.figure_canvas_genSig.flush_events()


    def get_num_of_shunks(self):
        if self.No_of_chunks_lineEdit.text() != "":
            self.No_of_shunks = self.No_of_chunks_lineEdit.text()
        return int(self.No_of_shunks)

    def get_fitting_order(self):
        if self.fitting_order_lineEdit.text() != "":
            self.order = self.fitting_order_lineEdit.text()
        return int(self.order)

    def Interpolate(self):
        if (self.fitting_order_lineEdit.displayText()!="" or self.No_of_chunks_lineEdit.displayText()!=""):
            genAxis = self.signal_fig.gca()
            genAxis.cla()
            self.fitted_equations.clear()
            self.error_equations.clear()
            self.shunks = self.get_num_of_shunks()
            self.Shunked_Time = np.array_split(self.time_col, self.shunks)
            self.Shunked_Amp = np.array_split(self.amp_col, self.shunks)
            self.poly_order = self.get_fitting_order()
            self.plot()
            self.Amp_values = []
            self.equation_list = []
            self.prec_error = []
            self.maperror_arr = []
            for i in range(0, self.shunks):
                x=symbols("x")
                self.poly_coef = np.polyfit(self.Shunked_Time[i], self.Shunked_Amp[i], self.poly_order)    # coefficients of the polynomial function
                poly_function = np.poly1d(self.poly_coef)
                self.parameters_list=list(poly_function)
                self.Amp_values.append(poly_function(self.Shunked_Time[i]))
                genAxis.plot(self.Shunked_Time[i], poly_function(self.Shunked_Time[i]), color="blue",linestyle='dashed')
                poly= sum(S("{:6.2f}".format(v))* x ** i for i,v in enumerate(self.poly_coef[::-1]))
                self.eq_latex= printing.latex(poly)
                self.lable="${}$".format(self.eq_latex)
                self.equation_list.append(self.lable)
                self.y_dim = 1
            for i in range(0, self.shunks):
                self.y_dim -= 0.08
                self.fitted_equations.text(0.01,self.y_dim+0.01,"Function of shunk no  "+str(i+1)+"--->  "+self.equation_list[i])

            self.error_array = []
            for x in range(0, self.shunks):
                Error = self.avg_shunk(self.Shunked_Amp[x], self.Amp_values[x])
                self.error_array.append(Error)
            self.percentage_Error = np.mean(self.error_array)
            self.prec_error.append(self.percentage_Error)

            self.error_equations.text(0.02, 0.8, r'$Error = \frac{1}{N} \sum_{k=0}^{k={N-1}} \frac{Y_{true}(k)-Y_{calculated}(k)}{Y_{true}(k)}$')
            self.error_equations.text(0.02,0.5,"Percentage Error  "+"--->  "+str(self.percentage_Error) +"  %")

        else:
            self.No_of_chunks_lineEditlineEdit.clear()
            self.fitting_order_lineEdit.clear()
            self.signal_fig.clear()
            self.plot()
            self.error_equations.clear()
            self.error_equations.text(0.02, 0.5,"There is no input in 'no of chunks or no of order'")
            self.fitted_equations.clear()
            self.fitted_equations.text(0.02, 0.5, "There is no input in 'no of chunks or no of order'")
        self.figure_canvas_error.draw()
        self.figure_canvas_error.flush_events()
        self.figure_canvas_genSig.draw()
        self.figure_canvas_genSig.flush_events()
        self.figure_canvas_fit.draw()
        self.figure_canvas_fit.flush_events()

    def avg_shunk(self, old_sh, new_sh):
        arr_error = self.calc_Error(old_sh, new_sh)
        return np.mean(arr_error)

    def calc_Error(self, old_shunk, new_shunk):
        Error_array = []
        for i in range(0, len(old_shunk)):
            Error = abs((old_shunk[i] - new_shunk[i]) / old_shunk[i]) * 100
            Error_array.append(Error)
        # print(Error_array)
        return Error_array

    def extrapolate(self):
        self.clearing()
        genAxis = self.signal_fig.gca()
        genAxis.cla()
        self.plot()
        self.portion = int(self.get_portionofsignal())
        self.poly_order = self.get_fitting_order()
        new_size = int(len(self.time_col) * self.portion / 100)
        self.newTime = self.time_col[:new_size]
        self.newAmp = self.amp_col[:new_size]
        self.poly_coef = np.polyfit(self.newTime, self.newAmp, self.poly_order)
        self.poly_function = np.poly1d(self.poly_coef)
        genAxis.plot(self.time_col, self.poly_function(self.time_col),color="green", linestyle='dashed')
        self.figure_canvas_genSig.draw()
        self.figure_canvas_genSig.flush_events()

    def get_portionofsignal(self):
        signal_portion = self.clipping_percentage_spinBox.value()
        return signal_portion

    def clearing(self):
        self.fitted_equations.clear()
        self.figure_canvas_fit.draw()
        self.figure_canvas_fit.flush_events()
        self.error_equations.clear()
        self.figure_canvas_error.draw()
        self.figure_canvas_error.flush_events()

    def overlap(self,time_chunks,overlap):
        overlaped_chunks=[time_chunks[0]]
        for chunk_number in range(1,len(time_chunks)):
            num_of_elements = int(overlap*len(time_chunks[chunk_number]))*chunk_number
            chunkx_new=[]
            for x in (time_chunks[chunk_number]):
                 xnew=x-num_of_elements
                 chunkx_new.append(xnew)
            overlaped_chunks.append( chunkx_new)
        return overlaped_chunks

    def calculate_error_map(self,number_of_chunks,order_of_polynomial,overlap):
        time_chunks = np.array_split(self.time_col,number_of_chunks)
        time_chunks = self.overlap(time_chunks,overlap)
        amp_chunks=np.array_split(self.amp_col, number_of_chunks)
        error_for_all_chunks=[]
        for chunk_number in range(len(time_chunks)):
            self.poly_coef = np.polyfit(time_chunks[chunk_number],amp_chunks[chunk_number],order_of_polynomial)
            y_fitting_list=[]
            error_for_each_chunk=[]
            for x in (time_chunks[chunk_number]):
                 index_x = list(time_chunks[chunk_number]).index(x)
                 y_fitting=0

                 for i in range(len( self.poly_coef)):
                     y_fitting+=self.poly_coef[i]*(x**(order_of_polynomial-i))
                 error_for_each_point=(y_fitting-amp_chunks[chunk_number][index_x])**2
                 error_for_each_chunk.append(error_for_each_point)
                 y_fitting_list.append( y_fitting)
            error_for_each_chunk=math.sqrt((sum(error_for_each_chunk)/len(time_chunks[chunk_number])))
            error_for_all_chunks.append( error_for_each_chunk)
        return (sum(error_for_all_chunks)/number_of_chunks)


    def Generate_error_map(self):
        self.error_map_fig.clf()
        self.axes = self.error_map_fig.gca()
        rows, cols = 5,5
        x=self.comboBox_Xaxis.currentIndex()
        y= self.comboBox_Yaxis.currentIndex()
        overlap_list=np.arange(0,30,5)
        print(overlap_list)
        print(len(overlap_list))
        self.overlap_percentage = int(self.overlap_percentage_lineEdit.text())
        arr=[]
        for i in range(rows):
           col = []
           for j in range( cols):
               dic={bool(x==1 and y==2):self.calculate_error_map(j+1,i+1,self.overlap_percentage/100),bool( x==2 and y==1):self.calculate_error_map(i+1,j+1,self.overlap_percentage/100),bool(x==3 and y==1):self.calculate_error_map(i+1,self.overlap_percentage,overlap_list[j]/100),bool( x==1 and y==3):self.calculate_error_map(j+1,self.overlap_percentage,overlap_list[i]/100),bool( x==3 and y==2):self.calculate_error_map(self.overlap_percentage,i+1,overlap_list[j]/100),bool( x==2 and y==3):self.calculate_error_map(self.overlap_percentage,j+1,overlap_list[i]/100)}
               a=dic.get(True)
               col.append(a)

           arr.append(col)

        self.canv = self.axes.imshow(np.array(arr), interpolation = 'nearest',cmap="inferno", aspect='auto', extent = [0.5,5.5,0.5,5.5],origin="lower")
        pl.colorbar(self.canv , ax= self.axes)

        self.error_map_canvas.draw()
        self.error_map_canvas.flush_events()

        if self.comboBox_Xaxis.currentIndex()==3:
            self.axes.set_xticklabels(['0','5','10','15','20','25'])
        else:
            self.axes.set_xticks(np.arange(1,cols+1))

        if self.comboBox_Yaxis.currentIndex()==3:
            self.axes.set_yticklabels(['0','5','10','15','20','25'])
        else:
            self.axes.set_yticks(np.arange(1,rows+1))

        self.generate_error_map_button.setText("Generate Error Map")
        self.generate_error_map_button.setStyleSheet("background-color : lightgreen")


    def toggle_button(self):
        if self.generate_error_map_button.text() == "Generate Error Map":
            self.progressBar.setVisible(True)
            self.progressBar.setValue(0)
            self.timer.start(30)
            self.timer.timeout.connect(self.update_progressbar)
        else:
            self.timer.stop()
            self.progressBar.setVisible(False)
            self.generate_error_map_button.setText("Generate Error Map")
            self.generate_error_map_button.setStyleSheet("background-color : lightgreen")
            self.error_map_fig.clear()
            self.error_map_canvas.draw()
            self.error_map_canvas.flush_events()

    def update_progressbar(self):
        self.progressBar.setValue(self.progressBar.value() + 1)
        self.generate_error_map_button.setText("cancel")
        self.generate_error_map_button.setStyleSheet("background-color : red")
        if self.progressBar.value() == 100:
            self.Generate_error_map()
            self.progressBar.setVisible(False)
            self.timer.stop()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fitting_equation_label.setText(_translate("MainWindow", "The fitting equation"))
        self.percentage_error_label.setText(_translate("MainWindow", "Percentage Error"))
        self.graph_label.setText(_translate("MainWindow", "Signal"))
        self.No_of_chunks_label.setText(_translate("MainWindow", "Enter the number of chunks "))
        self.fitting_order_lable.setText(_translate("MainWindow", " Enter the order of the fitting polynomial"))
        self.overlap_percentage_lable.setText(_translate("MainWindow", " Enter the percentage of the overlapping"))
        self.clipping_label.setText(_translate("MainWindow", "Clip the fitting process at ....% of the signal"))
        self.error_map_label.setText(_translate("MainWindow", "Error Map"))
        self.choose_x_axis_label.setText(_translate("MainWindow", "Choose the parameter of x-axis"))
        self.comboBox_Xaxis.setItemText(0, _translate("MainWindow", " "))
        self.comboBox_Xaxis.setItemText(1, _translate("MainWindow", "Number of chunks"))
        self.comboBox_Xaxis.setItemText(2, _translate("MainWindow", "The order of the fitting polynomial"))
        self.comboBox_Xaxis.setItemText(3, _translate("MainWindow", "overlapping between chunks"))
        self.choose_y_axis_label.setText(_translate("MainWindow", "Choose the parameter of Y-axis"))
        self.comboBox_Yaxis.setItemText(0, _translate("MainWindow", " "))
        self.comboBox_Yaxis.setItemText(1, _translate("MainWindow", "Number of chunks"))
        self.comboBox_Yaxis.setItemText(2, _translate("MainWindow", "The order of the fitting polynomial"))
        self.comboBox_Yaxis.setItemText(3, _translate("MainWindow", "overlapping between chunks"))
        self.generate_error_map_button.setText(_translate("MainWindow", "Generate Error Map"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
