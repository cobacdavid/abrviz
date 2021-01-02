from abrviz import Arbre, Noeud

d = {"abricot": 2, "poire": 5, "pomme": 1, "ananas": 7, "kiwi": 0}

c = Arbre()
for k in d:
    c.inserer(Noeud(d[k], k))
Arbre.etiquette = "contenu"
Arbre.sortie(c.racine, "exemple4_0", "png")

c = Arbre()
for k in d:
    noeud = Noeud(d[k])
    noeud.contenu = f"{k} ({d[k]})"
    c.inserer(noeud)

Arbre.etiquette = "contenu"
Arbre.sortie(c.racine, "exemple4_1", "png")
