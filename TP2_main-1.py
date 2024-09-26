"""
objectifs : réaliser le TP2, réaliser un automate qui vérifie si une phrase saisie est syntaxiquement correcte ou non.
date : 26 sept 2024
par : Adélie GIBOU
codé en python
programme principal
"""

import TP2_fonctions as f


dictionnaire = {"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4, "mange" : 3, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1, "bleu" : 1, "verte" : 1, "dort" : 3,"julie" : 4, "jean" : 4, "." : 5}

phrase_a_tester = str (input("Saisissez une phrase à tester : "))
print ("La phrase saisie est syntaxiquement", f.reponse(phrase_a_tester))