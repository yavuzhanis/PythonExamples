#Bu örneğimizde Python ile hesap makinesi kodlanacaktır.
def toplama(sayı1,sayı2):
    return sayı1+sayı2

def cikarma(sayı1,sayı2):
    return sayı1-sayı2
def carpma(sayı1,sayı2):
    return sayı1*sayı2
def bolme (sayı1,sayı2):
    return sayı1/sayı2

islemTipi = {
    "+" :toplama,
    "-":cikarma,
    "*":carpma,
    "/":bolme
}
def hesapMakinesi():
    for simge in islemTipi:
        print(f"{simge}")
    devam = True

    while devam :
        secilenSimge = input("Yapmak istediğiniz işlem tipini seçiniz:\n")
        sayı1 = int(input("Birinci sayıyı giriniz:"))
        sayı2 = int(input("ikinci sayıyı giriniz:"))
        hesaplama = islemTipi[secilenSimge]
        cevap= hesaplama(sayı1,sayı2)
        print(f"{sayı1} {secilenSimge} {sayı2} = {cevap}")

        son = input("Yeni bir işlem yapmak ister misiniz ? 'evet','hayır'\n")
        if son == "evet" :
            devam = True
        else:
            devam = False
hesapMakinesi()





