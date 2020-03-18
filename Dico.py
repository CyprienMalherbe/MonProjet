echiquier = {}
echiquier['a', 1] = "tour blanche" # En bas à gauche de l'échiquier
echiquier['b', 1] = "cavalier blanc" # À droite de la tour
echiquier['c', 1] = "fou blanc" # À droite du cavalier
echiquier['d', 1] = "reine blanche" # À droite du fou
# ... Première ligne des blancs
echiquier['a', 2] = "pion blanc" # Devant la tour
echiquier['b', 2] = "pion blanc" # Devant le cavalier, à droite du pion
# ... Seconde ligne des blancs

print(echiquier)

fruits = {"pommes":21, "melons":3, "poires":31}
for cle in fruits.keys():
    print(cle)

print(fruits.keys())

def fonction_inconnue(**parametres_nommes):
    """Fonction permettant de voir comment récupérer les paramètres nommés
    dans un dictionnaire"""
    print("J'ai reçu en paramètres nommés : {}.".format(parametres_nommes))
    print(type(parametres_nommes))
    print(parametres_nommes)

fonction_inconnue() # Aucun paramètre

fonction_inconnue(p=4, j=8)

parametres = {"sep":" >> ", "end":" -\n"}

print("Voici", "un", "exemple", "d'appel", **parametres)

help(print)