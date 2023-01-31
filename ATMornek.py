print("""

İşlemler;
1 . Bakiye sorgulama 
2 . Para Yatırma 
3 . Para Çekme

Programdan ÇIKMAK İÇİN q ya basın.....
""")

bakiye = 1000

while True : 
    
    işlem = input("Yapacağınız İşlemi SEÇİNİZ :")

    if (işlem == "q" ):
        print("Gene BEKLERİZ")
        break

    elif (işlem== "1"):

        print("Bakiyeniz {}} tl dir".format(bakiye))

    elif (işlem== "2" ) :

        miktar = int(input("Miktarı Giriniz:" ))

        bakiye += miktar

    elif (işlem== "3" ) : 
        miktar = int(input("Miktarı Giriniz:"))

        if(bakiye-miktar<0) :

            print("Böyle bir miktar çekemezsin")

            continue

        bakiye-= miktar

    else:
        print("Geçersiz İşlem")               
