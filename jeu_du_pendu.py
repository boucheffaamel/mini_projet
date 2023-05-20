import random
nombre_de_chance=6
lettres_trouvees=[]
lettres_manquees=[]
with open ('mots_pendu.txt','r') as file:
    contenu=file.read()
    mots=contenu.split()
    mot_aléatoire=random.choice(mots)
#print(mot_aléatoire)
#affichage de l'etat actuel des mots
def afficher_mot():
    for lettre in mot_aléatoire:
        if lettre in lettres_trouvees:
            print(lettre, end="")
        else:
            print("_", end=" ")
    print("\n")
while nombre_de_chance >0:
    afficher_mot()

    #affichage de la lettre manquees
    if len(lettres_manquees)>0:
        print('lettre manquées:','')

    #entrer une lettre
    lettre=input('entrer une lettre:')

    #vérifier si la lettre est dans le mot
    if lettre in mot_aléatoire:
        print('la lettre:',lettre,'est dans le mot')
        lettres_trouvees.append(lettre)
#    else:
#        print('incorrect')
        if set(lettres_trouvees)==set(mot_aléatoire):
            print('vous aver gagné','le mot est:',mot_aléatoire)
    else:
        print('incorrect',nombre_de_chance,'chances')
        nombre_de_chance=nombre_de_chance-1
if nombre_de_chance==0:
    print('vous n\'aver plus de chances','vous aver perdu')
