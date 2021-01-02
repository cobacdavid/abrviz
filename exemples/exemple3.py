from abrviz import Arbre, Noeud
import random


liste = list(range(20))
random.shuffle(liste)

a = Arbre()
a.fonction_ordre = lambda x, y: str(x.valeur) < str(y.valeur)

for e in liste:
    a.inserer(Noeud(e))

Arbre.sortie(a.racine, "exemple3_0", "png")

Arbre.options('node', {"style": "filled"})
Arbre.options('edge', {"arrowhead": "vee", "arrowsize": ".5"})
Arbre.sortie(a.racine, "exemple3_1", "png")

Arbre.options('graph', {"splines": "false"})
Arbre.sortie(a.racine, "exemple3_2", "png")
