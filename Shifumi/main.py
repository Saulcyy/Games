import random

print("Développé par Mona#6669")

shifumi = ['p','c','f']
nb_manche_voulu = int(input("Entrez le nombre de manche que vous souhaitez ?"))
score_j = 0
score_ord = 0
nb_manche = 0

while nb_manche < nb_manche_voulu:
    choix_joueur = input("Entrez votre choix Pierre(p), Ciseaux(c) et Feuille(f) ?")
    choix_ordi = random.choice(shifumi)
    if (choix_joueur == 'p' and choix_ordi == 'c') or (choix_joueur == 'c' and choix_ordi == 'f') or (choix_joueur == 'f' and choix_ordi == 'p'):
        print("Joueur gagne !")
        score_j+=1
    elif (choix_joueur == 'p' and choix_ordi == 'p') or (choix_joueur == 'c' and choix_ordi == 'c') or (choix_joueur == 'f' and choix_ordi == 'f'):
        print("Egalité !")
    elif (choix_joueur == 'c' and choix_ordi == 'p') or (choix_joueur == 'f' and choix_ordi == 'c') or (choix_joueur == 'p' and choix_ordi == 'f'):
        print("Ordi gagne !")
        score_ord+=1
    nb_manche+=1

if score_j>score_ord:
    print("Joueur gagne le match ! Joueur :" +str(score_j)+" vs Ordi :" +str(score_ord))
elif score_ord == score_j:
    print("Egalité dans ce match ! Joueur :" +str(score_j)+" vs Ordi :" +str(score_ord))
else:
    print("Ordi gagne le match ! Joueur :" +str(score_j)+" vs Ordi :" +str(score_ord))