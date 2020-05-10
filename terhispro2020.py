# Türk Silahlı Kuvvetleri Terhis Hesaplama Programı (2020)
# 6 Aylık yeni askerlik sistemine göre kodlanmıştır
# 
# Tarık VARDAR 
# tarikvardar@gmail.com 


import datetime

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

tarih = input('Sevk Tarihini (Yıl.Ay.Gun) şeklinde Giriniz : ')

tarih = tarih.split('.')

sevk = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))

simdi = datetime.datetime.now()

now = (simdi - sevk)

print('.' * 55)
print(f'Bugüne kadar ki askerlik süresi {now.days} gündür')
print('.' * 55)

muhtemel_terhis = sevk.day, sevk.month +6, sevk.year

if sevk.month + 6 > 12:
    muhtemel_terhis = sevk.day, sevk.month -6, sevk.year + 1
else:
    muhtemel_terhis = sevk.day, sevk.month + 6, sevk.year

print()

gec_katilis = int(input('Geç Katılış : '))

rapor = int(input('Rapor : '))
if rapor >6:
    rapor = rapor -6
else:
    rapor = 0

ceza = int(input('Ceza : '))

erken_terhis = int(input('Erken Terhis : '))

yol = int(input('Yol İzni : '))


gun = (muhtemel_terhis[0]) + gec_katilis + rapor + ceza - erken_terhis - yol
ay = muhtemel_terhis [1]
yil = muhtemel_terhis [2]

terhis = gun, ay, yil
if ay == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    if gun > 31:
        terhis = gun -31, ay +1, yil
if ay == 4 or 6 or 9 or 11:
    if gun > 30:
        terhis = gun - 30, ay + 1, yil
if ay == 2:
    if gun > 28:
        terhis = gun -28, ay +1, yil
else:
    pass

print('-' * 55)
print(f'Sevk Tarihine Göre 6 Ay Bitişi Gün.Ay.Yıl {muhtemel_terhis}')
print('-' * 55)
print(f'Hesaplanan Kesin Terhis Tarihi Gün.Ay.Yıl \n**{terhis}** dir.')
print('-' * 55)