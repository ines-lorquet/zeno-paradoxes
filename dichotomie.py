def distance(n):
    caillou = 0
    arbre = 8
    diviseur = 2
    score = 0
    for i in range (1, n) : 
        caillou = arbre / diviseur
        diviseur *= 2
        print ("Voici la distance restante :" , caillou)

n = int(input("Entrez le nombre d’itération que vous voulez effectuer : "))
distance(n)