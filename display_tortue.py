from termcolor import colored, cprint
import time
import math

# Values
Speed_A = 6
Speed_T = 3
Position_A = 0
Position_T = 40

# Initial position
initial_pos_A = math.ceil(Position_A)
initial_pos_T = math.ceil(Position_T)

display = 156

# Display the initial position before the calculation
display_list = ['.'] * display
display_list[initial_pos_A] = colored('A', "red")
display_list[initial_pos_T] = colored('T', "green")
print(''.join(display_list))
time.sleep(0.7)

# Graphical display logic
for i in range(0, 8):
    time_A = (Position_T - Position_A) / Speed_A
    Position_A = Position_T
    Position_T = Position_T + (Speed_T * time_A)

    # We need to round the calculations to allow graphical display
    pos_A = math.ceil(Position_A)
    pos_T = math.ceil(Position_T)

    display_list = ['.'] * display

    if pos_A == pos_T:
        display_list[pos_A] = colored('X', 'yellow')  
    else:
        display_list[pos_A] = colored('A', "red")  
        display_list[pos_T] = colored('T', "green")  

    print(''.join(display_list))
    time.sleep(0.5)

print("-" * 156)
time.sleep(0.4)
cprint("X", "yellow", end="")
time.sleep(0.4)
print(" Indicates that the distance between the Tortoise and Achilles is extremely small.")
time.sleep(0.4)
cprint("Achilles never manages to overtake the Tortoise…", "magenta")
time.sleep(0.4)
print("-" * 156)
time.sleep(0.4)
cprint("End of simulation", "red")
time.sleep(0.4)
print("-" * 156)
