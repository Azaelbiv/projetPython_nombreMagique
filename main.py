def myfunction(food):
    for x in food:
        print(x)


fruits = ["mangues", "fraises", "bananes", "oranges", "ananas"]
myfunction(fruits)

print(type(fruits))


# la fonction recursive
def tri_recusive(k):
    if k > 0:
        resultat = k + tri_recusive(k - 1)
        print(resultat)
    else:
        resultat = 0
        return resultat


#tri_recusive(4)

# la fonction lambda(c'est une petite fonction anonime de la forme: lambda argument : expression)

x = lambda nbre: nbre + 4
reponse = x(7)
print(f"la reponse de la valeur de lambda est : {reponse} ")


def lambdafunct(n):
    print()
    return lambda x: x * n


ledouble = lambdafunct(2)
letriple = lambdafunct(3)
print("le double de " + str(reponse) + " est " + str(ledouble(reponse)))
print("le triple de " + str(reponse) + " est " + str(letriple(reponse)))



"""import numpy as np
import matplotlib.pyplot as plt

tab1 = np.array([[1, 2, 3, 4], [2, 5, 3, 7]])
tab2 = np.array([[4, 1, 2, 5], [8, 3, 6, 1]])
a = tab2.T
print(a)
print(tab1, "\n", tab2)
print(np.dot(tab1, a))
print(tab1@a)


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
