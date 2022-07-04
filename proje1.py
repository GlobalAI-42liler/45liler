def not_giriniz():
    adsoyad = input('İsminiz: ')
    okulno = input('Okul Numaranız: ')
    sınavpuani1 = input('1. Sınav Notunuz: ')
    sınavpuani2 = input('2. Sınav Notunuz: ')

    with open("bilgiler.txt","a", encoding="utf-8") as file:  # yazılan bilgileri txt ye kayıt ettiriyor   #a a Moduyla dosyaya veri kayıt edicez
        file.write(adsoyad+' '+ okulno+ ' '+sınavpuani1+','+sınavpuani2+'\n') # verileri yazdırıyoruz

def save_al():
    pass
def ortalamalar_globalAI():
    with open("bilgiler.txt","r",encoding="uft-8") as file: #okuma işlemi yapıcaz
        for satir in file:
            print(satir)

while True:
    islem = input('1 - Bilgileri Giriniz\n2 - Notu Kayıt Et\n3 - Notları Görüntüle\n4 - Kapat\n')

    if islem == '1':
        not_giriniz() #not giririş 
    elif islem == '2':
        save_al()     #notları txt ye kayıt ettirecek
    elif islem == '3':
        save_al()
    else:           #yanlış girilen bi numarada fonksiyonu durduracak
        break
