# *Python : an introduction to programming* - second edition (Parker, 2021)

## Chapter 1 : Computers and programming

La plupart des ordinateurs sont des *digital computers* : ce sont des ordinateurs qui manipulent des nombres (les programmes sont encodés en caractères humainement compréhensibles). Les *analog computers* sont plus rares et manipulent plutôt des signaux électriques, ou sont mécaniques.

En programmation, on a plutôt besoin d'arithmétique en terme de mathématiques.

### **Solving a problem using a computer**
---

Le processus de résolution de problème commence avec une spécification détaillée du problème à résoudre. Il faut comprendre complètement le problème pour que celui-ci puisse être résolu à l'aide d'un ordi. On divise ensuite le problème en une partie qu'on sait résoudre avec nos moyens actuels (méthodes et programmes en notre possession) et en une partie qu'on ne sait pas résoudre.

**Pseudocode** : grandes lignes de la solution, souvent notées par écrit.\
**Script / source cocde / computer program** : le programme en langage de programmation qui résulte du pseudocode.\
**Compileur** : programme qui convertit notre code en code machine (0 et 1) que peut comprendre l'ordinateur.

">>>" en début de ligne = *a prompt*, on se trouve dans l'interpréteur Python.

IDE = "Integrated development environment", c'est un logiciel qui contient un environnement nécessaire au développement (éditeur de texte, débugger...).

Dans un langage de programmation, on trouve :
- des symboles ayant une signification (ex : *+* = *add*, *-* = *substract*)
- des ***reserved words***, des mots-clés qui sont définis par le langage et leur sens ne peut pas être changé par le programmeur (on ne peut pas les utiliser comme noms de variables donc - ex : *if*, *while*, *True*)
- des ***system variables*** qui ont une signification définie par le langage et peuvent être rétuilisées par le programmeur.
- des ***variables*** et des ***fonctions*** qui sont des termes définies par le programmeur pour être utilisées ensuite dans le code.

### Guess a number
---
Plusieurs variantes du jeu :
- Deviner de façon précise le nombre : une personne choisit un nombre dans un intervalle spécifique (le *chooser*) et une personne devine (le *guesser*). Si elle devine le nombre, elle a gagné.
- Identique + "plus grand" ou "plus petit".
- Plusieurs guessers avec une seule tentative, le plus proche gagne. En cas d'égalité, on recommence.

#### Solving the *guess a number* problem

**1ère version** : l'ordinateur choisit un nombre dans un intervalle et l'utilisateur doit le deviner.

1. L'ordinateur choisit un nombre.

2. L'ordinateur demande au joueur de deviner.

3. Le joueur tape un nombre entier et l'ordinateur l'analyse.

4. L'ordinateur compare l'input utilisateur avec celui qu'il a choisit ; s'ils sont identiques, le joueur a gagné, sinon l'ordinateur a gagné.

Pré-requis Python : imprimer un message dans le prompt, lire un nombre, pouvoir le stocker dans une variable, pouvoir comparer deux nombres et avoir deux issues possibles en fonction du résultat de cette comparaison.

**2ème version** : identique à la précédente mais on répète le processus si la réponse est mauvaise, jusqu'à ce que ce soit correct.

1. L'ordinateur choisit un nombre.

2. L'ordinateur demande au joueur de deviner.

3. Le joueur tape un nombre entier et l'ordinateur l'analyse.

4. L'ordinateur compare l'input utilisateur avec le nombre qu'il a choisit ; s'ils sont identiques, le joueur a gagné. **On se rend directement à l'étape 7.**

5. L'ordinateur détermine si le nombre est supérieur ou inférieur au nombre choisi et print le message.

6. **On répète depuis l'étape 2.**

7. Fin du jeu.

Le mécanisme de répétitions est le seul nouvel aspect par rapport à la version 1, mais la notion de **boucle** est très importante dans les langages de programmation.

### Rock-paper-scissors
---

Deux joueurs choisissent un item de la liste (pierre, feuille, ciseaux) et révèlent simultanément leur choix. Si l'item est identique, on recommence. Sinon, la feuille/le papier bat la pierre, la pierre bat le ciseau et le ciseau bat la feuille/le papier.

#### Solving the *rock-paper-scissors* problem

1. L'ordinateur choisit l'un des trois items et enregistre ce choix dans une variable ***choice***.

2. Demander au joueur de choisir. On peut utiliser une valeur numérique comme 1 = rock, 2 = paper et 3 = scissors. On peut aussi utiliser un module de random qui choisit parmi une liste d'éléments, pas forcément des entiers.

3. Lire le choix du joueur dans la variable ***player***.

4. Si **player** == **choice** :\
&emsp;Print "Egalité. Recommençons."\
&emsp;**Répéter depuis l'étape 1.**

5. Si **player** == 1 (rock) :\
&emsp;Si **choice** == paper, **aller à l'étape 8.**\
&emsp;Sinon, **aller à l'étape 9.**

6. Si **player** == 2 (paper) :\
&emsp;Si **choice** == scissors, **aller à l'étape 8.**\
&emsp;Sinon, **aller à l'étape 9.**

7. Si **player** == 3 (scissors) :\
&emsp;Si **choice** == rock, **aller à l'étape 8.**\
&emsp;Sinon, **aller à l'étape 9.**

8. Print "L'ordinateur a gagné." et fermer le programme.

9. Print "Vous avez gagné." et fermer le programme.