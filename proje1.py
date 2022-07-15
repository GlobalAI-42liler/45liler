import pandas as pd


class OgrenciOtomasyon:
    data = {"Adsoyad": [], "Okulno": [], "Ders": [], "Vize": [], "Final": [], "Ortalama": [], "Harf Notu": []}

    def __init__(self, adsoyad, okulno, ders, vize, final):
        self.adsoyad = adsoyad
        self.okulno = okulno
        self.ders = ders
        self.vize = vize
        self.final = final

    def ogrenciBilgiler(self):

        ortalama = (self.vize * 0.4 + self.final * 0.6)

        if ortalama >= 90 and ortalama <= 100:
            harf = "A1 Başarılı"
        elif ortalama >= 85 and ortalama < 90:
            harf = "A2 Başarılı"
        elif ortalama >= 80 and ortalama < 85:
            harf = "A3 Başarılı"
        elif ortalama >= 75 and ortalama < 80:
            harf = "B1 Geçti"
        elif ortalama >= 70 and ortalama < 75:
            harf = "B2 Geçti"
        elif ortalama >= 65 and ortalama < 70:
            harf = "B3 Geçti"
        elif ortalama >= 60 and ortalama < 65:
            harf = "C1 Koşullu Geçti"
        elif ortalama >= 55 and ortalama < 60:
            harf = "C2 Koşullu Geçti"
        elif ortalama >= 50 and ortalama < 65:
            harf = "C3 Koşullu Geçti"
        else:
            harf = "FF Kaldı"

        self.data["Adsoyad"].append(self.adsoyad)
        self.data["Okulno"].append(self.okulno)
        self.data["Ders"].append(self.ders)
        self.data["Vize"].append(self.vize)
        self.data["Final"].append(self.final)
        self.data["Ortalama"].append(ortalama)
        self.data["Harf Notu"].append(harf)

        print(f"{self.okulno} numaralı {self.adsoyad} adlı öğrencinin {self.ders} dersinden, {ortalama} ortalama ile aldığı harf notu {harf}")
        print(self.data)




ogrSayisi=int(input("Öğrenci Sayısını Giriniz:"))
while ogrSayisi>0:

    adsoyad = input("Adınız ve Soyadınız: ")
    okulno = input("Okul Numaranız: ")
    ders = input("Ders giriniz: ")
    vize = int(input("Vize puanınız:"))
    final = int(input("Final puanınız:"))


    ogr=OgrenciOtomasyon(adsoyad,okulno,ders,vize,final)
    ogr.ogrenciBilgiler()

    ogrSayisi-=1


data = pd.DataFrame(ogr.data)
data.to_excel("Otomasyon.xlsx")
print(data)
