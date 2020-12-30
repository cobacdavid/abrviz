from abrviz import Arbre
import random
import string

liste = list(range(20))
random.shuffle(liste)

a = Arbre()
for i in liste:
    a.inserer(i)

a.sortie("test_1", "png")
print(f"liste de départ\n\t{a.liste_insertion}")
print(f"parcours préfixe\n\t{a.prefixe}")
print(f"parcours infixe\n\t{a.infixe}")
print(f"parcours suffixe\n\t{a.suffixe}")
print(f"Taille : {a.taille}\nHauteur : {a.hauteur}")

print()

liste = list(string.ascii_letters)
random.shuffle(liste)
b = Arbre()
for i in liste:
    b.inserer(i)
b.fonction_ordre = lambda x, y: str(x) < str(y)
b.sortie("test_2", "png")
print(f"liste de départ\n\t{b.liste_insertion}")
print(f"parcours préfixe\n\t{b.prefixe}")
print(f"parcours infixe\n\t{b.infixe}")
print(f"parcours suffixe\n\t{b.suffixe}")
print(f"Taille : {b.taille}\nHauteur : {b.hauteur}")
