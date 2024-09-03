def display(pos_1, pos_2):
    run = "____________________________"
    step = list(run)
    step.insert(pos_1, "1")
    step.insert(pos_2, "0")
    print("".join(step))


def achille_tortue():
    pos_a = 0
    pos_t = 15
    vit_a = 2
    vit_t = 1

    while pos_a < 28:
        A = int(pos_a)
        T = int(pos_t)
        display(A, T)
        tp_a = (pos_t - pos_a) / vit_a
        pos_a = pos_t
        pos_t = pos_t + (vit_t * tp_a)


achille_tortue()
