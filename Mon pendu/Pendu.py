MotChoisi = "Bonjour"
LettreChoisie = 0
while type(LettreChoisie) != str:
    print(MotChoisi)
    LettreChoisie = input("Veuillez choisir une lettre ")
    try:
        LettreChoisie = int(LettreChoisie)
    except ValueError:
        print("Ah ouai byebye !!!")
