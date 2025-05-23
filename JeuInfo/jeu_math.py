import random
import tkinter as tk
from tkinter import messagebox

def Jeu_traitre():
    window = tk.Tk()
    window.title("Jeu du Traître")
    window.geometry("600x400")
    window.configure(background="#4e3629")

    traitre = random.randint(1, 200)  # Genere le premier traitre

    # Fonction permettant de trouver le traitre avec encapsulation ( toutes les fonctions ne fonctionneront sur dans Jeu_traitre)
    def trv_traitre():
        try:
            suspect = int(entry.get())  # Enregistre la valeur donnée par le joueur
            if suspect < traitre:
                result_label.config(text=f"Plus grand que {suspect}", fg="#ffd700")  # Indique si cest plus grand
            elif suspect > traitre:
                result_label.config(text=f"Moins que {suspect}", fg="#ff0000")  # Indique si cest plus petit
            elif suspect == traitre:
                result_label.config(text="Félicitations! Vous avez trouvé le traitre!", fg="#d4af37")
                messagebox.showinfo("Victoire!", "Vous avez trouvé le traitre!")
                start_button.config(state="normal")
                entry.config(state="disabled") # Désactive les bontons
                guess_button.config(state="disabled")  # Désactive les bontons
        except ValueError:
            result_label.config(text="Veuillez entrer un nombre valide.", fg="#f1e1c6")  # Verifie si l'information entrée est bien un nombre

    # Fonction permettant de recommencer
    def restart_game():
        nonlocal traitre  # Permet de modifier la variable "traitre" hors de cette fonction
        traitre = random.randint(1, 200)  # Genere un traitre
        entry.config(state="normal")
        guess_button.config(state="normal")
        result_label.config(text="")  # Efface la valeur du traitre
        start_button.config(state="disabled")
    Police_med=("Garamond", 14,"bold")
    # Affiche les instructions
    instruction_label = tk.Label(window, text="Devinez quel est le traitre (un nombre entre 1 et 200)!", font=Police_med, fg="#f42300", bg="#4e3629")
    instruction_label.pack(pady=10)

    entry = tk.Entry(window)
    entry.pack(pady=10)

    guess_button = tk.Button(window, text="Deviner", command=trv_traitre)
    guess_button.pack(pady=5)

    result_label = tk.Label(window, text="")
    result_label.pack(pady=10)

    # Defini le bouton pour recommencer si besoin
    start_button = tk.Button(window, text="Commencer un nouveau jeu", command=restart_game)
    start_button.pack(pady=20)


    window.mainloop() # Ouvre la fenetree


Jeu_traitre() # Lance le Jeu
