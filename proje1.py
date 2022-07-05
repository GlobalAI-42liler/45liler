def puan_hesaplama(satir):
    satir = satir[:-1]
    liste = satir.split(':')

    ogrenciAdi = liste[0]
    puanlar = liste[1].split(',')

    sinavpuani1 = int(puanlar[0])
    sinavpuani2 = int(puanlar[1])
    
    ortalama = (sinavpuani1+sinavpuani2)/2
    
    if ortalama>=90 and ortalama<=100:
        harf="AA"
    elif ortalama>=85 and ortalama<=89:
        harf="BA"
    elif ortalama>=65:
        harf="CC"
    else:
        harf="FF"

    return ogrenciAdi + ": " + harf + "\n" 


    def not_giriniz():
        adsoyad = input('İsminiz: ')
        okulno = input('Okul Numaranız: ')
        sinavpuani1 = input('1. Sınav Notunuz: ')
        sinavpuani2 = input('2. Sınav Notunuz: ')

        with open("bilgiler.txt","a", encoding="utf-8") as file:  # yazılan bilgileri txt ye kayıt ettiriyor   #a a Moduyla dosyaya veri kayıt edicez
            file.write(adsoyad+' '+ okulno+ ' '+sinavpuani1+','+sinavpuani2+'\n') # verileri yazdırıyoruz

    def save_al():
        pass

    def ortalamalar_globalAI():
        with open("bilgiler.txt","r",encoding="utf-8") as file: #okuma işlemi yapıcaz
            for satir in file:
                print(puan_hesaplama(satir))

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
