from termcolor import colored
class Coureur:
    def __init__(self, nom, vitesse, position_initiale):
        self.nom = nom
        self.vitesse = vitesse
        self.position = position_initiale

    def avancer(self, temps):
        self.position += self.vitesse * temps

class Simulation:
    def __init__(self, achille, tortue, iterations):
        self.achille = achille
        self.tortue = tortue
        self.iterations = iterations

    def calculer_temps(self):
        return (self.tortue.position - self.achille.position) / self.achille.vitesse

    def run(self):
        for i in range(self.iterations):
            temps_A = self.calculer_temps()
            self.achille.position = self.tortue.position
            self.tortue.avancer(temps_A)
            ecart = self.tortue.position - self.achille.position

            self.afficher_etape(i + 1, ecart)

    def afficher_etape(self, etape, ecart):
        print(colored("Etape", "green", attrs=["bold"]), colored(etape, "green"))
        print(colored(f"Voici la position d'{self.achille.nom}: ", "yellow"), colored(self.achille.position, "yellow"))
        print(colored(f"Voici la position de la {self.tortue.nom}: ", "magenta"), colored(self.tortue.position, "magenta"))
        print(colored("Ecart: ", "red", attrs=["bold"]), colored(ecart, "red"))

achille = Coureur("Achille", vitesse=2, position_initiale=0)
tortue = Coureur("Tortue", vitesse=1, position_initiale=15)

n = int(input(colored("Entrez le nombre d’itération que vous voulez effectuer : ", "cyan", attrs=["bold"])))

simulation = Simulation(achille, tortue, n)
simulation.run()