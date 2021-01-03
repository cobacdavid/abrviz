from abrviz import Arbre, Noeud


liste = [2, 3, 6, 0, 4, 5, 1]
liste_noeuds = [Noeud(i) for i in liste]

a = Arbre()
for e in liste_noeuds:
    a.inserer(e)

# On peut effectuer des mouvements de rotation à droite ou à gauche
# L'arbre reste un ABR
a.sortie(a.racine, "exemple5_0", "png")

# le noeud "racine" du changement est passé en argument
a.rotation_gauche(a.rechercher(2))
a.sortie(a.racine, "exemple5_1", "png")

# on peut alors équilibrer l'arbre
a.rotation_gauche(a.rechercher(0))
a.rotation_droite(a.rechercher(2))
a.rotation_gauche(a.rechercher(4))
a.rotation_droite(a.rechercher(6))
a.sortie(a.racine, "exemple5_2", "png")
