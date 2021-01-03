from abrviz import Arbre, Noeud


valeurs = [3, 4, 7, 9, 5, 8, 1, 0, 6, 2]
noeuds = [Noeud(i) for i in valeurs]

a = Arbre()
for n in noeuds:
    a.inserer(n)

texte = f"""Affichage imbriquée :
{a}

Hauteur : {a.hauteur()}
Taille : {len(a)}

Les parcours fournissent des listes d'objets :
Parcours en largeur : {a.largeur}

Pour obtenir les clés, on demande les valeurs :
Parcours en largeur : {[n.valeur for n in a.largeur]}

Parcours prefixe : {[n.valeur for n in a.prefixe]}
Parcours infixe : {[n.valeur for n in a.infixe]}
Parcours suffixe : {[n.valeur for n in a.suffixe]}

Une liste 'complète' en largeur peut être obtenue :
{[n if not n else n.valeur for n in a.liste_aplatie()]}

Recherche du noeud de clé 5 :
le noeud : {a.rechercher(5).__repr__()}
son arborescence : {a.rechercher(5)}
sa valeur : {a.rechercher(5).valeur}
son contenu (éventuellement transporté dans sa structure) : \
{a.rechercher(5).contenu}
le chemin qui y mène : {[n.valeur for n in a.chemin_vers(a.rechercher(5))]}

Si on connaît une référence vers le noeud, on peut l'utiliser.
le noeud de clé 5 est le 4ème de la liste noeuds : \
{noeuds[4]}
"""
print(texte)

a.supprimer(noeuds[0])
texte = f"""Nouveau parcours en largeur après suppression de la racine :
{[n.valeur for n in a.largeur]}
"""
print(texte)
