

def comparer(nombre_du_joueur, juste_prix):
    '''
        Prend le nombre donné par l'utilisateur et donne l'information

        Si le nombre est inférieur à au juste prix on lui c'est plus
        Si le nombre est supérieur à au juste prix on lui c'est moins
        Si le nombre est juste on lui c'est gagné

        params:
            nombre_du_joueur: nombre
            juste_prix: nombre

        return:
            "C'est plus" ou 
            "C'est moins" ou
            "C'est gagné"

    '''
    nombre_du_joueur = int(nombre_du_joueur)

    if nombre_du_joueur == juste_prix:
        return "C'est gagné"
    elif nombre_du_joueur < juste_prix:
        return "C'est plus"
    else:
        return "C'est moins"


def peut_jouer(nombre_tentative, tentative_max):
    '''
        Vérifie que le nombre de tentative de l'utilisateur est inférieur au nombre de tentatives max

        params:
            nombre_tentative
            tentative max
        return
            boolean
    '''
    if nombre_tentative >= tentative_max:
        return False
    else:
        return True
