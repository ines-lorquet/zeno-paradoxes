from termcolor import colored
import time
import math

# Valeurs 
Vitesse_A = 2
Vitesse_T = 1
Position_A = 0
Position_T = 15

display = 156

# Logique d’affichage graphique

for i in range (0, 10):
    temps_A = (Position_T-Position_A) / Vitesse_A
    Position_A = Position_T
    Position_T = Position_T + (Vitesse_T * temps_A)

    # Il faut arrondir les calculs pour permettre l’affichage graphique

    pos_A = math.ceil(Position_A)
    pos_T = math.ceil(Position_T)

    liste = ['#'] * display

    if Position_A==Position_T :
        liste[pos_A] = colored('X', 'yellow')
    else : 
        liste[pos_A] = colored('A', "red")
        liste[pos_T] = colored('T', "green")
    print(''.join(liste))
    time.sleep(0.5)

print("fin de la simulation")
