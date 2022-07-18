LISTE_OBJETS = [{"nom": "Lampe","taille" : 4,"pts": 10},
                {"nom": "Bibliothèque", "taille": 6,"pts": 5},
                {'nom': "Globe Terrestre", "taille": 4, "pts": 1},
                {"nom": "Bureau", "taille": 6, "pts": 20},
                {"nom": "Commode", "taille": 6, "pts": 2},
                {"nom": "Guéridon", "taille": 4, "pts" : 5},
                {"nom": "Vase", "taille": 4, "pts": 1},
                {"nom": "Petite table", "taille": 4, "pts": 5},
                {"nom": "Coffre", "taille": 4, "pts": 2},
                {"nom": "Lit double", "taille": 9, "pts": 50}
                ]

def points_d_utilites(objet):
    """
    Renvoie le nombre de points d’utilités d’un objet
    :param objet : (dict) représentant un objet
    :return: (int) le nombre de points d'utilités
    """
    return objet['pts']

def trier_liste(liste_objets) :
    """ 
    """
    return sorted(liste_objets, key=points_d_utilites, reverse=True)
        
        
def choix_objets (surface, liste_objets) :
    """
    :param surface: (int) la surface disponible
    :param objets: (list) des objets disponnible
    :return:(tuple) le couple composé de la liste contenant les noms des objets et le score d'utilité total
    """
    pass