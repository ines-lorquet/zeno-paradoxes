position_arbre = 8
position_pierre = 0

for i in range(10):
    lancer = (position_arbre-position_pierre)/2
    position_pierre = position_pierre + lancer
    
    print("Etape", (i + 1))
    print("Position pierre : ", position_pierre)
    print("Ecart : ",position_arbre - position_pierre)
