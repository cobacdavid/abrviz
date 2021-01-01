from abrviz import Arbre, Noeud
import random


liste = list(range(10))
random.shuffle(liste)
b = Arbre()
for e in liste:
    b.inserer(Noeud(e))

Arbre.sortie(b.racine, "exemple2_0", "png")
Arbre.sortie(b.racine.droit, "exemple2_1", "png")
