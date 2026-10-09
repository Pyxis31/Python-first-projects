def afficher(*paramètres,sep=' ',fin='\n'):
    """ Fonction reproduisant le comportement de print """
    
    # Tranformation du tuple (liste des paramètres) en liste pour le modifier
    paramètres=list(paramètres)
    
    # Convertion des valeurs en chaînes
    for i, élément in enumerate(paramètres):
        paramètres[i]=str(élément)
    
    # Chaîne finale
    chaîne=sep.join(paramètres)
    
    # Ajout du paramètre de fin
    chaîne+=fin
    
    # On affiche l'ensemble
    print(chaîne,end='')
    
    
             