class Çalışan() :
    def __init__(self,isim,maaş,departman) :
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgileriGoster(self):

        print("Çalışan sınıfının bilgileri....")
        print("İsim : {} \nMaaş : {}\nDepartman : {}\n".format(self.isim,self.maaş,self.departman))
    def departman_degıstır(self,yeni_departman):
        self.departman = yeni_departman
        print("Departman Değişiyor...")
class Yönetici_Sınıfı(Çalışan):
    pass
yönetici = Yönetici_Sınıfı("Yavuzhan",5000,"yazılım")
yönetici.bilgileriGoster()
yönetici.departman_degıstır("INSAN KAYNAKLARI")

