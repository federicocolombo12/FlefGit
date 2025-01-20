stringa1=input("Inserisci la prima stringa: ")
set1=set(stringa1)

stringa2=input("Inserisci la seconda stringa: ")
set2=set(stringa2)
setIntersezione=set1.intersection(set2)
setDifferenza1=set1.difference(setIntersezione)
setDifferenza2=set2.difference(setIntersezione)
alfabetoSet=set("abcdefghijklmnopqrstuvwxyz")
alfaDifferenza=alfabetoSet.difference(set1).difference(set2)


print("L'intersezione è: ",setIntersezione)
print("La differenza della prima stringa è: ",setDifferenza1)
print("La differenza della seconda stringa è: ",setDifferenza2)
print("Le lettere dell'alfabeto non presenti in nessuna delle due stringhe sono: ",alfaDifferenza)