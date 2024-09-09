# class Paradoxe(Display_para):
#     def __init__(self):
#         super().__init__()

#     def achille_tortue(self):
#         pos_a = 0
#         pos_t = 15
#         vit_a = 2
#         vit_t = 1

#         while pos_a < 28:
#             A = int(pos_a)
#             T = int(pos_t)
#             self.display_terminal(A, T)
#             tp_a = (pos_t - pos_a) / vit_a
#             pos_a = pos_t
#             pos_t = pos_t + (vit_t * tp_a)

#     def dichotomie(self):
#         a = 0
#         b = 15

#         for _ in range(28):
#             B = int(b)
#             print(B)
#             self.display_terminal_1(B)
#             tp_a = (b - a) / 2
#             a = b
#             b = b + (1 * tp_a)


# para = Paradoxe()
# # para.achille_tortue()
# para.dichotomie()
