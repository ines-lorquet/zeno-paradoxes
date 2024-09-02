Cible = 50
Fleche = 0
Vitesse = 5

for i in range(10):
    Tir = Fleche + Vitesse
    Fleche =  Tir
    Ecart = Cible - Tir
    
    print ("Etape", (i + 1))
    print ("Position fleche", Fleche)
    print ("Ecart avec la cible", Ecart)

