numérateur=10
dénominateur=0

try :
    résultat=numérateur/dénominateur
    print("Le résultat est :", résultat)
except NameError as ExceptionRetournée :
    print("Voici l'erreur :", ExceptionRetournée)
except ZeroDivisionError as ExceptionRetournée :
    print("Voici l'erreur :", ExceptionRetournée)
    