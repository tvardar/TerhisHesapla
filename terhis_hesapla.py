# Türk Silahlı Kuvvetleri Terhis Hesaplama Programı (2020)
# 6 Aylık yeni askerlik sistemine göre kodlanmıştır
# 
# Tarık VARDAR 
# tarikvardar@gmail.com 


import datetime
import datedelta

mesaj = ' Terhis Hesaplama '
mesaj2 = ' Tarik VARDAR '
mesaj3 = ' tarikvardar@gmail.com '

mesaj= mesaj.center(55, '*')
mesaj2 = mesaj2.center(55, '*')
mesaj3 = mesaj3.center(55, '*')

print()
print('*' * 55)
print(mesaj)
print('*' * 55)
print(mesaj2)
print(mesaj3)
print('*' * 55)
print()

#Bir sevk tarihi bilgisi girilmesini istiyoruz
tarih0 = input('Sevk Tarihini (Gun.Ay.Yıl) şeklinde Giriniz : ')

#Kullanıcı boş bırakırsa uyarıyoruz
while not tarih0.strip():
    tarih0 = input('Bir Tarih Girmediniz! Sevk Tarihi : ')

#Kontrol için kullanıcıya girdiği tarihi gösteriyoruz
print(f'Girilen Sevk Tarihi : {tarih0}')

#Baştan ve sondan boşluk bırakırsa, boşlukları siliyoruz
tarih1 = tarih0.strip()

#Girilen tarihi '.' lardan bölüyoruz
tarih1 = tarih0.split('.')

#Python Yıl Ay Gün okur, biz tersine çeviriyoruz
tarih = tarih1.reverse()

#Girilen tarihi gün ay yıl şeklinde bölümlerini bir değişkene atıyoruz
sevk = datetime.datetime(int(tarih1[0]), int(tarih1[1]), int(tarih1[2]))

# Bu değişkeni en son hesapta toplam süreyi bulmak için atadık
sevk1 = sevk

#şimdiki zamanı buluyoruz
now = datetime.datetime.now()

#sevk tarihinden bugüne geçen süreyi hesaplıyoruz
sure = (now - sevk)

#sevk tarihinden bugüne kadarki süreyi bir değişkene atıyoruz
askerlik_gun = sure.days

#Yukarıda değişkeni yazdırıp, askerlikte geçen süreyi buluyoruz
print(f'Askerlikte Geçen Süre {askerlik_gun} gün.')

# -----------------------------------
# Sayılan Sayılmayan günlerin hesabına başlıyoruz
# -----------------------------------

gec_katilis = int(input('Geç Katılış : '))

ceza = int(input('Ceza : '))

#Rapor 6 günden büyükse 6 günden fazlasını askerlikten sayma
rapor = int(input('Rapor : '))

if rapor > 6:
    rapor -= 6
else:
    rapor = 0

# İzin 6 gün hakkı var, kullanmadığı kısmı kadar askerliği kısalt
izin = int(input('Kullanılan izin : '))

if izin < 6:
    izin = (6 - izin)
else:
    izin = izin

erken_terhis = int(input('Erken Terhis : '))

yol = int(input('Yol İzni : '))

# Otomatik yol izni 1 gün vermek isterseniz alttaki satırı açın
#if yol == 0:
#    yol += 1
#else:
#    yol = yol


#Askerliği uzatan günleri bir yere toplayalım
uzat = gec_katilis + ceza + rapor

#Askerliği kısaltan günleri bir yere toplayalım
kisalt = erken_terhis + yol + izin


# Üstteki lerin toplamı negatif olursa, pozitif olursa böyle yap
if uzat - kisalt < 0:
    h1 = kisalt - uzat
else:
    h1 = uzat - kisalt

# Üstteki hesabı bir değişkene atayalım
gun = h1

#Sevk edilen tarihin üzerine 6 ay koyup, eldeki gün kadar toplayıp çıkaralım
sevk = datetime.datetime(int(tarih1[0]), int(tarih1[1]), int(tarih1[2])) +  datedelta.datedelta(months=6) -  datedelta.datedelta(days=gun)

sevk2 = sevk
# Bulduğumuz Terhis Tarihini yazdıralım
print()
print('Terhis Olacağınız Tarih :')
print(sevk.day, sevk.month, sevk.year)
print()

toplam_sure = sevk2 - sevk1
print(f'Toplam askerlik süresi {toplam_sure.days} gün')

kalan = toplam_sure.days - askerlik_gun

if kalan <=0:
    print(f'Terhis Oldunuz. Sivil Hayatta Başarılar !!!')
else:
    print(f'Terhise {kalan} gün kaldı')
