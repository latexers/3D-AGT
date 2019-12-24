#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This program creates a menubar. The
menubar has one menu with an exit action.

author: Murong Wang
website: wangmurong.org.cn
last edited: Nov. 2019
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication,QMessageBox
from PyQt5.QtGui import QIcon


class mainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('./Icons/exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        editMenu = menubar.addMenu("&Edit")
        viewMenu = menubar.addMenu("&View")
        netMenu = menubar.addMenu("&Network")
        dataMenu = menubar.addMenu("&Data")
        helpMenu = menubar.addMenu("&Help")

        helpMenu.addAction(exitAction)
        dataMenu.addAction(exitAction)
        netMenu.addAction(exitAction)
        viewMenu.addAction(exitAction)
        editMenu.addAction(exitAction)
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('3D-AGT')
        self.setWindowIcon(QIcon("./Icons/LFT3.png"))
        self.show()

    def about(self):
        QMessageBox.about(self, "About 3D Abalel Guided Thepy", "ddddd")

    def createActions(self):
        self.about(


