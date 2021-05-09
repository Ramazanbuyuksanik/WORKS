############# WHILE   ###########
# kelime ='ramazan'
# tahmin=''
# tah_say=0
# tah_lim=3
# tah_cikis= False
# i=1
# while tahmin!=kelime and not (tah_cikis):
#     if tah_say< tah_lim:
#         tahmin=input('tahmin gir')
#         tah_say+=1
#     else:
#         tah_cikis=True
# if tah_cikis:
#     print('yanlis')
# else:
#     print('tebrikler')
########################## BREAk
# sayac = 0
# while sayac<10:
#     if sayac== 5:
#         break
#     print(sayac)
#     sayac +=1

########### continue
# for sayılar in range (20):
#     if sayılar%3==0:
#         continue
#     print(sayılar)
########### PAS
while True:
    sayı=int(input("bir sayı gır: "))
    if sayı <0:
        pass
    elif sayı==0:
        break
    else:
        print("sayınız: ", sayı)

