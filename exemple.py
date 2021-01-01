from abrviz import Arbre, Noeud

# EXEMPLE 1
a = Arbre()
liste = [Noeud(i) for i in [3, 2, 1, 5, 4, 6]]
liste_noeuds = []
for i in liste:
    liste_noeuds.append(a.inserer(i))


print(a)
Arbre.sortie(a.racine, "exemple1_0", "png")
print(a.prefixe, a.infixe, a.suffixe)
print(a.hauteur())

Arbre.sortie(liste_noeuds[1], "exemple1_1", "png")

a.supprimer(liste_noeuds[0])
Arbre.sortie(a.racine, "exemple1_2", "png")


# EXEMPLE 2
import random
liste = list(range(20))
random.shuffle(liste)
b = Arbre()
for e in liste:
    b.inserer(Noeud(e))

Arbre.sortie(b.racine, "exemple2_0", "png")
Arbre.sortie(b.racine.droit, "exemple2_1", "png")
