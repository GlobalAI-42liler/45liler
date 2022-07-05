from encodings import utf_8
from logging.config import listen



def puan_hesaplama(sinavpuani1,sinavpuani2):

    ortalama = sinavpuani1*0,4+sinavpuani2*0,6

    if ortalama>=90 and ortalama<=100:
        harf="AA"
        passing = "Gecti"
    elif ortalama>=85 and ortalama<=89:
        harf="BA"
        passing = "Gecti"
    elif ortalama>=65:
        harf="CC"
        passing = "Kaldi"
    else:
        harf="FF"
        passing = "Kaldi"

    return harf
    
def not_giriniz():
    adsoyad = input('İsminiz: ')
    okulno = input('Okul Numaranız: ')
    sinavpuani1 = input('1. Sınav Notunuz: ')
    sinavpuani2 = input('2. Sınav Notunuz: ')
    Data.append([adsoyad,okulno,sinavpuani1,sinavpuani2(sinavpuani1*0,4+sinavpuani2*0,6),puan_hesaplama(sinavpuani1,sinavpuani2)]) ##kontrol yapılaca
    
    print(Data)





def save_al():

    with open('bilgiler.txt',"r",encoding="utf_8") as file:
        liste = []

        for i in file:
            liste.append(puan_hesaplama(i))

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
        not_giriniz() #not giririş 
    elif islem == '2':
        save_al()     #notları txt ye kayıt ettirecek
    elif islem == '3':
        ortalamalar_globalAI()

    
    else:           #yanlış girilen bi numarada fonksiyonu durduracak
        break  