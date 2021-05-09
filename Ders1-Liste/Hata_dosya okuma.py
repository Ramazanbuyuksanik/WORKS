################ HATA YAKALAMA
# try:
#     sayı =int(input("bir sayı girin: "))
#     kare =sayı**2
#     print(kare)
# except ValueError:
#     print("geçersiz")

# try:
#     sayı1 =int(input("bir sayı girin: "))
#     sayı2 = int(input("2. sayı girin: "))
#     sonuc=sayı1/sayı2
#     print(sonuc)
#
# except (ValueError, ZeroDivisionError) as hata:
#     print("geçersiz", hata)

######################### dosyas hatası
# try:
#     dosya=open("deneme.txt","r")
# except IOError:
#     print("hata")
# finally:
#     dosya.close()

###################### dosya okuma

# dosya = open ("notlar.txt")

# for notlar in dosya.readlines():
#     print(notlar)
# dosya.close()
########### close kullanmadan açma kapama
# with open("notlar.txt") as dosya:
#     print (dosya.read())
############bilgi ekleme
# with open("notlar.txt","a") as dosya:
#     dosya.write("\nburak 100") #### PRint etme ?????
########### başa ekleme
# with open("notlar.txt","r+") as dosya:
#     x=dosya.read()
#     dosya.seek(0)

#     dosya.write("burak 100\n")
#     print(dosya.read())
# #################
with open("notlar.txt","r+") as dosya:
   veri=dosya.readlines()
   veri.insert(1,"ali 33\n")
   dosya.seek(0)
   dosya.writelines(veri)



