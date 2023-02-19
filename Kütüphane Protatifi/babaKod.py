from PyQt5.QtWidgets import QApplication
from giris_ekrani_python import giris_ekrani_page


app=QApplication([])
pencere=giris_ekrani_page()
pencere.show()
app.exec_()








