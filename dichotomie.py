Arbre = 8
Pierre = 0

for i in range(10):
    Lancer = (Arbre-Pierre)/2
    Pierre = Pierre + Lancer
    print("Etape", (i + 1))
    print("Position pierre : ", Pierre)
    print("Ecart: ",Arbre - Pierre )
