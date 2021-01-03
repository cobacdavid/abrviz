__author__ = "david cobac"
__date__ = 20201215


import graphviz
import inspect
import math


class File:
    def __init__(self):
        self._liste = []
        self._est_vide = True

    @property
    def est_vide(self):
        self._est_vide = len(self._liste) == 0
        return self._est_vide

    def enfiler(self, element):
        self._liste.append(element)

    def defiler(self):
        if not self._est_vide:
            element = self._liste.pop(0)
            return element


class Noeud:
    def __init__(self, valeur, contenu=None):
        self.valeur = valeur
        self._contenu = contenu
        self.gauche = None
        self.droit = None
        self.parent = None

    def __str__(self):
        return f"({self.gauche} -- {self.valeur} -- {self.droit})"

    @property
    def contenu(self):
        return self._contenu

    @contenu.setter
    def contenu(self, contenu):
        self._contenu = contenu


class Arbre:
    # @classmethod
    # def sortie(cls, noeud, nom_fichier, format):

    #     cls._graphe = graphviz.Digraph()
    #     for k in Arbre._options_graphe:
    #         cls._graphe.attr(k, **Arbre._options_graphe[k])
    #     #
    #     cls._visunoeud(noeud)
    #     cls._graphe.render(nom_fichier, format=format)

    # @classmethod

    @classmethod
    def options(cls, classe, dictionnaire):
        cls._options_graphe[classe].update(dictionnaire)

    etiquette = "valeur"
    _graphe = graphviz.Digraph()
    _options_graphe = {"node": {"shape": "record"},
                       "edge": {"headport": "n",
                                "tailclip": "false",
                                "arrowsize": ".5",
                                "arrowhead": "vee"},
                       "graph": {"engine": "dot",
                                 "splines": "false"}}

    def __init__(self, racine=None):
        self.racine = racine
        self._fonction_ordre = lambda x, y: x.valeur < y.valeur

    def __str__(self):
        return str(self.racine)

    def __len__(self):
        return len(self.infixe)

    def est_vide(self):
        return self.racine is None

    @property
    def fonction_ordre(self):
        return inspect.getsource(self._fonction_ordre)

    @fonction_ordre.setter
    def fonction_ordre(self, fonction):
        self._fonction_ordre = fonction

    @property
    def prefixe(self):
        return self._parcours_prof("prefixe")

    @property
    def infixe(self):
        return self._parcours_prof("infixe")

    @property
    def suffixe(self):
        return self._parcours_prof("suffixe")

    @property
    def largeur(self):
        return self._parcours_largeur()

    def liste_aplatie(self, noeud=None):
        return self._parcours_largeur_numerote(noeud)

    def inserer(self, noeud, noeud_courant=None):
        if self.racine is None:
            self.racine = noeud
            return noeud

        # racine de l'arbre
        if noeud_courant is None:
            noeud_courant = self.racine

        if self._fonction_ordre(noeud, noeud_courant):
            if noeud_courant.gauche is None:
                noeud_courant.gauche = noeud
                noeud.parent = noeud_courant
                return noeud
            else:
                return self.inserer(noeud, noeud_courant.gauche)
        else:
            if noeud_courant.droit is None:
                noeud_courant.droit = noeud
                noeud.parent = noeud_courant
                return noeud
            else:
                return self.inserer(noeud, noeud_courant.droit)

    def maximum(self, noeud):
        # renvoie le maximum et le noeud
        courant = noeud
        while courant.droit is not None:
            courant = courant.droit
        return courant, courant.valeur

    def supprimer(self, noeud, noeud_courant=None, orientation=None):
        """Se placer au niveau du parent pour pouvoir pointer vers None, en
        effet supprimer un objet par lui-même semble impossible en
        Python !

        Donc on sait que l'élément cherché n'est pas celui actuel
        mais peut-être un des deux descendants.

        Néanmoins en ajoutant un attribut parent à chaque noeud, il
        est aisé de remonter au parent.

        orientation permet de savoir si on est à gauche ou à droite
        du parent pour supprimer le bon lien

        """

        if noeud_courant is None:
            noeud_courant = self.racine
        #
        if noeud.valeur == noeud_courant.valeur:
            # pas de descendant
            if noeud_courant.gauche is None and noeud_courant.droit is None:
                # on supprime le lien qui le lie à son parent
                # le garbage collector prend la suite
                if orientation == 'g':
                    # print(noeud_courant.parent.valeur)
                    noeud_courant.parent.gauche = None
                else:
                    noeud_courant.parent.droit = None
            # un seul à droite
            elif noeud_courant.gauche is None:
                if orientation == 'g':
                    noeud_courant.parent.gauche = noeud_courant.droit
                else:
                    noeud_courant.parent.droit = noeud_courant.droit
                noeud_courant.droit.parent = noeud_courant.parent
            # un seul à gauche
            elif noeud_courant.droit is None:
                if orientation == 'g':
                    noeud_courant.parent.gauche = noeud_courant.gauche
                else:
                    noeud_courant.parent.droit = noeud_courant.gauche
                noeud_courant.gauche.parent = noeud_courant.parent
            # deux ! on choisit le plus grand (le plus à
            # droite) du sous-arbre gauche qu'on devra donc
            # supprimer
            else:
                n, M = self.maximum(noeud_courant.gauche)
                # destruction du lien de droite du parent (le noeud
                # max vient de la droite !)
                # n.parent.droit = None
                self.supprimer(n, noeud_courant.gauche, "g")
                noeud_courant.valeur = M
                #
        elif noeud.valeur < noeud_courant.valeur:
            self.supprimer(noeud, noeud_courant.gauche, 'g')
        else:
            self.supprimer(noeud, noeud_courant.droit, 'd')

    def rechercher(self, element_a_chercher, type_element="valeur"):
        # Besoin d'un noeud pour la fonction de comparaison
        if type_element == "valeur":
            noeud_factice = Noeud(element_a_chercher)
        elif type_element == "contenu":
            noeud_factice = Noeud(-1, contenu=element_a_chercher)
        #
        courant = self.racine
        #
        # recherche simple
        if type_element == "valeur":
            while courant.valeur != element_a_chercher:
                if self._fonction_ordre(noeud_factice, courant):
                    courant = courant.gauche
                else:
                    courant = courant.droit
        elif type_element == "contenu":
            # parcours préfixe
            liste = self.prefixe
            courant = liste.pop(0)
            while courant.contenu != element_a_chercher:
                courant = liste.pop(0)
        return courant

    def chemin_vers(self, noeud):
        courant = self.racine
        liste_noeuds = [courant]

        while courant != noeud:
            if self._fonction_ordre(noeud, courant):
                courant = courant.gauche
            else:
                courant = courant.droit
            liste_noeuds.append(courant)

        return liste_noeuds

    def sortie(self, noeud, nom_fichier, format, style="compact"):
        graphe = graphviz.Digraph()
        for k in Arbre._options_graphe:
            graphe.attr(k, **Arbre._options_graphe[k])
        #
        if style == "compact":
            self._visunoeud(noeud, graphe)
        elif style == "complet":
            self._visunoeud2(noeud, graphe)
        graphe.render(nom_fichier, format=format)

    def _visunoeud(self, noeud, graphe):
        identifiant = noeud.valeur
        contenu = eval(f"noeud.{Arbre.etiquette}")
        if noeud.gauche is not None:
            identifiantg = noeud.gauche.valeur
        else:
            identifiantg = None
        if noeud.droit is not None:
            identifiantd = noeud.droit.valeur
        else:
            identifiantd = None

        with graphe.subgraph(name=f"sub_{identifiant}") as gsub:
            gsub.node(str(identifiant),
                      label="{" + str(contenu) + "|{<g>|<d>}}")
            if identifiantg is None:
                gsub.node(str(identifiant) + "invisg",
                          label="",
                          width=".1",
                          style="invis")
                gsub.edge(str(identifiant) + ":g:c", str(identifiant)
                          + "invisg", style="invis")
            else:
                gsub.edge(str(identifiant) + ":g:c", str(identifiantg))

            if identifiantd is None:
                gsub.node(str(identifiant) + "invisd",
                          label="",
                          width=".1",
                          style="invis")
                gsub.edge(str(identifiant) + ":d:c", str(identifiant)
                          + "invisd", style="invis")
            else:
                gsub.edge(str(identifiant) + ":d:c", str(identifiantd))

            if noeud.gauche is not None:
                self._visunoeud(noeud.gauche, gsub)
            if noeud.droit is not None:
                self._visunoeud(noeud.droit, gsub)

    def _visunoeud2(self, noeud, graphe):
        compteur = 1
        liste = self.liste_aplatie(noeud)
        liste += [None] * (2 ** (int(math.log2(len(liste))) + 1)
                           - 1 - len(liste))

        for i in range(self.hauteur(noeud)):
            # sub (ou autre) plutôt que cluster qui contraint à
            # l'intérieur du rectangle
            with graphe.subgraph(name=f"sub_{i}") as gsub:
                gsub.attr(rankdir="LR")
                # hack pourri parce que sinon les boeuds ne sont
                # pas dans le bon ordre sur une même ligne
                for indice in range(2 ** (i + 1) - 2, 2 ** i - 2, -1):
                    noeud = liste[indice]
                    compteur_du_parent = int((indice - 1) // 2)
                    identifiant = str(indice)
                    contenu = " " if not noeud \
                        else eval(f"noeud.{Arbre.etiquette}")
                    style = "invis" if not noeud else "solid"
                    # contenu, style))
                    gsub.node(identifiant,
                              label="{" + str(contenu) + "|{<g>|<d>}}",
                              style=style)
                    #
                    provenance = ":g:c" if compteur % 2 else ":d:c"
                    identifiant_parent = str(compteur_du_parent)
                    if compteur != 1:
                        graphe.edge(identifiant_parent + provenance,
                                    identifiant,
                                    style=style)  # , weight=str(2**i))
                    compteur += 1
        #
        # ci-dessous première version
        # mais les noeuds sont dans l'ordre contraire !!!
        #
        # for i in range(self.hauteur()):
        #     with graphe.subgraph(name=f"sub_{i}") as gsub:
        #         gsub.attr(rankdir="RL")
        #         while compteur <= 2 ** (i + 1) - 1:
        #             noeud = liste[compteur - 1]
        #             compteur_du_parent = int(compteur // 2)
        #             if noeud is not None:
        #                 # valeur = noeud.valeur
        #                 contenu = eval(f"noeud.{Arbre.etiquette}")
        #                 gsub.node(str(compteur),
        #                           label="{" + str(contenu) + "|{<g>|<d>}}")
        #                 if compteur % 2 == 0:
        #                     gsub.edge(str(compteur_du_parent) + ":d:c",
        #                               str(compteur))  # , weight=str(2**i-1))
        #                 elif compteur != 1:
        #                     gsub.edge(str(compteur_du_parent) + ":g:c",
        #                               str(compteur))  # , weight=str(2**i-1))
        #             else:
        #                 gsub.node(str(compteur),
        #                           label="{ |{<g>|<d>}}",
        #                           style="invis")
        #                 if compteur % 2 == 0:
        #                     gsub.edge(str(compteur_du_parent) + ":d:c",
        #                               str(compteur),
        #                               style="invis")  # , weight=str(2**i-1))
        #                 elif compteur != 1:
        #                     gsub.edge(str(compteur_du_parent) + ":g:c",
        #                               str(compteur),
        #                               style="invis")  # , weight=str(2**i-1))
        #             compteur += 1

    def hauteur(self, noeud=None):
        if noeud is None:
            noeud = self.racine
        return self._hauteur_rec(noeud, 0)

    def _hauteur_rec(self, noeud, h):
        if noeud.gauche is None and noeud.droit is None:
            return h + 1
        g = h if noeud.gauche is None else self._hauteur_rec(noeud.gauche,
                                                             h + 1)
        d = h if noeud.droit is None else self._hauteur_rec(noeud.droit,
                                                            h + 1)
        return max(g, d)

    def _parcours_prof(self, type_parcours, noeud=None):
        if noeud is None:
            noeud = self.racine
        return self._parcours_prof_rec(type_parcours, noeud, [])

    def _parcours_prof_rec(self, type_parcours, noeud_courant=None, liste=[]):
        #
        if type_parcours == "prefixe":
            liste.append(noeud_courant)
        if noeud_courant.gauche is not None:
            self._parcours_prof_rec(type_parcours, noeud_courant.gauche, liste)
        if type_parcours == "infixe":
            liste.append(noeud_courant)
        if noeud_courant.droit is not None:
            self._parcours_prof_rec(type_parcours, noeud_courant.droit, liste)
        if type_parcours == "suffixe":
            liste.append(noeud_courant)
        return liste

    def _parcours_largeur(self, noeud=None):
        liste = []
        f = File()
        if noeud is None:
            noeud = self.racine
        f.enfiler(noeud)
        while not f.est_vide:
            n = f.defiler()
            liste.append(n)
            if n.gauche is not None:
                f.enfiler(n.gauche)
            if n.droit is not None:
                f.enfiler(n.droit)
        return liste

    def _parcours_largeur_numerote(self, noeud=None):
        liste = []
        f = File()
        if not noeud:
            noeud = self.racine
        #
        f.enfiler((noeud, 1))
        while not f.est_vide:
            n, numero = f.defiler()
            # on comble le vide depuis la dernière insertion
            liste += [None] * (numero - len(liste) - 1)
            liste.append(n)
            if n.gauche is not None:
                f.enfiler((n.gauche, 2 * numero))
            if n.droit is not None:
                f.enfiler((n.droit, 2 * numero + 1))
        return liste

    def rotation_droite(self, noeud):
        changement_racine = noeud == self.racine
        # processus à partir de :
        # https://upload.wikimedia.org/wikipedia/commons/1/15/Tree_Rotations.gif
        pivot = noeud.gauche
        if pivot.droit is not None:
            noeud.gauche = pivot.droit
            pivot.droit.parent = noeud
        else:
            noeud.gauche = None
        pivot.droit = noeud
        # on agit aussi sur le parent de noeud
        if noeud.parent is not None and noeud.parent.gauche == noeud:
            noeud.parent.gauche = pivot
        elif noeud.parent is not None and noeud.parent.droit == noeud:
            noeud.parent.droit = pivot
        #
        pivot.parent = noeud.parent
        noeud.parent = pivot
        #
        if changement_racine:
            self.racine = pivot

    def rotation_gauche(self, noeud):
        changement_racine = noeud == self.racine
        # processus à partir de :
        # https://upload.wikimedia.org/wikipedia/commons/1/15/Tree_Rotations.gif
        pivot = noeud.droit
        if pivot.gauche is not None:
            pivot.gauche.parent = noeud
            noeud.droit = pivot.gauche
        else:
            noeud.droit = None
        pivot.gauche = noeud
        # on agit aussi sur le parent de noeud
        if noeud.parent is not None and noeud.parent.gauche == noeud:
            noeud.parent.gauche = pivot
        elif noeud.parent is not None and noeud.parent.droit == noeud:
            noeud.parent.droit = pivot
        #
        pivot.parent = noeud.parent
        noeud.parent = pivot
        #
        if changement_racine:
            self.racine = pivot
