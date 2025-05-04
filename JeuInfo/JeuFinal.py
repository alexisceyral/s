import tkinter as tk
from tkinter import messagebox
import random

# ---------------------------
# Variables globales
# ---------------------------
current_question = 0
score_quiz = 0
main_window = None

# ---------------------------
# Quizz Python
# ---------------------------
questions = [
    {
        "question": "Que permet d'afficher la commande suivante ?\nprint('Hello, World!')",
        "options": ["A", "B", "C"],
        "text_options": {
            "A": "Bonjour, Monde !",
            "B": "'Hello, World!'",
            "C": "Hello, World!"
        },
        "answer": "C"
    },
    {
        "question": "Quel mot-clé est utilisé pour définir une fonction en Python ?",
        "options": ["A", "B", "C", "D"],
        "text_options": {
            "A": "define",
            "B": "function",
            "C": "def",
            "D": "func"
        },
        "answer": "C"
    },
    {
        "question": "Quel est le type de la variable suivante ?\nx = 3.14",
        "options": ["A", "B", "C", "D"],
        "text_options": {
            "A": "int",
            "B": "float",
            "C": "double",
            "D": "str"
        },
        "answer": "B"
    },
    {
        "question": "Quelle est la sortie de ce code ?\nprint(2 * 'Python')",
        "options": ["A", "B", "C", "D"],
        "text_options": {
            "A": "PythonPython",
            "B": "2Python",
            "C": "Python2",
            "D": "Erreur"
        },
        "answer": "A"
    },
    {
        "question": "Comment ajouter un élément à une liste en Python ?",
        "options": ["A", "B", "C", "D"],
        "text_options": {
            "A": "list.append(element)",
            "B": "list.add(element)",
            "C": "list.insert(element)",
            "D": "list.push(element)"
        },
        "answer": "A"
    }
]

def lancer_quizz():
    global current_question, score_quiz
    current_question = 0
    score_quiz = 0
    window = tk.Toplevel(main_window)
    window.title("Quiz Python")
    window.geometry("1200x800")
    selected_option = tk.StringVar()

    def show_question():
        nonlocal selected_option
        selected_option.set(None)
        q = questions[current_question]
        question_label.config(text=q["question"])
        for widget in options_frame.winfo_children():
            widget.destroy()
        for code in q["options"]:
            text = f"{code}) {q['text_options'][code]}"
            rb = tk.Radiobutton(options_frame, text=text, variable=selected_option, value=code, font=("Arial", 15))
            rb.pack(anchor="w")

    def next_question():
        nonlocal selected_option
        global current_question, score_quiz
        selected = selected_option.get()
        if not selected:
            messagebox.showwarning("Attention", "Veuillez choisir une réponse.")
            return
        correct = questions[current_question]["answer"]
        if selected == correct:
            messagebox.showinfo("Bonne réponse", "Bonne réponse.")
            score_quiz += 1
        else :
            messagebox.showinfo("Mauvaise réponse", "Mauvaise réponse.")
        current_question += 1
        if current_question < len(questions):
            show_question()
        else:
            window.destroy()
            if score_quiz >= 3:
                show_scene("noble")
            else:
                show_scene("prison")

    question_label = tk.Label(window, text="", wraplength=550, font=("Arial", 20), justify="left")
    question_label.pack(pady=20)

    options_frame = tk.Frame(window)
    options_frame.pack(pady=10)

    tk.Button(window, text="Suivant", command=next_question).pack(pady=20)
    show_question()

# ---------------------------
# Mots inversés
# ---------------------------
def mots_inverses():
    mots = ["euqitamrofni", "nohtyp", "tnirp"]
    mot = random.choice(mots)
    def verifier():
        entree = entry.get()
        if entree == mot[::-1]:
            messagebox.showinfo("Bravo", "Vous avez réussi à décoder le mot !")
            mot_fen.destroy()
            show_scene("reussite_prison")
        else:
            messagebox.showerror("Erreur", "Ce n'est pas la bonne réponse.")
            mot_fen.destroy()
            show_scene("echec_prison")

    mot_fen = tk.Toplevel(main_window)
    mot_fen.title("Mots Inversés")
    tk.Label(mot_fen, text=f"Mot à décoder : {mot}").pack(pady=10)
    entry = tk.Entry(mot_fen)
    entry.pack()
    tk.Button(mot_fen, text="Vérifier", command=verifier).pack(pady=10)

# ---------------------------
# Blackjack
# ---------------------------
def BJtkinter():
    s = 0
#definiton des valurs de chaques cartes
    def valeur_cartes(carte):
        if carte[1] in ['Valet', 'Reine', 'Roi']:
            return 10
        elif carte[1] == 'As':
            return 11
        else:
            return int(carte[1])
#calcul des valeurs des mains
    def calculer_score(main):
        return sum(valeur_cartes(carte) for carte in main)
#affiche le résultat
    def afficher_resultat():
        score_j = calculer_score(carte_j)
        score_d = calculer_score(carte_d)
        if score_j > 21:
            messagebox.showinfo("Résultat", "Le croupier gagne !")
        elif score_d > 21 or score_j > score_d:
            messagebox.showinfo("Résultat", "Le joueur gagne !")
        else:
            messagebox.showinfo("Résultat", "Le croupier gagne !")
#tire 2 carte et les ajoute à la main
    def tirer_carte():
        carte_j.append(deck.pop())
        label_joueur.config(text=f"Main joueur: {carte_j}\nScore: {calculer_score(carte_j)}")
        if calculer_score(carte_j) > 21:
            afficher_resultat()

    def arreter():
        while calculer_score(carte_d) < 15:
            carte_d.append(deck.pop())
        label_croupier.config(text=f"Croupier: {carte_d}\nScore: {calculer_score(carte_d)}")
        afficher_resultat()

    # Définition des cartes
    famille = ['Coeurs', 'Piques', 'Carreaux', 'Trèfles']
    valeur = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Reine', 'Roi']
    deck = [(f, v) for f in famille for v in valeur]
    # Mélange du deck
    random.shuffle(deck)
    # Main de depart du joueur et du croupier
    carte_j = [deck.pop(), deck.pop()]
    carte_d = [deck.pop(), deck.pop()]

    root = tk.Toplevel(main_window)
    root.title("Blackjack")
    root.geometry("1000x800")

    label_joueur = tk.Label(root, text=f"Main joueur: {carte_j}\nScore: {calculer_score(carte_j)}")
    label_joueur.pack(pady=10)

    label_croupier = tk.Label(root, text="Croupier: Carte visible + carte cachée")
    label_croupier.pack(pady=10)

    tk.Button(root, text="Tirer", command=tirer_carte).pack(pady=5)
    tk.Button(root, text="Arrêter", command=arreter).pack(pady=5)
    tk.Button(root, text="Quitter", command=root.destroy).pack(pady=5)

# ---------------------------
# Jeu du Traître
# ---------------------------
def JeuTraitre():
    traitre = random.randint(1, 200)
    window = tk.Toplevel(main_window)
    window.title("Jeu du Traître")

    def verifier():
        try:
            val = int(entry.get())
            if val < traitre:
                result.config(text="Plus grand")
            elif val > traitre:
                result.config(text="Plus petit")
            else:
                result.config(text="Trouvé !")
                messagebox.showinfo("Victoire", "Vous avez trouvé le traître !")
        except ValueError:
            result.config(text="Nombre invalide")

    tk.Label(window, text="Devinez un nombre entre 1 et 200").pack(pady=10)
    entry = tk.Entry(window)
    entry.pack()
    result = tk.Label(window, text="")
    result.pack()
    tk.Button(window, text="Deviner", command=verifier).pack(pady=10)

# ---------------------------
# Scènes
# ---------------------------
def show_scene(scene):
    for widget in main_window.winfo_children():
        widget.destroy()

    def add_button(text, cmd):
        tk.Button(main_window, text=text, command=cmd, font=("Helvetica", 17)).pack(pady=10)

    if scene == "intro":
        tk.Label(main_window, text="Vous êtes un érudit convoqué par le roi.", fg="white", bg="black", font=("Helvetica", 20)).pack(pady=20)
        add_button("Accepter la mission", lancer_quizz)

    elif scene == "noble":
        tk.Label(main_window, text="Vous êtes promu noble. Déchiffrez un message.", fg="white", bg="black", font=("Helvetica", 20)).pack(pady=20)
        add_button("Décoder", mots_inverses)

    elif scene == "prison":
        tk.Label(main_window, text="Vous êtes emprisonné. Des mots apparaissent à l'envers.", fg="white", bg="black", font=("Helvetica", 20)).pack(pady=20)
        add_button("Essayer d'inverser", mots_inverses)

    elif scene == "echec_prison":
        tk.Label(main_window, text="Vous sombrez dans la folie... vous jouez au blackjack seul !", fg="white", bg="black", font=("Helvetica", 20)).pack(pady=20)
        add_button("Jouer au blackjack", BJtkinter)

    elif scene == "reussite_prison":
        tk.Label(main_window, text="Un portail s'ouvre. Trouvez qui vous à emprisonnés...", fg="white", bg="black", font=("Helvetica", 20)).pack(pady=20)
        add_button("Deviner", JeuTraitre)

# ---------------------------
# Lancement du jeu
# ---------------------------
main_window = tk.Tk()
main_window.title("L'érudit et les mystères du royaume")
main_window.geometry("1200x800")
main_window.configure(bg="black")
show_scene("intro")
main_window.mainloop()
