from math import *

Rayon = input("Quel est le rayon que tu veux entrer? " )
Rayon = int(Rayon)

def Surface(x):
    MonRayon = 4 * pi * x**2
    return MonRayon

print(Surface(Rayon))


def is_father_of_luke():
    Father = input("Ecris Dark Vador gros ")
    if Father == 'Dark Vador':
        return True
    else:
        return False

print(is_father_of_luke())

def ajoute_1(Ajout):
    Ajout += 1
    return Ajout

print(ajoute_1(2))

MonTest = """Salut la famille
Comment c'est? """

print(MonTest)

MonTest2 = """Hello World {:,}""".format(1e4)

print(MonTest2)

def greeting_from_johnny():
    AhQueCoucou = input ("""Ecris ton nom stp """)
    return """Ah que coucou {}""".format(AhQueCoucou)

print(greeting_from_johnny())

ortographe_1 = """St Pierre-des-Corps"""
ortographe_2 = """Saint Pierre Des Corps"""

def OrthographeNormalisée(texte):
    TexteNormalise = texte.replace('St','Saint').lower().replace('-',' ')
    return TexteNormalise

print(OrthographeNormalisée(ortographe_1) == OrthographeNormalisée(ortographe_2))

a = "75_001"
b = "75_002"

PremieresLettresA = a[:3]
PremieresLettresB = b[:3]

print(PremieresLettresA == "75_")
print(PremieresLettresB == "75_")

communes = ['Ajaccio', 'Bastia', 'Bonifacio']
print(communes[-2])

prenoms = ['Ange', 'Bianca', 'Bartolumeu']
if 'Ange' in prenoms:
    print("Wallah")
else:
    print("Nope")


communes = ['Corte', 'Sarente', 'Bastia', 'Ajaccio']
print(communes)
communes.sort() # Triez les communes dans l'ordre alphabétique
communes_in_alphabetical_order = communes
first_three = communes[:3]  # sélectionnez uniquement les trois premières
print(communes_in_alphabetical_order)
print(first_three)

False # écrivez ici un test qui vérifie que 'Bastia' est dans la liste first_three et renvoie un booléen

def Test():
    if "Bastia" in first_three:
        return True
    else:
        return False

print(Test())

print(list("Ah ouai bye bye"))

print("Ah ouaaaii".split("i"))

a = 30,
print(type(a))

a = {1,2,3,4,4,4}

print(type(a))

a.pop()

print(a)

villes_corses = ['Corte', 'Sarente', 'Bastia', 'Ajaccio']
villes_contenant_un_a = ['Bastia', 'Ajaccio', 'Marseille', 'Paris', 'Bordeaux']

print(set(villes_corses).intersection(villes_contenant_un_a))
print(set(villes_corses).union(villes_contenant_un_a))
print(set(villes_contenant_un_a)-set(villes_corses))

a = dict()


print(type(a))


sidekicks = {
    "Aladdin": "Abu",
    "Mulan": "Mushu",
    "Snow White": "Seven dwarves",
    "Cinderella": "Gus"
}

sidekicks2 = {
    "The little mermaid": "Sebastian",
    "Frozen": "Olaf",
    "Peter Pan": "Tinker Bell"
}

sidekicks.update(sidekicks2)
all_sidekicks = sidekicks # dictionnaire qui regroupe les deux
print(all_sidekicks)  # imprimez la liste de tous les sidekicks
print(all_sidekicks.keys())  # imprimez la liste de tous les personnages principaux
print(tuple([all_sidekicks.keys(),all_sidekicks]))  # imprimez un liste de tuples (personnage, sidekick)

Heure = input ("Quelle heure est-il ? ")
Heure = int(Heure)

if Heure > 12:
    print ("Good afternoon")
else:
    print("Good morning")


total = 0


for i,j in [(1,2),(3,1)]:
    total += i**j
    print(total)

print("total =",total)


def fizzbuzz():
    '''fizzbuzz to 16'''
    for x in range(17):
        if x % 3 == 0 and x % 5 == 0:
            print ("fizzbuzz")
        elif x % 3 == 0:
            print("fizz")
        elif x%5 == 0:
            print("buzz")
        else:
            print(x)
        # Ecrivez ici la fonction

fizzbuzz()

print ([ i for i in range(11)])

communes = ['Corte', 'Calvi', 'Bastia', 'Ajaccio', 'Propriano']
départements =  ['Haute-Corse', 'Haute-Corse', 'Haute-Corse', 'Corse-du-Sud', 'Corse-du-Sud']
Dico = {i: j for i,j in zip(communes,départements)} # construisez ici

print(Dico)

print([i if (i%2 == 0) else 0 for i in range (10) ])

print([i if i%3 != 0 or i%5 != 0 else 'fizzbuzz' for i in range(1,16)])

print ([max(str(i), 'fizz' * (i%3==0) + 'buzz' * (i%5==0)) for i in range(1,16) ])

class Youhou():
    "Ouai ouai"
    pass

print(type(Youhou))

print(Youhou)

class myClass():
    my_attr = 1
    
a = myClass()
a.my_attr

print(type(a))

print(a)



class myClass():
    my_attribute = 5
    def add(self, x):
        return x + self.my_attribute

a = myClass()

print(a)

a.add(3)

print(a)

class Clerc:
   heal = 50
   def soigner(self):
      return self.heal * 2

print(Clerc.soigner(self.soigner))