import random
import tkinter as tk
from tkinter import messagebox
s = 0
def BJtkinter():
    # Définition des cartes
    famille_carte = ['Coeurs', 'Piques', 'Carreaux', 'Trèfles']
    liste_carte = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Reine', 'Roi']
    deck = [(famille, carte) for famille in famille_carte for carte in liste_carte]

    # Mélange du deck
    random.shuffle(deck)

    # Main du joueur et du croupier
    carte_j = [deck.pop(), deck.pop()]
    carte_d = [deck.pop(), deck.pop()]

    # Definition de la valeur des cartes
    def valeur_cartes(carte):
        if carte[1] in ['Valet', 'Reine', 'Roi']:
            return 10
        elif carte[1] == 'As':
            return 11
        else:
            return int(carte[1])
     # fonction de calcul du score
    def calculer_score(main):
        return sum(valeur_cartes(carte) for carte in main)

    def afficher_resultat():
        score_j = calculer_score(carte_j)
        score_d = calculer_score(carte_d)

        if score_j > 21:
            messagebox.showinfo("Résultat", "Le croupier gagne !")
            s = 0
        elif score_d > 21:
            messagebox.showinfo("Résultat", "Le joueur gagne !")
            s = 1
        elif score_j > score_d:
            messagebox.showinfo("Résultat", "Le joueur gagne !")
            s=1
        elif score_d > score_j:
            messagebox.showinfo("Résultat", "Le croupier gagne !")
            s=0
        else:
            messagebox.showinfo("Résultat", "Égalité !")


    def tirer_carte():
        carte_j.append(deck.pop())
        score_j = calculer_score(carte_j)
        label_joueur.config(text=f"Main du joueur: {carte_j}\nScore: {score_j}")
        if score_j > 21:
            afficher_resultat()


    def arreter():
        score_d = calculer_score(carte_d)
        while score_d < 15:
            carte_d.append(deck.pop())
            score_d = calculer_score(carte_d)
        label_croupier.config(text=f"Main du croupier: {carte_d}\nScore: {score_d}")
        afficher_resultat()




    # Création de la fenêtre Tkinter
    root = tk.Tk()
    root.title("Blackjack")
    root.geometry("600x400")

    frame = tk.Frame(root)
    frame.pack(pady=20)

    label_joueur = tk.Label(frame, text=f"Main du joueur: {carte_j}\nScore: {calculer_score(carte_j)}", font=("Rod", 14))
    label_joueur.pack()

    label_croupier = tk.Label(frame, text=f"Main du croupier: {carte_d[:1]} et une carte cachée", font=("Rod", 14))
    label_croupier.pack()

    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    btn_tirer = tk.Button(button_frame, text="Tirer une carte", command=tirer_carte, font=("Rod", 12), width=15)
    btn_tirer.grid(row=2, column=0, padx=10)

    btn_arreter = tk.Button(button_frame, text="Arrêter", command=arreter, font=("Rod", 12), width=15)
    btn_arreter.grid(row=2, column=2, padx=10)

    btn_quitter = tk.Button(button_frame, text="Quitter", command=root.destroy, font=("Rod", 12), width=15)
    btn_quitter.grid(row=2, column=3, padx=10)
    root.mainloop()

    return s
BJtkinter()
