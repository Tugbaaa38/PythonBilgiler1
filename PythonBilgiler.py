#python da bazi islemler ve bilgiler

#********************************************Kucuk bir tavsiye*******************************************
#Degisken tanimlamasi yaparken dikkat etmemiz gereken bazi seyler vardir.
#Ornegin bir degisken tanimlarken anlamli ifadeler kullanmak daha hos olacaktir.
#Herhangi bir islem yapacagimiz zaman sayi tanimlamasinda s1 yerine sayi1 demek kodu daha okunakli kilar.
#camelCase yontemi cok kullanilir.Bu yontem de kelimenin ilk harfi kucuk, diger kelimelerin ilk harfleri buyuk olacak sekilde tanimlama yapariz.
#ör:  musteriNo 
#Degisken isimleri tanimlarken sayi ile baslamayin,ozel semboller kullanmayin.
#Turkce karakter kullanmamaya ozen gosterin.


# Python da (') (") (""") farkı ve kullanimi
"""Parantez icine metin yazarken  dikkat edecek olursak metinimizi ister " " içinde ister ' ' içinde metinlerimizi yazabiliriz.
Fakat bazi durumlara dikkat etmemiz gerekiyor.

İnceleyelim:
->print("Ingilizce de fare "mouse" demektir.") 
Burada python kodlari okurken tırnak nerde baslıyor nerde bitiyor dikkat eder ve bu durumda kodumuz hata verecektir.
Bu yuzden de bu isaretleri kullanirken dogru secmemiz gerekiyor.
->print('Ingilizce de fare "mouse" demektir.')
Bu sekilde kodumuz sorunsuz calisacaktir.

Bir diger isaretimiz ise ("""  """) isaretidir.Ayni sekilde metinlerimizi yazdirirken kullanabiliriz.
Ve uzun aciklama satirlarinda da bu isareti kullaniriz.
"""

#Her hangi bir degiskenin turu,uzunlugu nasıl bulunur ve ataması nasıl olur?

metin="Seni Cok Seviyorum"
print(metin)  #string degiskenleri de aynen bu sekilde yazdiriyoruz.
print(type(metin)) #Burada bize type komutu metin degiskenin turunu verecektir.
print(len(metin))  #len komutu ise bize metinin uzunlugunu verecektir fakat len bosluklari da sayar.Ciktimiz 18 olur.
hesap_no=12345678
#print(len(hesap_no))    #len komutu int turundeki degiskenlerin uzunlugunu bize veremez.Kod hata verir.

#Python da atama ve degis tokus

sayi1=10
sayi2=20
sayi3=30
sayi4=40

print(sayi1)
print(sayi2)
print(sayi3)
print(sayi4)

sayi1,sayi2=sayi3,sayi4  
#Goruldugu gibi python da degis tokus islemi cok kolaydir.
print('\n')   #alt satira gecme
print(sayi1)
print(sayi2)
print(sayi3)
print(sayi4)
#sayi3 ve sayi4 degeri degismedi.

#bu atamayi c de yapacak olsaydik;
#sayi1=sayi3;
#sayi2=sayi4;

print("Sayi1 degeri:{} ve Sayi2 degeri:{}".format(sayi1,sayi2)) 
print(f"Sayi1 degeri:{sayi1} ve Sayi2 degeri:{sayi2}")



