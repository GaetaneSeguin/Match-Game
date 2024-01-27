# Fonction qui soustrait à total le nombre d'allumettes sélectionné
def enlever(nombre):
    global total
    total -= nombre
    return total

# Fonction pour sélectionner le nombre de joueur.euse
def selectPlayer():
    nbrJoueur = int(input("Sélectionner le nombre de joueurs.euses entre 2 et 6 "))
    while nbrJoueur < 2 or nbrJoueur > 6:
        nbrJoueur = int(input("Sélectionner le nombre de joueurs.euses entre 2 et 6 "))
    return nbrJoueur

# nomDuJoueur = ""

total = 50
nbrPlayer = selectPlayer()
numPlayer = 0

while total != 0:
    # Gestion du jeu en multi-joueur.euse
    numPlayer += 1
    if numPlayer > nbrPlayer:
        numPlayer = 1
        
    nomDuJoueur = "Joueur " + str(numPlayer)

    number = int(input( nomDuJoueur + " : combien d'allumettes souhaitez vous retirer ?"))
    while number < 1 or number > 6 or type(number) is str :
        number = int(input( nomDuJoueur + " : combien d'allumettes souhaitez vous retirer ? (entre 1 et 6)"))
    while total < number:
        number = int(input( nomDuJoueur + " : combien d'allumettes souhaitez vous retirer ? Il reste " + str(total) + " allumettes"))
    
    resultat = enlever(number)
    print(resultat)

# Gestion du jeu quand il n'y a que deux joueurs.euses
    # if not aQuiDeJouer:
    #     nomDuJoueur="Joueur 2"
    #     aQuiDeJouer=True
    # elif aQuiDeJouer:
    #     nomDuJoueur="Joueur 1"
    #     aQuiDeJouer=False
    
if total <= 0:
    print('Bravo '+ nomDuJoueur + ', vous avez gagné !')