class Course:

    def __init__(self, vitesse, position):
        self.vitesse = vitesse
        self.position = position

Achille =Course( 5, 0)
Tortue =Course( 1, 15)

for i in range (50):
    temps = (Tortue.position - Achille.position) / Achille.vitesse
    Achille.position = Tortue.position
    Tortue.position = Tortue.position + (Tortue.vitesse * temps)
    ecart = Tortue.position - Achille.position

print("Etape", i+1)
print(Achille.position)
print(Tortue.position)
print(ecart)
