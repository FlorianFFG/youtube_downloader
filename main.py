# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys
import pytube
 
class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle("Диалоговое окно")
        self.resize(200, 70)
        
        self.mainBox = QtWidgets.QVBoxLayout()
        
        self.lineEdit = QtWidgets.QLineEdit()
        self.mainBox.addWidget(self.lineEdit)
        
        self.hbox = QtWidgets.QHBoxLayout()
        self.btnOK = QtWidgets.QPushButton("&OK")
        self.btnCancel = QtWidgets.QPushButton("&Cancel")
        self.btnCancel.setDefault(True)
        self.btnOK.clicked.connect(self.accept)
        self.btnCancel.clicked.connect(self.reject)
        self.hbox.addWidget(self.btnOK)
        self.hbox.addWidget(self.btnCancel)
        self.mainBox.addLayout(self.hbox)
        
        self.setLayout(self.mainBox)
 
def on_accepted():
    print("on_accepted")
 
def on_rejected():
    print("on_rejected")
 
def on_finished(status):
    print("on_finished", status)
 
def on_clicked():
    dialog = MyDialog(window)
    dialog.accepted.connect(on_accepted)
    dialog.rejected.connect(on_rejected)
    dialog.finished[int].connect(on_finished)
    result = dialog.exec_()
    if result == QtWidgets.QDialog.Accepted:
        # link = "https://www.youtube.com/watch?v=PzwXT8hdFqM&t=1152s"
        video = pytube.YouTube(dialog.lineEdit.text())
        stream = video.streams.get_highest_resolution()
        stream.download()
        # print(dialog.lineEdit.text())
    else:
        print("Нажата кнопка Cancel, кнопка Закрыть или клавиша <Esc>", 
              result)
 
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QDialog")
window.resize(300, 70)
 
button = QtWidgets.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)
 
box = QtWidgets.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
 
window.show()
sys.exit(app.exec_())
