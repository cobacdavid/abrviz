from abrviz import Arbre, Noeud


valeurs = [3, 4, 7, 9, 5, 8, 1, 0, 6, 2]
noeuds = [Noeud(i) for i in valeurs]

a = Arbre()
for n in noeuds:
    a.inserer(n)

print("Affichage imbriquée :")
print(a)
print()
print("Hauteur :", a.hauteur())
print("Taille :", len(a))
print()
print("Parcours en largeur :", a.largeur)
print("Parcours prefixe :", a.prefixe)
print("Parcours infixe :", a.infixe)
print("Parcours suffixe :", a.suffixe)
print("Liste aplatie en largeur :", a.liste_aplatie())
print()
a.supprimer(noeuds[0])
print("Nouveau parcours en largeur après suppression du noeud racine :")
print(a.largeur)
