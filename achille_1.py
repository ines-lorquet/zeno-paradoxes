def achi_tort():
    A, T = 0, 5
    while A != 15:
        A, T = T, T + T // 2
        print(A, T)
        run = "________________"
        step = list(run)
        step.insert(A, "A")
        step.insert(T, "T")
        print(''.join(step))

achi_tort()