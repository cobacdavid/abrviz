from abrviz import Arbre, Noeud

# EXEMPLE 3
import random
liste = list(range(20))
random.shuffle(liste)
c = Arbre()
c.fonction_ordre = lambda x, y: str(x.valeur) < str(y.valeur)
for e in liste:
    c.inserer(Noeud(e))

Arbre.sortie(c.racine, "exemple3_0", "png")
