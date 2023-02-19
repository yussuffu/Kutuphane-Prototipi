from PyQt5.QtWidgets import *
from ana_ekran_Qt import Ui_MainWindow
from kitap_oneri_python import kitap_oneri_page
from tum_kitaplar_python import tum_kitaplar_page
from Kutuphane_python import Kutuphane

class ana_ekran_page(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ana_ekran=Ui_MainWindow()
        self.kitap_onerileri=kitap_oneri_page()
        self.tum_kitaplar_111=tum_kitaplar_page()
        self.kitaplar=Kutuphane()
        self.ana_ekran.setupUi(self)

        self.ana_ekran.actionKitap_nerisi.triggered.connect(self.kitap_oneri)
        self.ana_ekran.actionT_m_Kitaplar.triggered.connect(self.tum_kitaplar)
        self.ana_ekran.pushButton_ekle_kitap_ekle.clicked.connect(self.kitap_ekle)

    def kitap_ekle(self):
        self.kitaplar.kitap_ekle(self.ana_ekran.lineEdit_isim_kitap_ekle.text(),self.ana_ekran.lineEdit_yazar_kitap_ekle.text(),self.ana_ekran.comboBox_katagori_kitap_ekle.currentText())
        self.tum_kitaplar_111.tabloya_kitap_ekle()
    def kitap_oneri(self):
        self.kitap_onerileri.show()
    def tum_kitaplar(self):
        self.tum_kitaplar_111.show()

