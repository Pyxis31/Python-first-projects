import os

def afficher_flottant(flottant):
    if type(flottant) is not float:
        raise TypeError
    flottant=str(flottant)
    # La méthode split éclate le flottant en deux chaînes autour du séparateur "."
    partie_entière,partie_flottante=flottant.split(".")
    # La méthode join réunit les deux chaînes (concatène)
    # [:2] sélectionne une partie de la chaîne (2 premiers caractères). Voir page 107.
    print(",".join([partie_entière,partie_flottante[:2]]))
 

# Autotest de la fonction
if __name__ == "__main__":
    afficher_flottant(3.1415927)
    os.system("pause")
