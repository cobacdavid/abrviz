from abrviz import Arbre, Noeud

# dictionnaire, les valeurs seront les clés de l'arbre
dico_contenu = {"abricot": 2, "poire": 5, "pomme": 1, "ananas": 7, "kiwi": 0}

a = Arbre()
for k in dico_contenu:
    a.inserer(Noeud(dico_contenu[k], k))

# les noeuds montreront le contenu du noeud et non la clé ("valeur")
Arbre.etiquette = "contenu"
a.sortie(a.racine, "exemple4_0", "png")

# pour visualiser un mix des deux (clés et valeurs du dictionnaire)
# on redéfinit l'arbre et les noeuds :
a = Arbre()
for k in dico_contenu:
    noeud = Noeud(dico_contenu[k])
    # le contenu du noeud reprend les données complètes du dictionnaire
    noeud.contenu = f"{k} ({dico_contenu[k]})"
    a.inserer(noeud)

Arbre.etiquette = "contenu"
a.sortie(a.racine, "exemple4_1", "png")
