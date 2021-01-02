from abrviz import Arbre, Noeud

import random
liste = list(range(20))
random.shuffle(liste)
c = Arbre()
c.fonction_ordre = lambda x, y: str(x.valeur) < str(y.valeur)
for e in liste:
    c.inserer(Noeud(e))

Arbre.sortie(c.racine, "exemple3_0", "png")

Arbre.options('node', {"style": "filled"})
Arbre.options('edge', {"arrowhead": "vee", "arrowsize": ".5"})
Arbre.sortie(c.racine, "exemple3_1", "png")

Arbre.options('graph', {"splines": "false"})
Arbre.sortie(c.racine, "exemple3_2", "png")
