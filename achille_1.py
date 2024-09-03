def display(pos_1,pos_2):
        run = "_______________________________"
        step = list(run)
        step.insert(pos_1, "l")
        step.insert(pos_2, "0")
        print(''.join(step))
          
def achi_tort():
    pos_a = 0 
    pos_t = 5
    vit_a = 2
    vit_t = 1
    while pos_a < 30:
        A = int(pos_a)
        T = int(pos_t)
        print(A,T)
        display(A,T)
        tp_a = (pos_a - pos_t) / vit_a
        pos_a = pos_t
        pos_t += pos_t + (vit_t * tp_a)

achi_tort()
