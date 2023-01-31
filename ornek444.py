"""
secim = input("Sinema için (s) tiyatro için (t) yi tuşlayınız:")
ogrenci = input("Ogrenci misiniz?(E/H) : ")
ucret = 0
#indirimsiz ücret hesaplama 
if secim == "1":
    ucret = 15
elif secim == "2":
    ucret = 10
# öğrenci ücreti hesaplama 
if ogrenci == "E" or ogrenci == "e" :
    ucret = ucret / 2 
print("Ödemeniz gereken ücret:{}".format(ucret))
"""
def ciftMi(k):
    return k % 2 == 0

toplam = 0
sayac = 0
baslangıc = input("Başlangıç sayısı:")
bitis =input("Bitiş sayısı:")
for sayi in range(int(baslangıc),int(bitis)):
    if(ciftMi(int(sayi))):
        toplam = toplam+sayi
        sayac =sayac+1
print("Ortalama" , (toplam/sayac))
