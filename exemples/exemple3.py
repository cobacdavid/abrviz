from abrviz import Arbre, Noeud
import random


liste = list(range(20))
random.shuffle(liste)

a = Arbre()
# on change la fonction de la relation d'ordre
a.fonction_ordre = lambda x, y: str(x.valeur) < str(y.valeur)

for e in liste:
    a.inserer(Noeud(e))

a.sortie(a.racine, "exemple3_0", "png")

# on change le style
Arbre.options('node', {"style": "filled"})
Arbre.options('edge', {"arrowhead": "diamond", "arrowsize": "1"})
a.sortie(a.racine, "exemple3_1", "png")

# les flèches se courbent
Arbre.options('graph', {"splines": "true"})
a.sortie(a.racine, "exemple3_2", "png")
