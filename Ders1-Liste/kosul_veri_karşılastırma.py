############if else

# puan= int (input("puan giriniz: "))
# if puan >=50:
#     print('gectiniz')
# else:
#     print('tekrar dene')

######### if and elif
# sayi= int(input("sayi girin"))
# if sayi <=100:
#     print('sayi 100 den kucuk')
# elif sayi>= 500:
#     print('sayi 500 den buyuk')
# else:
#     print('sayi 100 ile 500 arasinda')

###########   boolean AND  OR  #################
# ali=True
# velu= False
# if ali or velu:
#     print('dogru')
# else:
#     print('yanlis')
#
# print(not(ali))
#################            KARSILASTIRMA (=<>)           ###############
# parola=12345
# sifre = input('sifre gir')
# if parola==sifre:
#     print('dogru')
# else:
#     print('yanlis')
#########################
# say1= input('sayi 1 gir: ')
# say2= input('sayi 2 gir: ')
# say3= input('sayi 3 gir: ')
# def buyuk(say1,say2,say3):
#     if say1>=say2 and say1>=say3:
#         return say1
#     elif say2>=say1 and say2>=say3:
#         return say2
#     else:
#         return say3
# print(buyuk(say1,say2,say3))
######################### Dictionary Sozluk    ############
dil={'ali': 'almanca', 'veli': ' fransizca'}
print(dil['ali'])
dil['ayse']= 'rusca'
print(dil)
del (dil['ali'])
print(dil)
print(dil.keys(), dil.values(),dil.items(),dil.get('veli'))


