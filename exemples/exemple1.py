from abrviz import Arbre, Noeud


a = Arbre()
liste = [Noeud(i) for i in [3, 2, 1, 5, 4, 6]]
for i in liste:
    a.inserer(i)


Arbre.sortie(a.racine, "exemple1_0", "png")
Arbre.sortie(liste[1], "exemple1_1", "png")
a.supprimer(liste[0])
Arbre.sortie(a.racine, "exemple1_2", "png")
