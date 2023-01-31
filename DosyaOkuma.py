"""
Dosya Okuma ve Yazma işlemleri
Öğrenci notlarını tutan bir dosya olsun
"""
# Yazmak için dosya oluştur.

dosya = open("notlar.txt" , "w")
notlar = {
    "anıl": 45,
    "yavuz": 90,
    "zeynep": 75,
    "asım": 60,
    "serdar": 85,
    "azamet": 99
}
for item in notlar.items():
    dosya.write(str(item))
    dosya.write("\n")

dosya.close()

# Dosyayı okumak için tekrar açtık
dosya = open("notlar.txt", "r")
for i in dosya.readlines():
    print(i)

dosya.close()