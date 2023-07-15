import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 30)
y1 = np.cos(x)
y2 = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y1, 'b:o')
ax.plot(x, y2, 'r--')
ax.set_title("fonction cosinus et sinus")
ax.plot(x, y1, label="cos(x)")
ax.plot(x, y2, label="sin(x)")
plt.legend()
plt.show()

"""def demander_nombre(nb_min, nb_max):
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
NOMBRE_MAGIQUE = random.randint(1, 10)
NB_VIES = 4
vies = NB_VIES

nombre = 0

while not nombre == NOMBRE_MAGIQUE and vies > 0:
    print(f"Il vous reste {vies} vies.")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("felicitations, vous avez gagné! \nLe nombre magique est bel et bien égal à " + str(nombre))

    elif nombre > NOMBRE_MAGIQUE:
        print("le nombre magique est plus petit que " + str(nombre))
        vies -= 1

    elif nombre < NOMBRE_MAGIQUE:
        print("le nombre magique est plus grand que " + str(nombre))
        vies -= 1
    else:
        print("Veillez entrer un nombre!")
if vies == 0:
    print(f"Vous avez perdu, le nombre magique était bien {NOMBRE_MAGIQUE}")"""
