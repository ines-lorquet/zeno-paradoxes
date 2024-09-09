position_tree = 8
position_rock = 0

for i in range(10):
    throw = (position_tree-position_rock)/2
    position_rock = position_rock + throw
    
    print("Etape", (i + 1))
    print("Position de la pierre : ", position_rock)
    print("Ecart : ",position_tree - position_rock)
