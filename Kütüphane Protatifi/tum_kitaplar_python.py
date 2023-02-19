from PyQt5.QtWidgets import *
from tum_kitaplar_Qt import Ui_Form
from Kutuphane_python import Kutuphane

class tum_kitaplar_page(QWidget):
    def __init__(self):
        super().__init__()
        self.tum_kiatplar=Ui_Form()
        self.kitap=Kutuphane()
        self.tum_kiatplar.setupUi(self)

        self.tabloya_kitap_ekle()
    def tabloya_kitap_ekle(self):
        kitaplar=self.kitap.tum_kitaplar()
        self.tum_kiatplar.tableWidget.clear()
        a=0
        for kitap in kitaplar:
            self.tum_kiatplar.tableWidget.setItem(a,0,QTableWidgetItem(kitap[0]))
            self.tum_kiatplar.tableWidget.setItem(a,1,QTableWidgetItem(kitap[1]))
            self.tum_kiatplar.tableWidget.setItem(a,2,QTableWidgetItem(kitap[2]))
            a+=1



