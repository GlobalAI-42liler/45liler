class puan_hesaplama(satir):
    satir = satir[:-1]
    liste = satir.split(' ')

    AdSoyad = liste[0]
    notlar = liste[1]
    
    ortalama = (sınavpuani1+sınavpuani2)/2

class not_giriniz():
    adsoyad = input('İsminiz: ')
    okulno = input('Okul Numaranız: ')
    sinavpuani1 = input('1. Sınav Notunuz: ')
    sinavpuani2 = input('2. Sınav Notunuz: ')

    with open("bilgiler.txt","a", encoding="utf-8") as file:  # yazılan bilgileri txt ye kayıt ettiriyor   #a a Moduyla dosyaya veri kayıt edicez
        file.write(adsoyad+' '+ okulno+ ' '+sinavpuani1+','+sinavpuani2+'\n') # verileri yazdırıyoruz

class save_al():
    pass

class ortalamalar_globalAI():
    with open("bilgiler.txt","r",encoding="utf-8") as file: #okuma işlemi yapıcaz
        for satir in file:
            print(satir)

while True:
    islem = input('1 - Bilgileri Giriniz\n2 - Notu Kayıt Et\n3 - Notları Görüntüle\n4 - Kapat\n')

    if islem == '1':
        not_giriniz() #not giriş 
    elif islem == '2':
        save_al()     #notları txt ye kayıt ettirecek
    elif islem == '3':
        ortalamalar_globalAI()
    else:           #yanlış girilen bi numarada fonksiyonu durduracak
        break
