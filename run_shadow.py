#!/usr/bin/env -S python3 -B
import os
from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr
from os import listdir


tk = TkDrawer()
try:
    for name in os.listdir("data"):
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        Polyedr(f"data/{name}").draw(tk)
        delta_time = time() - start_time
        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
