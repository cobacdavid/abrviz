from abrviz import Arbre, Noeud


a = Arbre()
liste = [Noeud(i) for i in [3, 2, 1, 5, 4, 6]]
for i in liste:
    a.inserer(i)

# on visualise l'arbre
a.sortie(a.racine, "exemple1_0", "png")
# on demande une visualisation en arbre binaire complet : un peu
# plus d'espace dans la dernière ligne
a.sortie(a.racine, "exemple1_1", "png", style="complet")
# on demande une visualisation à partir du 2ème noeud rentré
a.sortie(liste[1], "exemple1_2", "png")
# on supprime la racine puis on visualise le nouvel arbre en pdf
a.supprimer(liste[0])
a.sortie(a.racine, "exemple1_3", "pdf")
