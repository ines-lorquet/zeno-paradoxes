Position_A = 0
Position_T = 10
 
for i in range (50):
    Distance = (Position_T-Position_A)
    Position_A = Position_A + (Distance // 2)
        
    print("Distance: ", Distance)
    print("Voici la position d'Achille: ", Position_A)
    print("Voici la position de la tortue: ", Position_T)
