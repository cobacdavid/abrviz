from abrviz import Arbre, Noeud
import random


liste = list(range(15))
random.shuffle(liste)

a = Arbre()
for e in liste:
    a.inserer(Noeud(e))

mon_noeud = a.racine
Arbre.sortie(mon_noeud, "exemple2_0", "png")
Arbre.sortie(mon_noeud.droit, "exemple2_1", "png")

if mon_noeud.gauche is not None:
    mon_noeud = mon_noeud.gauche
    Arbre.sortie(mon_noeud, "exemple2_2", "png")
