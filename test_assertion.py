valeur=input("Entrer une valeur > 10 :")
try:
    valeur=int(valeur)
    assert valeur>10 # On s'assure que valeur > 10 sinon exception
except ValueError:
    print("Pas un nombre")
except AssertionError:
    print("Pas > 10")
    