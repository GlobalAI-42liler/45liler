from encodings import utf_8
from logging.config import listen

Data = []

def ogrenciBilgiler():
  adsoyad = input("Adınız ve Soyadınız: ")
  okulno = input("Okul Numaranız: ")
  ders = input("Ders giriniz: ")
  vize = int(input("Vize puanınız:"))
  final = int(input("Final puanınız:"))

  ortalama = (vize*0.4+final*0.6)

  if ortalama >=90 and ortalama <= 100:
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
    harf="FF Kaldı"
  Data.append([adsoyad, okulno, ders, vize, final, ortalama])
  print(f"{okulno} numaralı {adsoyad} adlı öğrencinin {ders} dersinden, {ortalama} ortalama ile aldığı harf notu {harf}")
  print(Data)
ogrenciBilgiler()

  



def kaydet():

    with open('bilgiler.txt',"r",encoding="utf_8") as file:
        liste = []

        for i in file:
            liste.append(ortalama(i))

        with open("sonuclar.txt","w",encoding="utf_8") as file2:
            for i in liste:
                file.write(i)

def ortalamalar_globalAI():
    with open("bilgiler.txt","r",encoding="utf-8") as file: #okuma işlemi yapıcaz
        for satir in file:
            print(puan_hesaplama(satir))

while True:
    islem = input('1 - Bilgileri Giriniz\n2 - Notu Kayıt Et\n3 - Notları Görüntüle\n4 - Kapat\n')

    if islem == '1':
        ogrenciBilgiler() #bilgi girişi
    elif islem == '2':
        save_al()     #notları txt ye kayıt ettirecek
    elif islem == '3':
        ortalamalar_globalAI()
    else:           #yanlış girilen bi numarada fonksiyonu durduracak
        break  
