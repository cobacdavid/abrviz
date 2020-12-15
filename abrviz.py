__author__ = "david cobac"
__date__ = 20201215


import graphviz
import random

def est_plus_petit(element1, element2, fonction=None):
    if not fonction: fonction = lambda a, b: a < b
    return fonction(element1, element2)


class Arbre:
    def __init__(self):
        self.liste = []

    def ajoute_noeud(self, valeur):
        indice = 1
        trouve = False if self.liste else True 

        while not trouve:
            if est_plus_petit(self.liste[indice - 1], valeur):
                indice = 2 * indice + 1
            else:
                indice = indice * 2
            trouve = indice > len(self.liste) or self.liste[indice-1] is None

        if len(self.liste) < indice:
            self.liste += [None] * (indice - len(self.liste))
        self.liste[indice - 1] = valeur


def visu(arbre, nom_fichier, format):
    g = graphviz.Digraph(engine="dot")
    g.attr("node", shape="record")
    g.attr("edge", headport="n")
    g.attr("edge", tailclip="false")
    #
    visunoeud(g, arbre.liste, 1)
    g.render(nom_fichier, format=format)


def visunoeud(graphe, liste, indice):
    contenu = liste[indice - 1]
    if contenu is None: return
    
    contenug = liste[2*indice - 1] if 2 * indice <= len(liste) else None
    contenud = liste[2*indice] if 2 * indice + 1 <= len(liste) else None

    graphe.node(str(contenu), label="{" + str(contenu)+ "|{<g>|<d>}}")

    if contenug is None:
        graphe.node(str(contenu) + "invisg", style="invis")
        graphe.edge(str(contenu) + ":g:c", str(contenu) + "invisg",
                    style="invis", weight="-100")
    else:
        graphe.edge(str(contenu) + ":g:c", str(contenug), weight="100")
        
    if contenud is None:
        graphe.node(str(contenu) + "invisd", style="invis")
        graphe.edge(str(contenu) + ":d:c", str(contenu) + "invisd",
                    style="invis", weight="-100")
    else:
        graphe.edge(str(contenu) + ":d:c", str(contenud), weight="100")

    if 2*indice - 1 < len(liste):
        visunoeud(graphe, liste, 2 * indice)
    if 2*indice < len(liste):
        visunoeud(graphe, liste, 2*indice + 1)



liste = list(range(20))
random.shuffle(liste)

a = Arbre()
for i in liste:
    a.ajoute_noeud(i)

visu(a, "test", "png")
