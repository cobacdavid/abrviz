__author__ = "david cobac"
__date__ = 20201215

import graphviz
import math
import inspect


class Arbre:
    def __init__(self):
        self._liste = []
        self._liste_insertion = []
        self._fonction_ordre = lambda a, b: a < b
        self._graphe = graphviz.Digraph(engine="dot")
        self._recherche_chemin = False
        self._infixe = []
        self._prefixe = []
        self._suffixe = []

    @property
    def taille(self):
        return sum([1 for n in self._liste if n is not None])

    @property
    def hauteur(self):
        return 1 + int(math.log2(len(self._liste)))

    @property
    def fonction_ordre(self):
        return inspect.getsource(self._fonction_ordre)

    @fonction_ordre.setter
    def fonction_ordre(self, fonction):
        l_insert = self._liste_insertion
        self.__init__()
        self._fonction_ordre = fonction
        for element in l_insert:
            self.inserer(element)

    @property
    def liste_insertion(self):
        return self._liste_insertion

    @liste_insertion.setter
    def liste_insertion(self, liste):
        for element in liste:
            self.inserer(element)

    def _est_plus_petit(self, element1, element2):
        return self._fonction_ordre(element1, element2)

    def inserer(self, valeur):
        self._liste_insertion.append(valeur)
        #
        indice = 1
        trouve = False if self._liste else True
        #
        while not trouve:
            if self._est_plus_petit(self._liste[indice - 1], valeur):
                indice = 2 * indice + 1
            else:
                indice = indice * 2
            trouve = indice > len(self._liste) or \
                self._liste[indice - 1] is None
        #
        if len(self._liste) < indice:
            self._liste += [None] * (indice - len(self._liste))
        self._liste[indice - 1] = valeur

    def sortie(self, nom_fichier, format):
        self._graphe.attr("node", shape="record")
        self._graphe.attr("edge", headport="n")
        self._graphe.attr("edge", tailclip="false")
        #
        self._visunoeud(self._graphe, 1)
        self._graphe.render(nom_fichier, format=format)

    def chemin_vers(self, nombre):
        self._recherche_chemin = True
        indice = 1
        chemin = []
        trouve = self._liste[indice - 1] == nombre
        #
        # tant que :
        # - on n'a pas trouvé
        # - on reste dans la limite de la liste
        # - le noeud maintenant considéré n'est pas None
        while not trouve and indice - 1 < len(self._liste) and \
              self._liste[indice - 1] is not None:
            # on ajoute le noeud dans les parcourus
            chemin.append(self._liste[indice - 1])
            # on teste si son doit aller à gauche ou à droite
            if self._est_plus_petit(nombre, self._liste[indice - 1]):
                indice = 2 * indice
            else:
                indice = 2 * indice + 1
            # a-t-on trouvé ?
            trouve = indice - 1 > len(self._liste) or \
                self._liste[indice - 1] == nombre
        #
        # si on est dans un cas de dépassement ou d'arrivée sur
        # None : le nombre demandé n'est pas dans l'arbre
        if indice > len(self._liste) or not self._liste[indice - 1]:
            return
        else:
            chemin.append(self._liste[indice - 1])
            return chemin

    def _parcours(self, type_parcours):
        return self._parcours_rec(type_parcours, 1, [])

    def _parcours_rec(self, type_parcours, indice=1, resultat=[]):
        if indice - 1 < len(self._liste):
            if type_parcours == "pre" and self._liste[indice - 1] is not None:
                resultat.append(self._liste[indice - 1])
            self._parcours_rec(type_parcours, 2 * indice, resultat)
            if type_parcours == "in" and self._liste[indice - 1] is not None:
                resultat.append(self._liste[indice - 1])
            self._parcours_rec(type_parcours, 2 * indice + 1, resultat)
            if type_parcours == "suf" and self._liste[indice - 1] is not None:
                resultat.append(self._liste[indice - 1])
        return resultat

    @property
    def prefixe(self):
        return self._parcours("pre")

    @property
    def infixe(self):
        return self._parcours("in")

    @property
    def suffixe(self):
        return self._parcours("suf")

    def _visunoeud(self, graphe, indice):
        contenu = self._liste[indice - 1]
        if contenu is None: return

        N = len(self._liste)

        indice_gauche = 2 * indice
        indice_droit = indice_gauche + 1
        contenug = self._liste[indice_gauche - 1] \
            if indice_gauche <= N else None
        contenud = self._liste[indice_droit - 1] \
            if indice_droit <= N else None

        with graphe.subgraph(name=str(contenu) + "sub") as gsub:
            gsub.node(str(contenu), label="{" + str(contenu) + "|{<g>|<d>}}")
            if contenug is None:
                gsub.node(str(contenu) + "invisg", style="invis")
                gsub.edge(str(contenu) + ":g:c", str(contenu) + "invisg",
                            style="invis", weight="10")
            else:
                gsub.edge(str(contenu) + ":g:c", str(contenug))

            if contenud is None:
                gsub.node(str(contenu) + "invisd", style="invis")
                gsub.edge(str(contenu) + ":d:c", str(contenu) + "invisd",
                            style="invis", weight="10")
            else:
                gsub.edge(str(contenu) + ":d:c", str(contenud))

            if indice_gauche - 1 < N:
                self._visunoeud(gsub, indice_gauche)
            if indice_droit - 1 < N:
                self._visunoeud(gsub, indice_droit)
