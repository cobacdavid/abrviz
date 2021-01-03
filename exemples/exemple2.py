from abrviz import Arbre, Noeud
import random


liste = list(range(15))
random.shuffle(liste)

a = Arbre()
for e in liste:
    a.inserer(Noeud(e))

# Visualisation de l'arbre
mon_noeud = a.racine
a.sortie(mon_noeud, "exemple2_0", "png")

# on peut demander une version "complète" avec les noeuds
# invisibles d'un arbre binaire complet : l'apparence est très
# large
a.sortie(mon_noeud, "exemple2_1", "png", style="complet")

# s'il y a un sous-arbre gauche, on le visualise
if mon_noeud.gauche is not None:
    a.sortie(mon_noeud.gauche, "exemple2_2", "png")
