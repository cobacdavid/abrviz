# abrviz

## usage

``` python
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
```

# Sortie image

<img src="test.png" width="800">

# Sorties parcours

``` python
[16, 1, 0, 13, 3, 2, 9, 8, 5, 4, 6, 7, 11, 10, 12, 14, 15, 17, 18, 19]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
[0, 2, 4, 7, 6, 5, 8, 10, 12, 11, 9, 3, 15, 14, 13, 1, 19, 18, 17, 16]
```

## Licence
CC-BY-NC-SA
