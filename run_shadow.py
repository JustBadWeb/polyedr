#!/usr/bin/env -S python3 -B
import os
from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr


tk = TkDrawer()
try:
    for name in os.listdir("data"):
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        p = Polyedr(f"data/{name}")
        p.draw(tk)
        print(f"сумма длин проекций полностью невидимых рёбер, "
              f"проекция центра которых находится на расстоянии "
              f"строго меньше 1 от прямой x=2 = {p.X}")
        delta_time = time() - start_time
        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
