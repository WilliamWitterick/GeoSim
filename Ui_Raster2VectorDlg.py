# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Raster2VectorDlg.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Raster2VectorDlg(object):
    def setupUi(self, Raster2VectorDlg):
        Raster2VectorDlg.setObjectName("Raster2VectorDlg")
        Raster2VectorDlg.resize(401, 221)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Raster2VectorDlg.sizePolicy().hasHeightForWidth())
        Raster2VectorDlg.setSizePolicy(sizePolicy)
        Raster2VectorDlg.setMinimumSize(QtCore.QSize(401, 221))
        Raster2VectorDlg.setMaximumSize(QtCore.QSize(401, 221))
        self.verticalLayoutWidget = QtWidgets.QWidget(Raster2VectorDlg)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Label1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Label1.setMinimumSize(QtCore.QSize(379, 0))
        self.Label1.setObjectName("Label1")
        self.verticalLayout.addWidget(self.Label1)
        self.cmbProcessLayer = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cmbProcessLayer.setObjectName("cmbProcessLayer")
        self.verticalLayout.addWidget(self.cmbProcessLayer)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Raster2VectorDlg)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 170, 381, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ProgressBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget_2)
        self.ProgressBar.setObjectName("ProgressBar")
        self.horizontalLayout_3.addWidget(self.ProgressBar)
        self.btnRun = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btnRun.setObjectName("btnRun")
        self.horizontalLayout_3.addWidget(self.btnRun)
        self.btnExit = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btnExit.setObjectName("btnExit")
        self.horizontalLayout_3.addWidget(self.btnExit)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Raster2VectorDlg)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 381, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.rbPoints = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbPoints.setObjectName("rbPoints")
        self.horizontalLayout.addWidget(self.rbPoints)
        self.rbPolygons = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbPolygons.setChecked(True)
        self.rbPolygons.setObjectName("rbPolygons")
        self.horizontalLayout.addWidget(self.rbPolygons)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Raster2VectorDlg)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 110, 381, 51))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Label3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.Label3.setObjectName("Label3")
        self.verticalLayout_3.addWidget(self.Label3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tbxOutput = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.tbxOutput.setObjectName("tbxOutput")
        self.horizontalLayout_2.addWidget(self.tbxOutput)
        self.btnBrowse = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnBrowse.setObjectName("btnBrowse")
        self.horizontalLayout_2.addWidget(self.btnBrowse)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Raster2VectorDlg)
        QtCore.QMetaObject.connectSlotsByName(Raster2VectorDlg)

    def retranslateUi(self, Raster2VectorDlg):
        _translate = QtCore.QCoreApplication.translate
        Raster2VectorDlg.setWindowTitle(_translate("Raster2VectorDlg", "Raster to Vector Converter"))
        self.Label1.setText(_translate("Raster2VectorDlg", "Select Raster Layer To Process:"))
        self.cmbProcessLayer.setToolTip(_translate("Raster2VectorDlg", "Select the layer to process."))
        self.btnRun.setText(_translate("Raster2VectorDlg", "Run"))
        self.btnExit.setText(_translate("Raster2VectorDlg", "Exit"))
        self.label.setText(_translate("Raster2VectorDlg", "Select Vector Layer Type:            "))
        self.rbPoints.setText(_translate("Raster2VectorDlg", "Point Layer"))
        self.rbPolygons.setText(_translate("Raster2VectorDlg", "Polygon Layer"))
        self.Label3.setText(_translate("Raster2VectorDlg", "Specify output shapefile:"))
        self.tbxOutput.setToolTip(_translate("Raster2VectorDlg", "Give the filepath and filename of the output shapefile"))
        self.btnBrowse.setToolTip(_translate("Raster2VectorDlg", "Gives dialog box for selecting output filepath and filename."))
        self.btnBrowse.setText(_translate("Raster2VectorDlg", "Browse"))

