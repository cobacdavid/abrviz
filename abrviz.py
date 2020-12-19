__author__ = "david cobac"
__date__ = 20201215

import graphviz


def est_plus_petit(element1, element2, fonction=None):
    if not fonction: fonction = lambda a, b: a < b
    return fonction(element1, element2)


class Arbre:
    def __init__(self):
        self.liste = []
        self.fonction_ordre = None
        self.graphe = graphviz.Digraph(engine="dot")

    def set_fonction_ordre(self, fonction):
        self.fonction_ordre = fonction

    def ajoute_noeud(self, valeur):
        indice = 1
        trouve = False if self.liste else True 
        #
        while not trouve:
            if est_plus_petit(self.liste[indice - 1], valeur,
                              self.fonction_ordre):
                indice = 2 * indice + 1
            else:
                indice = indice * 2
            trouve = indice > len(self.liste) or self.liste[indice-1] is None
            #
        if len(self.liste) < indice:
            self.liste += [None] * (indice - len(self.liste))
        self.liste[indice - 1] = valeur

    def sortie(self, nom_fichier, format):
        self.graphe.attr("node", shape="record")
        self.graphe.attr("edge", headport="n")
        self.graphe.attr("edge", tailclip="false")
        #
        self._visunoeud(self.graphe, 1)
        self.graphe.render(nom_fichier, format=format)

    def prefixe(self, indice=1, resultat=[]):
        if indice - 1 < len(self.liste):
            if self.liste[indice - 1] is not None:
                resultat.append(self.liste[indice - 1])
            self.prefixe(2 * indice, resultat)
            self.prefixe(2 * indice + 1, resultat)
        return resultat

    def infixe(self, indice=1, resultat=[]):
        if indice - 1 < len(self.liste):
            self.infixe(2 * indice, resultat)
            if self.liste[indice - 1] is not None:
                resultat.append(self.liste[indice - 1])
            self.infixe(2 * indice + 1, resultat)
        return resultat

    def suffixe(self, indice=1, resultat=[]):
        if indice - 1 < len(self.liste):
            self.suffixe(2 * indice, resultat)
            self.suffixe(2 * indice + 1, resultat)
            if self.liste[indice - 1] is not None:
                resultat.append(self.liste[indice - 1])
        return resultat


    def _visunoeud(self, graphe, indice):
        contenu = self.liste[indice - 1]
        if contenu is None: return

        N = len(self.liste)

        indice_gauche = 2 * indice
        indice_droit = indice_gauche + 1
        contenug = self.liste[indice_gauche - 1] if indice_gauche <= N else None
        contenud = self.liste[indice_droit - 1] if indice_droit <= N else None

        with graphe.subgraph(name=str(contenu) + "sub") as gsub:
            gsub.node(str(contenu), label="{" + str(contenu)+ "|{<g>|<d>}}")
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



if __name__ == "__main__":
    import random
    
    
    liste = list(range(20))
    random.shuffle(liste)

    a = Arbre()
    # a.set_fonction_ordre(lambda x, y: str(x) < str(y))
    for i in liste:
        a.ajoute_noeud(i)

    a.sortie("test", "png")

    print(a.prefixe())
    print(a.infixe())
    print(a.suffixe())
