from random import randint
from src.JustePrix import comparer, peut_jouer
# Le juste prix !

'''
    Le but du juste prix est de permettre à un joueur de proposer un nombre et on doit lui dire si le nombre à deviné correspond à son nombre.
    Si non on lui indique si c'est plus ou moins

    Il a un nombre d'essai limité
'''

juste_prix = randint(0, 1000)

nombre_du_joueur = 0

nombre_tentative = 0
tentative_max = 10

# tant que mon joueur peut jouer
while peut_jouer(nombre_tentative, tentative_max):
    # on demande le nombre au joueur
    nombre_du_joueur = input(f'essai {nombre_tentative + 1} Deviner le nombre:')
    # génération du message
    message = comparer(nombre_du_joueur, juste_prix)
    # affichage
    print(message)
    if message == "C'est gagné":
        break
    # incrémentation du nombre de tentative
    nombre_tentative += 1

