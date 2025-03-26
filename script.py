import random
# import de la fonction permettant l'aléatoire

#on defini la liste des cartes
famille_carte = ['Coeurs', 'Piques', 'Carreaux', 'Trèfles']
liste_carte = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Reine', 'Roi']
deck=[(famille,carte)for famille in famille_carte for carte in liste_carte]


def valeur_cartes(carte):
    if carte[1] in ['Valet', 'Reine', 'Roi']:
        return 10
    elif carte[1] == 'As':
        return 11
    else :
        return int(carte[1])

#mélange de carte
print('le croupier tire 2 cartes pour vous 2 pour lui')
random.shuffle(deck)
carte_j=[deck.pop(),deck.pop()]
carte_d=[deck.pop(),deck.pop()]


while True:
    score_j=sum(valeur_cartes(carte)for carte in carte_j)
    # calcul de la valeur de la main du joueur
    score_d=sum(valeur_cartes(carte)for carte in carte_d)
    # calcul de la valeur de la main du croupier
    print("Main du joueur :" , carte_j)
    print(" ")
    print("Score du joueur :" , score_j)
    print(" ")
#nous propose de repiocher
    c=input("nouvelle carte (oui) ou stop (non) :")
    if c == 'oui':
        nc=deck.pop()
        carte_j.append(nc)
    else :
        break
#Fait repiocher le croupier si la valeur de sa main < 15
while score_d < 15:
    ncd = deck.pop()
    carte_d.append(ncd)
    score_d += valeur_cartes(ncd)
#Verification des conditions de victoires
print("Cards Dealer Has:", carte_d)
print("Score Of The Dealer:", score_d)
print("")
if score_j > 21:
    print("Carte du croupier:", carte_d)
    print("Score du croupier:", score_d)
    print("Carte du joueur :", carte_j)
    print("Score du joueur:", score_j)
    print("Victoire du croupier:)")

elif score_d > 21:
    print("Carte du croupier:", carte_d)
    print("")
    print("Score du croupier:", score_d)
    print("")
    print("Carte du joueur :", carte_j)
    print("")
    print("Score du joueur:", score_j)
    print("")
    print("Player wins (Dealer Loss Because Dealer Score is exceeding 21)")

elif score_j > score_d:
    print("Carte du croupier:", carte_d)
    print("")
    print("Score du croupier:", score_d)
    print("")
    print("Carte du joueur :", carte_j)
    print("")
    print("Score du joueur:", score_j)
    print("")
    print("Player wins (Player Has High Score than Dealer)")

elif score_d > score_j:
    print("Carte du croupier:", carte_d)
    print("")
    print("Score du croupier:", score_d)
    print("")
    print("Carte du joueur :", carte_j)
    print("")
    print("Score du joueur:", score_j)
    print("")
    print("Dealer wins (Dealer Has High Score than Player)")

else:
    print("Carte du croupier:", carte_d)
    print("")
    print("Score du croupier:", score_d)
    print("")
    print("Carte du joueur :", carte_j)
    print("")
    print("Score du joueur:", score_j)
    print("")
    print("égalité.")