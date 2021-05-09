############## kümeler SET
# a="ankara"
# kume=set(a)
# print(kume)
# liste =[1,2,3,4,3,2,1,3,451]
# B =set(liste)
# C= {1,2,3,4,5,6,7,8,9}
# print(B)
# print(kume|B) #### Birlerşim
# print(B&C) ########### kesişim
# print(B-C)  ###### Fark
# print(B^C) #####Simetrik fark

##########

A={2,3,4,5,6,7,8,9}
A.add(22)
print(A)
A.discard(3)
A.remove(2)
print(A)
B={2,3,4,5,6,7,77,66}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))
print(A.issubset(B) )
print(B.issuperset(A))
print(3 in (A))
X= frozenset(B)