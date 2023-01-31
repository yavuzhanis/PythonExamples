print("Kullanıcı Girişi programı")
sys_kullanıcı_adı = "yyavuz"
sys_parola = "12345"
gırıs_hakkı = 3

while True :
    kullanıcı_adı = input("Kullancı adı:")
    parola = input("Parola:")
    if(kullanıcı_adı!=sys_kullanıcı_adı and parola==sys_parola) :
        print("Kullanıcı ADI hatalı")
        gırıs_hakkı-= 1 
    elif (kullanıcı_adı == sys_kullanıcı_adı and parola !=sys_parola) :
           print("Parola Hatalı..")
           gırıs_hakkı-= 1 
    elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola) :
           print("Kullanıcı adı ve Parola Hatalı..")
           gırıs_hakkı-= 1 
    else :
        print("sisteme giriş başarılı")
        break

    if(gırıs_hakkı == 0 ) : 
        print("giriş hakkınız bitti")
        break

    