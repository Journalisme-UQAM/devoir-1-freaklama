#coding: utf-8
### N'oublie jamais la première ligne, ci-dessus
### Mes commentaires seront précédés de trois «#» pour les distinguer des lignes de ton script que j'ai mises en commentaire

### J'ai mis la ligne ci-dessous en commentaire, car elle fait planter le script en partant
# /devoir1.py
salut = list(range(30000,100000))
print(salut) # Ici, tu affiches le contenu de la liste salut d'un seul coup, avec les crochets et les virgules entre chaque élément
bonjour = list(range(00000,18000))
for num in bonjour:
    print("{:05d}".format(num)) # Ici, tu affiches le contenu de la liste bonjour un élément à la fois, en prenant soin de le formater correctement
    
    ### J'ai également mis la ligne suivante en commentaire, car elle fait aussi planter le script
    # Pas le format la plus optimal, je ne comprends pas comment les printer ensemble.

### Bien! Ici, il faut juste faire un petit changement pour que ça fonctionne:
### Après la création de la liste «salut», fais une boucle qui passe à travers chaque élément et qui l'affiche, comme ceci:

for numero in salut:
	print(numero)