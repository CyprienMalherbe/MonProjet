liste_origine = [0, 1, 2, 3, 4, 5]
print([nb * nb for nb in liste_origine])

liste_origine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
MaListe = [nb for nb in liste_origine if nb % 2 == 0]
print(MaListe)

qtt_a_retirer = 7 # On retire chaque semaine 7 fruits de chaque sorte
fruits_stockes = [15, 3, 18, 21] # Par exemple 15 pommes, 3 melons...
MaNouvelleListe = [nb_fruits-qtt_a_retirer for nb_fruits in fruits_stockes if nb_fruits>qtt_a_retirer]

print(MaNouvelleListe)


inventaire = [
     ("pommes", 22),
     ("melons", 4),
     ("poires", 18),
     ("fraises", 76),
     ("prunes", 51),
 ]

""">>> autre_liste = [
...     [1, 'a'],
...     [4, 'd'],
...     [7, 'g'],
...     [26, 'z'],
... ] # J'ai étalé la liste sur plusieurs lignes
>>> for nb, lettre in autre_liste:
...     print("La lettre {} est la {}e de l'alphabet.".format(lettre, nb))
... 
La lettre a est la 1e de l'alphabet.
La lettre d est la 4e de l'alphabet.
La lettre g est la 7e de l'alphabet.
La lettre z est la 26e de l'alphabet.
>>>"""

NouvelInventaire = [(nb,fruits) for fruits, nb in inventaire]
print(NouvelInventaire)
InventaireRetourné = sorted(NouvelInventaire, reverse=True)
InventaireTrié = [(fruits, nb) for nb, fruits in InventaireRetourné]

print(InventaireTrié)

#for fruits, nb in inventaire:
#    NouvelInventaire = [nb,fruits]
#    print(NouvelInventaire)

#NouvelInventaire = [nb, fruits for fruits in inventaire]

#print(NouvelInventaire)

#InventaireTrié = sorted(NouvelInventaire)

#print(InventaireTrié)