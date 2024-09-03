from termcolor import cprint, colored

def tortue_sul(n) : 
    Vitesse_A = 2
    Vitesse_T = 1
    Position_A = 0
    Position_T = 15
    
    for i in range (0, n):
        temps_A = (Position_T-Position_A) / Vitesse_A
        Position_A = Position_T
        Position_T = Position_T + (Vitesse_T * temps_A)
        Ecart = Position_T-Position_A
        print(colored("Etape", "green", attrs=["bold"]), colored(i + 1, "green"))
        print(colored("Voici la position d'Achille: ", "yellow"), colored(Position_A, "yellow"))
        print(colored("Voici la position de la tortue: ", "magenta"), colored(Position_T, "magenta"))
        print(colored("Ecart: ", "red", attrs=["bold"]), colored(Ecart, "red"))

n = int(input(colored("Entrez le nombre d’itération que vous voulez effectuer : ", "cyan", attrs=["bold"])))

tortue_sul(n)