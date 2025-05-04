import tkinter as tk
from tkinter import messagebox


# ----------------------------
# Données du quiz
# ----------------------------
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

current_question = 0
score = 0
def Quizz() :
    # ----------------------------
    # Variables de contrôle
    # ----------------------------
    current_question = 0  # Position actuelle dans la liste de questions
    score = 0             # Score de l'utilisateur

    # ----------------------------
    # Création de la fenêtre principale
    # ----------------------------
    window = tk.Tk()
    window.title("Quiz Python")
    window.geometry("600x400")

    # Variable liée aux boutons radio pour savoir quelle réponse a été choisie
    selected_option = tk.StringVar()

    # ----------------------------
    # Fonction pour afficher une question
    # ----------------------------
    def show_question():
        selected_option.set(None)  # Réinitialise la sélection
        q = questions[current_question]  # Récupère la question actuelle
        question_label.config(text=q["question"])  # Affiche le texte de la question

        # Supprime les anciens boutons de réponse
        for widget in options_frame.winfo_children():
            widget.destroy()

        # Crée un bouton radio pour chaque option de réponse
        for code in q["options"]:
            text = f"{code}) {q['text_options'][code]}"
            rb = tk.Radiobutton(
                options_frame,
                text=text,
                variable=selected_option,
                value=code,
                font=("Arial", 11)
            )
            rb.pack(anchor="w", pady=2)

    # ----------------------------
    # Fonction appelée lors du clic sur "Suivant"
    # ----------------------------
    def next_question():
        global current_question, score
        selected = selected_option.get()  # Récupère la réponse sélectionnée

        # Si aucune réponse n'est sélectionnée
        if not selected:
            messagebox.showwarning("Attention", "Veuillez choisir une réponse.")
            return

        # Vérifie la réponse
        correct = questions[current_question]["answer"]
        if selected == correct:
            score += 1
            messagebox.showinfo("Résultat", "Bonne réponse !")
        else:
            bonne = questions[current_question]["text_options"][correct]
            messagebox.showinfo("Résultat", f"Mauvaise réponse.\nLa bonne réponse était : {correct}) {bonne}")

        # Passe à la question suivante ou termine le quiz
        current_question += 1
        if current_question < len(questions):
            show_question()
        else:
            messagebox.showinfo("Fin du quiz", f"Vous avez terminé le quiz !\nScore : {score}/{len(questions)}")
            window.quit()  # Ferme la fenêtre


    # ----------------------------
    # Widgets de l'interface
    # ----------------------------

    # Label pour la question
    question_label = tk.Label(
        window,
        text="",
        wraplength=550,
        font=("Arial", 13),
        justify="left"
    )
    question_label.pack(pady=20)

    # Frame contenant les boutons radio
    options_frame = tk.Frame(window)
    options_frame.pack(pady=10)

    # Bouton "Suivant"
    next_btn = tk.Button(
        window,
        text="Suivant",
        command=next_question,
        font=("Arial", 12)
    )
    next_btn.pack(pady=20)

    # ----------------------------
    # Démarrage du quiz
    # ----------------------------
    show_question()
    window.mainloop()
    #----------------------------
    #score
    #----------------------------
    return score

