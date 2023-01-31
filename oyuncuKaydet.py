print("oyuncu kaydetme programı:")
ad = input("Oyuncunun ADI:")
soyAd = input("oyuncunun Soy Adı : ")
takım = input("oyuncunun Takımı:")

bilgiler = [ad,soyAd,takım]
print("bilgiler Kaydediliyor..")
print("Oyuncu Adı: {}\n Oyuncu Soyadı :{}\n Oyuncunun Takımı : {}\n " .format(bilgiler[0],bilgiler[1],bilgiler[2]))
print("bilgiler kaydedildi..")
"burada bir takım için oyuncu kaydetme programı oluşturduk.."