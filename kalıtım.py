class Çalışan() :
    def __init__(self,isim,maaş,departman) :
        print("Çalışan sınıfının init fonskiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigoster(self):

        print("Çalışan sınıfının bilgileri...")

        print("İsim : {} \nMaaş : {}  \nDepartman : {}\n".format(self.isim,self.maaş,self.departman))
    def departman_degistir(self,yeni_departman):
        print("Departman değişiyor...")
        self.departman = yeni_departman

class Yönetici(Çalışan):
    pass

yönetici =Yönetici("Yavuzhan",4334 ,"Yazılım")
yönetici.bilgilerigoster()
yönetici.departman_degistir("İnsan Kaynakları")
yönetici.bilgilerigoster()
"""
class Yönetici(Çalışan):
    def zam_yap(self,zam_miktarı):
        self.maaş += zam_miktarı
        yönetici =Yönetici("Yavuzhan",4334 ,"Yazılım")
        yönetici.zam_yap[5353]
        yönetici.bilgilerigoster()
"""
# Yönetici zam yapmak için yukarıdaki kod yuvarlamalarını kullancaktır .


        