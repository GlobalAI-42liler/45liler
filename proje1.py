import pandas as pd

data = {"Adsoyad":[], "Okulno":[], "Ders":[], "Vize":[], "Final":[], "Ortalama":[], "Harf Notu":[]}

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
        harf = "FF Kaldı"
    data["Adsoyad"].append(adsoyad)
    data["Okulno"].append(okulno)
    data["Ders"].append(ders)
    data["Vize"].append(vize)
    data["Final"].append(final)
    data["Ortalama"].append(ortalama)
    data["Harf Notu"].append(harf)
    print(f"{okulno} numaralı {adsoyad} adlı öğrencinin {ders} dersinden, {ortalama} ortalama ile aldığı harf notu {harf}")
    print(data)
ogrenciBilgiler()

data = pd.DataFrame(data)
data.to_excel("Otomasyon.xlsx")
data
