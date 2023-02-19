import sqlite3

class Kutuphane():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.con=sqlite3.connect("Kütüphane")
        self.cursor=self.con.cursor()

        self.cursor.execute("create table if not exists kitaplar(isim TEXT,yazar TEXT,katagori TEXT)")
        self.con.commit()

    def kitap_ekle(self,isim,yazar,katagori):
        self.cursor.execute("insert into kitaplar values(?,?,?)",(isim,yazar,katagori))
        self.con.commit()
    def tum_kitaplar(self):
        self.cursor.execute("select * from kitaplar")
        kitaplar=self.cursor.fetchall()
        return kitaplar

class Kayitli_kisiler():
    def __init__(self):
        self.baglanti_olustur2()
    def baglanti_olustur2(self):
        self.con2=sqlite3.connect("Kayıtlı Kişiler")
        self.cursor2=self.con2.cursor()

        self.cursor2.execute("create table if not exists üyeler(kullanici_adi TEXT,şifre TEXT)")
        self.con2.commit()
    def kaydol(self,kullanici_adi,sifre):
        self.cursor2.execute("insert into üyeler values(?,?)",(kullanici_adi,sifre))
        self.con2.commit()

    def sorgula(self,kullanici_adi,sifre):
        self.cursor2.execute("select * from üyeler where kullanici_adi=? and şifre=?",(kullanici_adi,sifre))
        kisiler=self.cursor2.fetchall()
        if len(kisiler)!=0:
            return True
        else:
            return False


