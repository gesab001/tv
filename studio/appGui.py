# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app-gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import io
from PyQt5 import QtCore, QtGui, QtWidgets
from appCore import getBible, getVideoFile, getSrtFile, playVideo, getWordList, playVideoWithoutSubs, showErrorDialog
from bad_word_identifier import loadBadWords
from youtubeDownloaderScript import download
from getBibleVerses import getTopics
from PyQt5.QtCore import Qt
import json
import platform
import os
import sys

class Ui_MainWindow(object):
    def showPopUpInfo(self, title, message, detail):
        self.messageBox.setIcon(QtWidgets.QMessageBox.Critical)    
        self.messageBox.setWindowTitle(title)  
        self.messageBox.setText(message)          
        self.messageBox.setDetailedText(detail)          

        self.messageBox.exec()
        
        
    def setVideoFileName(self):
        try:
          filename = sys.argv[1]          
        except IndexError as error:
          filename = getVideoFile(self)
        
        self.plainTextEdit.setPlainText(filename)

    def downloadYoutube(self):
          youtubeId= self.plainTextEdit_youtube_url_input.toPlainText()
          download(youtubeId)

                
    def setSrtFileName(self):
        videoFolder = os.path.dirname(self.plainTextEdit.toPlainText())
        self.plainTextEdit_2.setPlainText(getSrtFile(self, videoFolder))
        srtfile = self.plainTextEdit_2.toPlainText()

        self.populateTopicList(srtfile)



    def play(self):
        choice = "book"
        topic = "Revelation"    
        videofile = self.plainTextEdit.toPlainText()
        srtfile = self.plainTextEdit_2.toPlainText()
        if self.bibleRadioButton.isChecked():
          index = self.bibleListView.currentIndex()
          choice = "book"
          topic = self.bibleListView.model().data(index, Qt.DisplayRole)
          print(topic) 
        if self.topicRadioButton.isChecked():
          choice = "topic"
          index = self.topicListView.currentIndex()
          topic = self.topicListView.model().data(index, Qt.DisplayRole)
          print(topic) 
        print("topic")
        
        print(topic)
        if len(videofile)>1:
         print("self.filterOnRadioButtonisChecked()")
         if self.filterOnRadioButton.isChecked():
          if topic!=None:
           if len(srtfile)>1:
            playVideo(self, videofile, srtfile, choice, topic)
           else:
            print("please load SRT file for the video")
            self.showPopUpInfo("Subtitles", "please load SRT file for the video", "click on the Load SRT button")        
         
          else:
            if self.topicRadioButton.isChecked():
              self.showPopUpInfo("Topic", "please select a topic", "click on a word from the topic list to generate bible verses where the word is found")        
            if self.bibleRadioButton.isChecked():
              self.showPopUpInfo("Book", "please select a book", "click on a book from the book list to genereate bible verses from the selected book")        
              
         else:
          if topic!=None:
            print("play video without subtitles")
            playVideoWithoutSubs(self, videofile, choice, topic)         
          else:
            if self.topicRadioButton.isChecked():
              print("select a topic")
              self.showPopUpInfo("Topic", "please select a topic",  "click on a word from the topic list to generate bible verses where the word is found")        
            if self.bibleRadioButton.isChecked():
              print("select a book")  
              self.showPopUpInfo("Book", "please select a book", "click on a book from the book list to genereate bible verses from the selected book")        

        else:
          print("please select a video")  
          self.showPopUpInfo("Video", "please select a video", "click on the Load Video button")
        

    def getBooksOfTheBible(self):
        books = []
        bible = getBible(self)
        for item in bible:
          book = item['book']
          if book not in books:
            books.append(book)
        return books
    
    def populateBibleList(self):
        print("LINE 29")
        entries = self.getBooksOfTheBible()
        model = QtGui.QStandardItemModel()
        self.bibleListView.setModel(model)
        for i in entries:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)



    
    def populateTopicList(self, srt):
        print("LINE 29" + srt)

        entries = getTopics()
        try:
          f = io.open(srt, encoding='latin-1')
          subtitle_string = f.read().strip() 
          json_data = {} 
          sublist = list(filter(None, subtitle_string.split("\n\n"))) #removes empty strings in a list of strings
          print(subtitle_string)
          self.progress_dialog = QtWidgets.QProgressDialog("Analysing subtitles to generate keywords for topic list", "", 0,  len(sublist)-1, self)
          self.progress_dialog.setWindowModality(QtCore.Qt.WindowModal)
          self.progress_dialog.setWindowTitle("Analysing subtitles")
          self.progress_dialog.setWindowModality(QtCore.Qt.WindowModal)
          self.progress_dialog.setCancelButtonText("Cancel")
          self.progress_dialog.show() 
          self.progress_dialog.setValue(0)
          badlanguage = loadBadWords()
          entries = entries + getWordList(self.progress_dialog.setValue, sublist, badlanguage)
          f.close()

        except:
          print("srt not loaded") 

        model = QtGui.QStandardItemModel()
        self.topicListView.setModel(model)
        for i in entries:
            item = QtGui.QStandardItem(i)
            self.messageBox.setDetailedText(i)
            model.appendRow(item)    
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 704)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.messageBox = QtWidgets.QMessageBox(MainWindow)


        
        self.openVideo = QtWidgets.QPushButton(self.centralwidget)
        self.openVideo.setGeometry(QtCore.QRect(260, 110, 111, 25))
        self.openVideo.setObjectName("openVideo")
        self.openSrt = QtWidgets.QPushButton(self.centralwidget)
        self.openSrt.setGeometry(QtCore.QRect(260, 150, 111, 25))
        self.openSrt.setObjectName("openSrt")
        self.playVideo = QtWidgets.QPushButton(self.centralwidget)
        self.playVideo.setGeometry(QtCore.QRect(400, 600, 89, 25))
        self.playVideo.setObjectName("playVideo")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(380, 110, 261, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(380, 150, 261, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(190, 40, 511, 151))
        self.groupBox.setObjectName("groupBox")
        self.download_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.download_pushButton.setGeometry(QtCore.QRect(70, 30, 111, 25))
        self.download_pushButton.setObjectName("download_pushButton")
        self.plainTextEdit_youtube_url_input = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_youtube_url_input.setGeometry(QtCore.QRect(190, 30, 261, 31))
        self.plainTextEdit_youtube_url_input.setObjectName("plainTextEdit_youtube_url_input")
        self.plainTextEdit_youtube_url_input.setPlaceholderText("enter youtube video url or videoId")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(120, 310, 641, 281))
        self.groupBox_2.setObjectName("groupBox_2")
        self.topicListView = QtWidgets.QListView(self.groupBox_2)
        self.topicListView.setGeometry(QtCore.QRect(40, 40, 256, 192))
        self.topicListView.setObjectName("topicListView")
        self.topicRadioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.topicRadioButton.setGeometry(QtCore.QRect(130, 240, 112, 23))
        self.topicRadioButton.setObjectName("topicRadioButton")
        self.bibleRadioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.bibleRadioButton.setGeometry(QtCore.QRect(440, 240, 112, 23))
        self.bibleRadioButton.setObjectName("bibleRadioButton")
        self.bibleListView = QtWidgets.QListView(self.groupBox_2)
        self.bibleListView.setGeometry(QtCore.QRect(350, 40, 256, 192))
        self.bibleListView.setObjectName("bibleListView")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(310, 210, 281, 80))
        self.groupBox_3.setObjectName("groupBox_3")
        self.filterOnRadioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.filterOnRadioButton.setGeometry(QtCore.QRect(30, 40, 112, 23))
        self.filterOnRadioButton.setObjectName("filterOnRadioButton")
        self.filterOffRadioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.filterOffRadioButton.setGeometry(QtCore.QRect(160, 40, 112, 23))
        self.filterOffRadioButton.setObjectName("filterOffRadioButton")
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.openVideo.raise_()
        self.openSrt.raise_()
        self.playVideo.raise_()
        self.plainTextEdit.raise_()
        self.plainTextEdit_2.raise_()
        self.groupBox_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 936, 22))
        self.menubar.setObjectName("menubar")
        #self.menuDownload = QtWidgets.QMenu(self.menubar)
        #self.menuDownload.setObjectName("menuDownload")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionloadTopicList = QtWidgets.QAction(MainWindow)
        self.actionloadTopicList.setObjectName("actionloadTopicList")
        self.actionloadBibleList = QtWidgets.QAction(MainWindow)
        self.actionloadBibleList.setObjectName("actionloadBibleList")
        #self.actionYoutube = QtWidgets.QAction(MainWindow)
        #self.actionYoutube.setObjectName("actionYoutube")
        #self.actionTorrent = QtWidgets.QAction(MainWindow)
        #self.actionTorrent.setObjectName("actionTorrent")
        self.actiondownloadYoutube = QtWidgets.QAction(MainWindow)
        self.actiondownloadYoutube.setObjectName("actiondownloadYoutube")
        #self.menuDownload.addAction(self.actionYoutube)
        #self.menuDownload.addAction(self.actionTorrent)
        #self.menubar.addAction(self.menuDownload.menuAction())


        self.retranslateUi(MainWindow)
        try:
          filename = sys.argv[1]
          self.plainTextEdit.setPlainText(filename)
        except IndexError as error:
          print("video not loaded")
        self.openVideo.clicked.connect(self.setVideoFileName)

        self.playVideo.clicked.connect(self.play)
        self.openSrt.clicked.connect(self.setSrtFileName)
        self.download_pushButton.clicked.connect(self.downloadYoutube)

        self.populateBibleList()
        self.populateTopicList("")
        self.topicListView.clicked['QModelIndex'].connect(MainWindow.show)
        self.bibleListView.clicked['QModelIndex'].connect(MainWindow.show)
        self.topicRadioButton.clicked['bool'].connect(MainWindow.show)
        self.bibleRadioButton.clicked['bool'].connect(MainWindow.show)
        self.bibleRadioButton.setChecked(True)

        self.filterOffRadioButton.clicked['bool'].connect(MainWindow.show)
        self.filterOnRadioButton.clicked['bool'].connect(MainWindow.show)
        self.filterOnRadioButton.setChecked(True)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BLF Video Player"))
        self.openVideo.setText(_translate("MainWindow", "Load Video"))
        self.openSrt.setText(_translate("MainWindow", "Load SRT"))
        self.playVideo.setText(_translate("MainWindow", "Play"))
        self.groupBox.setTitle(_translate("MainWindow", "LOAD FILES"))
        self.download_pushButton.setText(_translate("MainWindow", "Download"))
        self.groupBox_2.setTitle(_translate("MainWindow", "CHOOSE BIBLE VERSES"))
        self.topicRadioButton.setText(_translate("MainWindow", "Topic"))
        self.bibleRadioButton.setText(_translate("MainWindow", "Book"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Filter"))
        self.filterOnRadioButton.setText(_translate("MainWindow", "On"))
        self.filterOffRadioButton.setText(_translate("MainWindow", "Off"))
        #self.menuDownload.setTitle(_translate("MainWindow", "Download"))
        self.actionloadTopicList.setText(_translate("MainWindow", "loadTopicList"))
        self.actionloadBibleList.setText(_translate("MainWindow", "loadBibleList"))
        #self.actionYoutube.setText(_translate("MainWindow", "Youtube"))
        #self.actionTorrent.setText(_translate("MainWindow", "Torrent"))
        self.actiondownloadYoutube.setText(_translate("MainWindow", "downloadYoutube"))
