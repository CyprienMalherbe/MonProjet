import os
import pickle

os.chdir("C:/Users/cmalherbe/Desktop/python/")

print(os.getcwd())

mon_fichier = open("fichier.txt", "w")

contenu = mon_fichier.write("\nAh ouai bye bye 4")

print(contenu)

mon_fichier.close()

print(mon_fichier)

print(type(mon_fichier))

AhOuaiByebye = "Ah ouai bye bye"
AhOuaiCarrément = "Ah ouai carrément"

with open('donnees.txt', 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(AhOuaiByebye)
    mon_pickler.dump(AhOuaiCarrément)
# enregistrement

with open('donnees.txt', 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    score_recupere = mon_depickler.load()
    DeuxiemeScore = mon_depickler.load()

print(score_recupere)
print(DeuxiemeScore)
