from abrviz import Arbre, Noeud

dico_contenu = {"abricot": 2, "poire": 5, "pomme": 1, "ananas": 7, "kiwi": 0}

a = Arbre()
for k in dico_contenu:
    a.inserer(Noeud(dico_contenu[k], k))
Arbre.etiquette = "contenu"
Arbre.sortie(a.racine, "exemple4_0", "png")

a = Arbre()
for k in dico_contenu:
    noeud = Noeud(dico_contenu[k])
    noeud.contenu = f"{k} ({dico_contenu[k]})"
    a.inserer(noeud)

Arbre.etiquette = "contenu"
Arbre.sortie(a.racine, "exemple4_1", "png")
