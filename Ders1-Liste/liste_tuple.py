import random
import math
# my_List = [i for i in range(10)]    # List comprehension!!! [0,1,2,3,4,5,6,7,8,9]
# print(my_List)

# popped_item = my_List.pop(0)
# print(my_List)

# sinema_izleyiciler = ['Ramazan', 'Burak', 'ahmet', 'Mehmet', 'James']

# for _ in range(len(sinema_izleyiciler)):
#     giren_izleyici = random.choice(sinema_izleyiciler)
#     print(giren_izleyici+' parasini odedi.. Iyi seyirler..')
#     sinema_izleyiciler.remove(giren_izleyici)
# print(sinema_izleyiciler)

# sayimiz = 13
# for _ in range(8):
#     sayimiz += 1
#     print(f'Sayimiz suan : {sayimiz}')
# print(f'son sayi: {sayimiz}')


# karekoksuz_liste = [i for i in range(100) if i != 0 ]
# karekoksuz_liste = [i for i in range(100)]
# karekoklu_liste = []

# for rakam in karekoksuz_liste:
#     check_rakam = math.sqrt(rakam)
#     if check_rakam - int(check_rakam) == 0 and check_rakam!=0:
#         karekoklu_liste.append(check_rakam)
# print(karekoklu_liste)
# print(math.sqrt(25))

## TUPLE VS LIST

# TUPLE ->>>>> Immutable {DEGISTIRILEMEZ}
# LIST ->>>>> Mutable {DEGISTIRILEBILIR}


# LISTE ORNEGI
sinema_izleyiciler = ['Ramazan', 'Burak', 'ahmet', 'Mehmet', 'James','James','James','James']

# for _ in range(len(sinema_izleyiciler)):
#     giren_izleyici = random.choice(sinema_izleyiciler)
#     print(giren_izleyici+' parasini odedi.. Iyi seyirler..')
#     sinema_izleyiciler.remove(giren_izleyici)
# sinema_izleyiciler.append("Aybuke")
# print(sinema_izleyiciler)


#  TUPLE ORNEGI

# sinema_izleyiciler = ('Ramazan', 'Burak', 'ahmet', 'Mehmet', 'James')
# for _ in range(len(sinema_izleyiciler)):
#     giren_izleyici = random.choice(sinema_izleyiciler)
#     print(giren_izleyici+' parasini odedi.. Iyi seyirler..')
#     sinema_izleyiciler.remove(giren_izleyici)

# When executed gives error -> AttributeError: 'tuple' object has no attribute 'remove'

# bizim_tuple = set(sinema_izleyiciler)
# # print(type(bizim_tuple))2
# print(sinema_izleyiciler)
# print(bizim_tuple)


# Duplicate element removal

# liste = [1,1,1,1,2,3,4,5,7,7,7,8,8,9,9,9,9,9]
# print(set(liste))