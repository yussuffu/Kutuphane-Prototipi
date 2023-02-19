from PyQt5.QtWidgets import *
from kitap_oneri_Qt import Ui_Form
from Kutuphane_python import Kutuphane
import random

class kitap_oneri_page(QWidget):
    def __init__(self):
        super().__init__()
        self.kitap_oneri=Ui_Form()
        self.kitap_oneri.setupUi(self)
        self.kitap=Kutuphane()

        self.kitap_oneri.pushButton_oner_kitapOner.clicked.connect(self.oner)

    def oner(self):
        kitaplar=self.kitap.tum_kitaplar()
        kitap=random.choice(kitaplar)
        self.kitap_oneri.lineEdit_isim_kitapOner.setText(kitap[0])
        self.kitap_oneri.lineEdit_yazar_kitapOner.setText(kitap[1])
        self.kitap_oneri.lineEdit_katagori_kitapOner.setText(kitap[2])

