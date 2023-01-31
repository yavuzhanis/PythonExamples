
"""
Python ile pizza siparişi yapabilmemizi sağlayan bir program yazacağız. Program aşağıdaki bilgiler ışığında yazılacaktır:

Kullanıcıdan pizza siparişi için aşağıdaki şekilde ücretlendirme alınacaktır:
Küçük boy (S) pizza: 25 TL
Orta boy (M) pizza: 30 TL
Büyük boy (L) pizza: 35 TL

Ekstra peynirin pizza boyutlarına göre fiyatlandırılması:
Küçük boy (S) pizzaya +2 TL
Büyük boy (L) ve orta boy (M) pizzaya +3 TL

İçecek istiyorsa +2 TL
"""
print("Yavuzhan Pizzaya hoş geldiniz...")
boyut = input('Hangi boyutta pizza istiyorsunuz? "S","M" VEYA "L" :')
ekstra_peynir = input('Ekstra peynir ister misiniz ? "Evet" veya "Hayır":')
ıcecek = input('İçecek alır mısınız ? "Evet" veya "Hayır" :')
hesap = 0

if boyut == "S":
    hesap+=20
elif boyut == "M":
    hesap +=25
else:
    hesap+=30

if ekstra_peynir == "Evet":
    if boyut == "S":
        hesap+=2
    else:
        hesap+=3
if ıcecek == "Evet":
    hesap+=2
print(f"Toplam Tutarı : {hesap} TL.")