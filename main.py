import random


def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"Quel est le nombre magisue (entre {nb_min} et {nb_max}) ? ")
        try:
            nombre_int = int(nombre_str)

        except ValueError:
            print("Erreur: Vous devez rentrer un nombre. Réessayez!")
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"Erreur: Vous devez rentrer un nombre compris (entre {nb_min} et {nb_max}). Réessayez!")
                nombre_int = 0

    return nombre_int


NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE8MAGIQUE = random.randint(1,10)

nombre = 0

while not nombre == NOMBRE8MAGIQUE:
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE8MAGIQUE:
        print("felicitations, vous avez gagné! \nLe nombre magique est bel et bien égal à " + str(nombre))

    elif nombre > NOMBRE8MAGIQUE:
        print("le nombre magique est plus petit que " + str(nombre))

    elif nombre < NOMBRE8MAGIQUE:
        print("le nombre magique est plus grand que " + str(nombre))
    else:
        print("Veillez entrer un nombre!")
