position_tree = 8
position_rock = 0

for i in range(10):
    throw = (position_tree-position_rock)/2
    position_rock = position_rock + throw
    
    print("Step", (i + 1))
    print("Rock position: ", position_rock)
    print("Difference : ",position_tree - position_rock)
