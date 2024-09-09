from termcolor import colored, cprint
import time
import math

# Valeurs 
Vitesse_A = 6
Vitesse_T = 3
Position_A = 0
Position_T = 40

# Position initiale
pos_ini_A = math.ceil(Position_A)
pos_ini_T = math.ceil(Position_T)

display = 156

# Affichage de la position initiale avant le calcul
liste = ['.'] * display
liste[pos_ini_A] = colored('A', "red")
liste[pos_ini_T] = colored('T', "green")
print(''.join(liste))
time.sleep(0.7)

# Logique d’affichage graphique
for i in range(0, 8):
    temps_A = (Position_T - Position_A) / Vitesse_A
    Position_A = Position_T
    Position_T = Position_T + (Vitesse_T * temps_A)

    # Il faut arrondir les calculs pour permettre l’affichage graphique
    pos_A = math.ceil(Position_A)
    pos_T = math.ceil(Position_T)

    liste = ['.'] * display

    if pos_A == pos_T:
        liste[pos_A] = colored('X', 'yellow')  
    else:
        liste[pos_A] = colored('A', "red")  
        liste[pos_T] = colored('T', "green")  

    print(''.join(liste))
    time.sleep(0.5)

print("-" * 156)
time.sleep(0.4)
cprint("X", "yellow", end="")
time.sleep(0.4)
print(" Signifie que la valeur entre la Tortue et Achille est extrèmement petite.")
time.sleep(0.4)
cprint("Achille ne parvient jamais à dépasser la Tortue …", "magenta")
time.sleep(0.4)
print("-" * 156)
time.sleep(0.4)
cprint("Fin de la simulation", "red")
time.sleep(0.4)
print("-" * 156)