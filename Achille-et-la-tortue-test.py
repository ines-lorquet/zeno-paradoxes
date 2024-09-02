Vitesse_A = 2
Vitesse_T = 1
Position_A = 0
Position_T = 15
 
for i in range (20):
    temps_A = (Position_T-Position_A) / Vitesse_A
    Position_A = Position_T
    Position_T = Position_T + (Vitesse_T * temps_A)
    Ecart = Position_T-Position_A
    
    print("Etape", ( i + 1))
    print("Voici la position d'Achille: ", Position_A)
    print("Voici la position de la tortue: ", Position_T)
    print("Ecart: ", Ecart)
