import tkinter as tk
from tkinter import messagebox
import random

def dobas(dobasok):
    eredmenyek = [0 for _ in range(7)]
    for _ in range(dobasok):
        szam = random.randint(1, 6)
        eredmenyek[szam] += 1
    eredmeny_cimke.set(
        f"1 - {eredmenyek[1]}\n"
        f"2 - {eredmenyek[2]}\n"
        f"3 - {eredmenyek[3]}\n"
        f"4 - {eredmenyek[4]}\n"
        f"5 - {eredmenyek[5]}\n"
        f"6 - {eredmenyek[6]}"
    )
    #print(eredmenyek)
    #eredmeny_cimke.set(f"A dobás: {szam}")

def on_dobas():
    try:
        dobasok_szama = int(dobasok_szama_bemenet.get())
        dobas(dobasok_szama)
    except ValueError:
        messagebox.showerror("Hiba", "Rossz értéket adtál meg.")

root = tk.Tk()
root.title("Kockadobások statisztikája")
root.geometry("600x400")

cim = tk.Label(root, text="Kattints a gombra!", font=("Arial", 16))
cim.grid(row=0, column=1, pady=20)
#cim.pack(pady = 30)


dobasok_szama_bemenet = tk.StringVar(value="10")
dobasszam = tk.Entry(root, textvariable = dobasok_szama_bemenet, width=10)
dobasszam.grid(row=1, column=0, pady=20, padx=50)
#dobasszam.pack(pady = 10)

gomb = tk.Button(root, text="Dobás", command=on_dobas)
gomb.grid(row=1, column=2, pady=20)
#gomb.pack()

eredmeny_cimke = tk.StringVar(value = ".....")
eredmeny = tk.Label(root, textvariable = eredmeny_cimke, font=("Arial", 16))
eredmeny.grid(row=2, column=1, pady=20)
#eredmeny.pack(pady = 20)

kilepes = tk.Button(root, text="Kilépés", command=root.destroy, bg="red")
kilepes.grid(row=3, column=1, pady=20)
#kilepes.pack()

tk.mainloop()
