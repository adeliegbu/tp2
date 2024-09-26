"""
objectifs : réaliser le TP2, réaliser un automate qui vérifie si une phrase saisie est correcte syntaxiquement ou non.
date : 26 sept 2024
par : Adélie GIBOU
codé en python
programme des fonctions
"""



#définitions des Types:

#je définis l'alphabet des entrées
#nos entrées sont les articles(0), les adjectifs(1), les noms(2), les verbes(3), les noms propres(4), les points(5)
entrees = (0, 1, 2, 3, 4, 5)

#je définis l'ensemble des états
etats = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

#je définis l'alphabet des sorties
sorties = ("corecte", "incorrecte")


#définitions des Tables:

#je définis les transitions d'états 
table_de_transitions = [[1, 8, 8, 8, 4, 8],
                       [8, 1, 2, 8, 8, 8],
                       [8, 2, 8, 3, 8, 8],
                       [5, 8, 8, 8, 7, 9],
                       [8, 8, 8, 3, 8, 8],
                       [8, 5, 6, 8, 8, 8],
                       [8, 6, 8, 8, 8, 9],
                       [8, 8, 8, 8, 8, 9],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0]]

#je définis les sorties
#la sortie 8 correspond à une phrase incorrecte et la sortie 9 à une phrase correcte
table_de_sortie = [8, 9]


#définitions des Fonctions:

#j'écris une fonction qui transforme la phrase en une liste des valeurs qui sont associées à chaque mot (ex: "julie mange ." devient [4, 3 ,5])
def decoder(phrase):
    liste = phrase.split()
    if "." in liste[-1] and liste[-1] != ".": #si un point final est directement collé au dernier mot, je le supprime du mot pour rajouter un nouveau point qui sera un nouvel élément de la liste
        liste[-1] = liste[-1].rstrip(".")
        liste.append(".")
    return [dictionnaire[i] for i in liste]

#j'écris une fonction qui détermine l'état final de la phrase (8 ou 9)
def test(phrase):
    etat = 0 #on commence le test à l'état 0
    while etat < 8 : #le test s'arrête quand on est dans l'état 8 ou l'état 9 (la phrase est alors incorrecte ou correcte), tant qu'on est dans les etats de intermédiaires (de 0 à 7) on continue le test
        for i in range (len(decoder(phrase))):
            etat = table_de_transitions[etat][decoder(phrase)[i]]
    return etat
    
#j'écris une fonction qui associe l'état final de la phase à "incorrect" (pour 8) ou "correct" (pour 9)    
def reponse(phrase):
    if test(phrase) == 8:
        return ("incorrecte.")
    else :
        return ("correcte.")
