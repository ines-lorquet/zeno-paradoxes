from display import Display_para


class Achille(Display_para):
    def __init__(self):
        super().__init__()

    def achille_tortue(self):
        pos_a = 0
        pos_t = 15
        vit_a = 2
        vit_t = 1

        while pos_a < 28:
            A = int(pos_a)
            T = int(pos_t)
            self.display_terminal(A, T)
            tp_a = (pos_t - pos_a) / vit_a
            pos_a = pos_t
            pos_t = pos_t + (vit_t * tp_a)


test = Achille()
test.achille_tortue()
