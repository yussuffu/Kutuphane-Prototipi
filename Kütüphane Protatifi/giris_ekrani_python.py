from PyQt5.QtWidgets import *
from giris_ekranı_Qt import Ui_Form
from ana_ekran_python import ana_ekran_page
from Kutuphane_python import Kayitli_kisiler,Kutuphane


class giris_ekrani_page(QWidget):
    def __init__(self):
        super().__init__()
        self.giris_ekrani = Ui_Form()
        self.ana_ekrani = ana_ekran_page()
        self.uyeler = Kayitli_kisiler()
        self.kitaplar=Kutuphane()
        self.giris_ekrani.setupUi(self)

        self.giris_ekrani.pushButton_giris_yap.clicked.connect(self.giris_yap)
        self.giris_ekrani.pushButton_kaydol.clicked.connect(self.kaydol)

        self.show()

    def giris_yap(self):
        if self.uyeler.sorgula(self.giris_ekrani.lineEdit_kullanici_adi.text(),
                               self.giris_ekrani.lineEdit_sifre.text()):
            self.giris_ekrani.label_bildiri_girisEkrani.setText("Giriş Yapıldı")
            self.hide()
            self.ana_ekrani.show()
        else:
            self.giris_ekrani.label_bildiri_girisEkrani.setText("Tekrar Dene")

    def kaydol(self):
        self.uyeler.kaydol(self.giris_ekrani.lineEdit_kullanici_adi.text(), self.giris_ekrani.lineEdit_sifre.text())
        self.giris_ekrani.label_bildiri_girisEkrani.setText("Kayıt Olundu")
