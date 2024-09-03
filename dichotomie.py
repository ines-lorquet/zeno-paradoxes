def dichotomie_antoine(n):
    caillou = 0
    arbre = 8
    diviseur = 2
    score = 0
    for i in range (1, n) : 
        caillou = arbre / diviseur
        diviseur *= 2
        score = score + 1
        print (score , "Voici la distance restante :" , caillou)

# n = int(input("Entrez le nombre d’itération que vous voulez effectuer : "))
# dichotomie_antoine(n)

def tortue_antoine_v0(n):
    achille = 0
    tortue = 4
    temps = 0
    iteration = 2
    ecart = 0
    for i in range (1, n) :
        iteration *= 2
        print("itération : ", iteration)
        ecart = (tortue - achille) / 2 ** iteration
        print("écart : ", ecart)
        achille = tortue
        print("achille : ",achille)
        tortue = achille + ecart
        print("tortue : ",tortue)
        print(f"Achille est à {achille} mètres et la Tortue est à {tortue} mètres.")

n = int(input("Entrez le nombre d’itération que vous voulez effectuer : "))
tortue_antoine_v0(n)